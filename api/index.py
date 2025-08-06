from urllib.parse import parse_qs
import json

from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        print('post_data', post_data)

        # Decode and parse form data
        try:
            form_data = parse_qs(post_data.decode('utf-8'))
            # Flatten single-value lists for convenience
            data = {k: v[0] if len(v) == 1 else v for k, v in form_data.items()}
        except Exception as e:
            data = {"error": f"Could not parse form data: {str(e)}"}

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response = {
            "message": "POST request received!",
            "data": data
        }

        self.wfile.write(json.dumps(response).encode('utf-8'))
        return
