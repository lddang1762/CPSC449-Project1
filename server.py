import sys
import http.client
import http.server
import socketserver
import json
import urllib

PORT = 8080

host1 = "www.foaas.com"
host2 = "www.purgomalum.com"

def request(host, path):
  connection = http.client.HTTPSConnection(host)
  header = {"Accept": "application/json"}
  connection.connect()
  connection.request("GET", path, "", header)
  response = connection.getresponse().read()
  data = json.loads(response)  
  connection.close()
  return data

# def main():
#     path = sys.argv[1]
#     uncensoredData = request(host1, path)
#     parsed = urllib.parse.quote(uncensoredData["message"])
#     censoredData = request(host2, "/service/json?text=" + parsed)
#     censoredData["subtitle"] = uncensoredData["subtitle"]

#     string = json.dumps(censoredData, indent=2)
#     print(string)    

class Generator(http.server.BaseHTTPRequestHandler):
  def do_GET(self):    
    self.send_response(200)
    self.send_header('Content-Type', 'text/html; charset=utf-8')
    self.end_headers()

    path = self.path
    uncensoredData = request(host1, path)
    parsed = urllib.parse.quote(uncensoredData["message"])
    censoredData = request(host2, "/service/json?text=" + parsed)
    censoredData["subtitle"] = uncensoredData["subtitle"]
    message = censoredData["result"]
    subtitle = censoredData["subtitle"]

    payload = (f'<html><head><title>FCPSC 449 - Project 1</title>'
              f'<meta charset="utf-8" />'
              f'<meta name="viewport" content="width=device-width, initial-scale=1" />'
              f'<link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.min.css" rel="stylesheet" /></head>'
              f'<body style="margin-top: 40px"><div class="container"><div id="view-10"><div class="hero-unit">'
              f'<h1>{message}</h1>'
              f'<p><em>{subtitle}</em></p></div></div>'
              f'<p style="text-align: center"><a href="https://foaas.com">foaas.com</a></p></div></body></html>'
              f'')
    self.wfile.write(payload.encode('utf-8'))

with socketserver.TCPServer(("", PORT), Generator) as httpd:
    print("serving at port", PORT)
    print("Please open your web browser and navigate to localhost:8000")
    httpd.serve_forever()
    
