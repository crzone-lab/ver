import subprocess
import time
import urllib.request
import json

chrome = subprocess.Popen([
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--headless=new',
    '--disable-gpu',
    '--remote-debugging-port=9222',
    '--window-size=412,840',
    'file:///Users/crzone/.gemini/antigravity/scratch/fruit-rabbit-touch-engine/index.html'
])

time.sleep(2.5)

resp = urllib.request.urlopen('http://localhost:9222/json')
targets = json.loads(resp.read().decode())
target = next(t for t in targets if t['type'] == 'page' and not t['url'].startswith('chrome-extension'))

print("Connected to target:", target['url'])

# Send CDP HTTP evaluate commands via websocket framing using python
