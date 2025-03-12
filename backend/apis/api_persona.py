from http.server import BaseHTTPRequestHandler
from model.persona import Persona

class PersonaAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/persona":
            persona = Persona("Kevin", "Calvo", "kevinyadir@hotmail.com")
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(str(persona).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()
