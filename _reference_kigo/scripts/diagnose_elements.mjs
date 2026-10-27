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

  const result = await send('Runtime.evaluate', {
    expression: `
      (() => {
        const info = {};
        
        // 1. Check nav items
        const nav = document.querySelector('.header__navigation');
        if (nav) {
          const comp = window.getComputedStyle(nav);
          info.header_navigation = {
            display: comp.display,
            visibility: comp.visibility,
            width: nav.offsetWidth,
            height: nav.offsetHeight,
            childrenCount: nav.children.length
          };
        } else {
          info.header_navigation = 'NOT FOUND';
        }

        // 2. Check Japanese calligraphy
        const cal = document.querySelector('.spring-calligraphy');
        if (cal) {
          const comp = window.getComputedStyle(cal);
          info.calligraphy = {
            display: comp.display,
            visibility: comp.visibility,
            opacity: comp.opacity,
            width: cal.getBoundingClientRect().width,
            height: cal.getBoundingClientRect().height,
            viewBox: cal.getAttribute('viewBox')
          };
        } else {
          info.calligraphy = 'NOT FOUND';
        }

        // 3. Check clients section
        const clients = document.querySelector('#clients');
        if (clients) {
          const rect = clients.getBoundingClientRect();
          const comp = window.getComputedStyle(clients);
          info.clients = {
            top: rect.top + window.scrollY,
            height: rect.height,
            display: comp.display,
            visibility: comp.visibility,
            opacity: comp.opacity
          };
        } else {
          info.clients = 'NOT FOUND';
        }

        // 4. Check hero landscape image
        const img = document.querySelector('.hero__landscape img');
        if (img) {
          info.hero_landscape = {
            src: img.src,
            naturalWidth: img.naturalWidth,
            naturalHeight: img.naturalHeight,
            complete: img.complete
          };
        }

        // 5. Check all sections tops and heights
        info.sections = Array.from(document.querySelectorAll('section, footer')).map(s => ({
          tag: s.tagName,
          id: s.id,
          cls: s.className,
          top: s.getBoundingClientRect().top + window.scrollY,
          height: s.getBoundingClientRect().height
        }));

        return info;
      })()
    `,
    returnByValue: true
  });

  if (result.result && result.result.value) {
    console.log(JSON.stringify(result.result.value, null, 2));
  } else {
    console.log("Full result:", JSON.stringify(result, null, 2));
  }
  ws.close();
} finally {
  chrome.kill();
}
