import { spawn } from 'child_process';
import fs from 'fs';

const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const chrome = spawn(chromePath, [
  '--headless=new',
  '--remote-debugging-port=9222',
  '--disable-gpu',
  '--window-size=1440,900',
  'about:blank'
]);

await new Promise(r => setTimeout(r, 1500));

try {
  const listResp = await fetch('http://localhost:9222/json');
  const targets = await listResp.json();
  const pageTarget = targets.find(t => t.type === 'page') || targets[0];
  const ws = new WebSocket(pageTarget.webSocketDebuggerUrl);

  await new Promise((res, rej) => {
    ws.onopen = res;
    ws.onerror = rej;
  });

  let id = 1;
  const callbacks = new Map();
  ws.onmessage = (event) => {
    const msg = JSON.parse(event.data);
    if (msg.id && callbacks.has(msg.id)) {
      callbacks.get(msg.id)(msg);
      callbacks.delete(msg.id);
    }
  };

  function send(method, params = {}) {
    return new Promise((res) => {
      const msgId = id++;
      callbacks.set(msgId, res);
      ws.send(JSON.stringify({ id: msgId, method, params }));
    });
  }

  await send('Page.navigate', { url: 'http://localhost:5173/' });
  await new Promise(r => setTimeout(r, 2000));

  const sections = [
    { name: '0_hero', sel: '#hero' },
    { name: '1_clients', sel: '#clients' },
    { name: '1b_services_1', sel: '#serviceItem1' },
    { name: '1b_services_2', sel: '#serviceItem2' },
    { name: '1b_services_3', sel: '#serviceItem3' },
    { name: '1b_services_4', sel: '#serviceItem4' },
    { name: '2_work', sel: '.home-work' },
    { name: '3_exp', sel: '#experience' },
    { name: '4_faq', sel: '#faq' },
    { name: '5_contact', sel: '#contact' },
    { name: '6_footer', sel: 'footer' }
  ];

  for (const s of sections) {
    await send('Runtime.evaluate', {
      expression: `(() => { const el = document.querySelector('${s.sel}'); if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' }); })()`
    });
    await new Promise(r => setTimeout(r, 400));
    const ss = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(`sec_${s.name}.png`, Buffer.from(ss.result.data, 'base64'));
    console.log(`Captured sec_${s.name}.png`);

    // Extra scrolled view for clients section to see full dancer + logos
    if (s.name === '1_clients') {
      await send('Runtime.evaluate', { expression: `window.scrollBy(0, 700)` });
      await new Promise(r => setTimeout(r, 400));
      const ss2 = await send('Page.captureScreenshot', { format: 'png' });
      fs.writeFileSync(`sec_1_clients_b.png`, Buffer.from(ss2.result.data, 'base64'));
      console.log(`Captured sec_1_clients_b.png`);
    }
  }

  ws.close();
} finally {
  chrome.kill();
}
