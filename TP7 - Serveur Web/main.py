import http.server
from urllib.parse import urlparse, parse_qs, unquote
import csv
import base64

PORT = 8888
DATA_FILE = "data.txt"
CREDENTIALS_FILE = "mdp.csv"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse the request URL
        url = urlparse(self.path)
        path = unquote(url.path)

        # Check if the request is for "/index.html", serve the content of index.html as HTML
        if path == '/index.html':
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()

            # Read the content of index.html and send it as the response
            with open("index.html", "rb") as file:
                html_content = file.read().decode("utf-8")
                self.wfile.write(html_content.encode("utf-8"))
        elif path == '/view_data':
            # Check if the request is for "/view_data", require authentication
            auth_header = self.headers.get('Authorization')
            if auth_header is None or not self.authenticate_user(auth_header):
                # Unauthorized, send 401 response with WWW-Authenticate header
                self.send_response(401)
                self.send_header('WWW-Authenticate', 'Basic realm="Auth Required"')
                self.send_header("Content-type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(b"Authentication required.")
            else:
                # Authorized, serve the content of the data file
                self.send_response(200)
                self.send_header("Content-type", "text/plain; charset=utf-8")
                self.end_headers()

                # Read the content of the data file and send it as the response
                try:
                    with open(DATA_FILE, "r", encoding="utf-8") as file:
                        data_content = file.read()
                        self.wfile.write(data_content.encode("utf-8"))
                except FileNotFoundError:
                    self.wfile.write(b"No data available.")
        else:
            # For other requests, serve files using the default SimpleHTTPRequestHandler
            super().do_GET()

    def do_POST(self):
        # Parse the request URL
        url = urlparse(self.path)
        path = unquote(url.path)

        # If the request is for "/index.html", handle the POST data
        if path == '/index.html':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            parsed_data = parse_qs(post_data)

            # Extract and print the 'name' parameter from the form
            if 'name' in parsed_data:
                name = parsed_data['name'][0]
                print(f"Nom soumis : {name}")

                # Store the data in a file
                with open(DATA_FILE, "a", encoding="utf-8") as data_file:
                    data_file.write(f"Nom : {name}\n")

            # Respond with a simple message
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            response_message = "<html><body><h1>Données reçues avec succès!</h1></body></html>"
            self.wfile.write(response_message.encode("utf-8"))
        else:
            # For other POST requests, serve files using the default SimpleHTTPRequestHandler
            super().do_POST()

    def authenticate_user(self, auth_header):
        # Check if the provided username/password in the Authorization header is valid
        credentials = self.get_credentials(auth_header)
        if credentials:
            username, password = credentials
            with open(CREDENTIALS_FILE, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                for row in reader:
                    if len(row) == 2 and row[0] == username and row[1] == password:
                        return True
        return False

    def get_credentials(self, auth_header):
        # Extract username and password from the Authorization header
        try:
            auth_type, auth_data = auth_header.split(' ', 1)
            if auth_type.lower() == 'basic':
                decoded_data = base64.b64decode(auth_data).decode('utf-8')
                return tuple(decoded_data.split(':', 1))
        except Exception:
            pass
        return None

def run_server():
    server_address = ("", PORT)
    server = http.server.HTTPServer(server_address, CustomHandler)
    print("Serveur actif sur le port :", PORT)
    server.serve_forever()

if __name__ == "__main__":
    run_server()
