import sys
import http.client
import http.server
import socketserver
import json
import urllib

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

def main():
  if(len(sys.argv) != 2):
    print("Usage: python3 server.py /PATH")
  elif(sys.argv[1][0] != "/"):
    print("Invalid path. Path must begin with '/'")
  else:
    path = sys.argv[1]
    uncensoredData = request(host1, path)
    parsed = urllib.parse.quote(uncensoredData["message"])
    censoredData = request(host2, "/service/json?text=" + parsed)
    censoredData["subtitle"] = uncensoredData["subtitle"]

    string = json.dumps(censoredData, indent=2)
    print(string)   

if __name__ == "__main__":
  main()