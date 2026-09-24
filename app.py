from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.wfile.write(
            b"Hello from MicroApp - Jenkins CI/CD"
        )


server = HTTPServer(("0.0.0.0", 8080), Handler)

print("MicroApp listening on port 8080")

server.serve_forever()