import subprocess
import time
import json
import urllib.request
import asyncio
import os

# Start Chrome in background
cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--headless=new",
    "--remote-debugging-port=9222",
    "--disable-gpu",
    "--window-size=1440,900",
    "http://localhost:5173/"
]
proc = subprocess.Popen(cmd)
time.sleep(2)

try:
    with urllib.request.urlopen("http://localhost:9222/json") as resp:
        targets = json.loads(resp.read().decode())
    print("Chrome targets:", len(targets))
    ws_url = targets[0]["webSocketDebuggerUrl"]
    print("WebSocket URL:", ws_url)
finally:
    proc.terminate()
