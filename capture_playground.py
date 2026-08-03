import subprocess
import json
import time
import urllib.request
import os
import websocket

# Launch Chrome with remote debugging
chrome_cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless=new",
    "--disable-gpu",
    "--remote-debugging-port=9222",
    "--window-size=412,840",
    "https://fruit-rabbit-touch-engine.vercel.app"
]

proc = subprocess.Popen(chrome_cmd)
time.sleep(2.5)

try:
    # Fetch WebSocket debugger URL
    resp = urllib.request.urlopen("http://localhost:9222/json")
    targets = json.loads(resp.read().decode())
    ws_url = targets[0]['webSocketDebuggerUrl']

    ws = websocket.create_connection(ws_url)

    def send_cdp(method, params=None):
        cmd = {"id": 1, "method": method, "params": params or {}}
        ws.send(json.dumps(cmd))
        return json.loads(ws.recv())

    # Wait for page load
    time.sleep(1)

    # Click start button
    eval_click = {
        "expression": "document.querySelector('.start-game-btn') ? (document.querySelector('.start-game-btn').click(), 'clicked') : 'not_found'"
    }
    ws.send(json.dumps({"id": 2, "method": "Runtime.evaluate", "params": eval_click}))
    res = json.loads(ws.recv())
    print("Click result:", res)

    time.sleep(1.5)

    # Capture screenshot
    ws.send(json.dumps({"id": 3, "method": "Page.captureScreenshot", "params": {"format": "png"}}))
    shot_res = json.loads(ws.recv())

    import base64
    img_data = base64.b64decode(shot_res['result']['data'])
    out_path = "/Users/crzone/.gemini/antigravity/brain/827de87e-5067-4327-9014-bff4ce181bb6/playground_live_preview.png"
    with open(out_path, "wb") as f:
        f.write(img_data)
    print("Playground screenshot saved successfully to", out_path)

    ws.close()
finally:
    proc.terminate()
