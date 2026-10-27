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

  await send('Page.enable');
  await send('Runtime.enable');
  await send('DOM.enable');

  // Navigate to localhost:5173
  await send('Page.navigate', { url: 'http://localhost:5173/' });
  await new Promise(r => setTimeout(r, 2000));

  // Get dimensions of all main sections
  const evalResult = await send('Runtime.evaluate', {
    expression: `
      (() => {
        const sections = [
          'header',
          '#hero',
          '#clients',
          '.home-work',
          '#experience',
          '#faq',
          '#contact',
          'footer'
        ];
        return sections.map(sel => {
          const el = document.querySelector(sel);
          if (!el) return { sel, found: false };
          const rect = el.getBoundingClientRect();
          const comp = window.getComputedStyle(el);
          return {
            sel,
            found: true,
            top: rect.top + window.scrollY,
            left: rect.left,
            width: rect.width,
            height: rect.height,
            display: comp.display,
            position: comp.position,
            overflow: comp.overflow,
            visibility: comp.visibility,
            opacity: comp.opacity,
            zIndex: comp.zIndex
          };
        });
      })()
    `,
    returnByValue: true
  });

  console.log("Section metrics:");
  console.log(JSON.stringify(evalResult.result.value, null, 2));

  // Capture full page screenshot
  const metrics = await send('Page.getLayoutMetrics');
  const width = Math.ceil(metrics.result.contentSize.width);
  const height = Math.ceil(metrics.result.contentSize.height);
  console.log(`Page content size: ${width}x${height}`);

  // Capture viewport screenshot at top
  const ss1 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('ss_hero.png', Buffer.from(ss1.result.data, 'base64'));
  console.log("Saved ss_hero.png");

  // Scroll to work section and capture
  await send('Runtime.evaluate', {
    expression: `document.querySelector('.home-work')?.scrollIntoView();`
  });
  await new Promise(r => setTimeout(r, 500));
  const ss2 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('ss_work.png', Buffer.from(ss2.result.data, 'base64'));
  console.log("Saved ss_work.png");

  // Scroll to faq
  await send('Runtime.evaluate', {
    expression: `document.querySelector('#faq')?.scrollIntoView();`
  });
  await new Promise(r => setTimeout(r, 500));
  const ss3 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('ss_faq.png', Buffer.from(ss3.result.data, 'base64'));
  console.log("Saved ss_faq.png");

  // Scroll to contact
  await send('Runtime.evaluate', {
    expression: `document.querySelector('#contact')?.scrollIntoView();`
  });
  await new Promise(r => setTimeout(r, 500));
  const ss4 = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('ss_contact.png', Buffer.from(ss4.result.data, 'base64'));
  console.log("Saved ss_contact.png");

  ws.close();
} finally {
  chrome.kill();
}
