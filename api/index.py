import json

from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)

        # Optionally parse JSON body
        try:
            data = json.loads(post_data)
        except json.JSONDecodeError:
            data = {"error": "Invalid JSON"}

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response = {
            "message": "POST request received!",
            "data": data
        }

        self.wfile.write(json.dumps(response).encode('utf-8'))
        return
