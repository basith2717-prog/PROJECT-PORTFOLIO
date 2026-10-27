import puppeteer from 'puppeteer';
const browser = await puppeteer.launch({ args: ['--no-sandbox'] });
const page = await browser.newPage();
await page.setViewport({ width: 1440, height: 900 });
await page.goto('http://localhost:5173/', { waitUntil: 'networkidle0', timeout: 20000 });

const el = await page.$('#clients');
const box = await el.boundingBox();
console.log('Clients section bounds:', JSON.stringify(box));

// Scroll to section
await page.evaluate((y) => window.scrollTo(0, y - 80), box.y);
await new Promise(r => setTimeout(r, 800));

// Resize viewport tall enough to see whole section
const h = Math.min(Math.ceil(box.height) + 120, 3000);
await page.setViewport({ width: 1440, height: h });
await page.evaluate((y) => window.scrollTo(0, y - 80), box.y);
await new Promise(r => setTimeout(r, 400));

await page.screenshot({ path: 'clients_full.png', fullPage: false });
console.log('Captured clients_full.png');
await browser.close();
