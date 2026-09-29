import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


def response_for(path):
    if path == "/health":
        return 200, {"status": "healthy"}
    if path == "/":
        return 200, {"message": "DevSecOps practice application"}
    return 404, {"error": "not found"}


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        status, payload = response_for(self.path)
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", 8000), RequestHandler)
    print("Practice application running at http://localhost:8000")
    server.serve_forever()
