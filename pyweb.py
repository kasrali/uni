from http.server import HTTPServer, BaseHTTPRequestHandler
import serial
ser = serial.Serial("COM2", 9600)

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
       try:
           cc=str(ser.readline())
           file_to_open = '<html><head><meta http-equiv="refresh" content="1" ><style>p : { font-size = 40px; }</style></head><body><p> Gas Value: '+str(cc[2:][:-5])+'</p></body></html>'
           self.send_response(200)
       except:
           file_to_open = "File not found"
           self.send_response(404)
       self.end_headers()
       self.wfile.write(bytes(file_to_open, 'utf-8'))

httpd = HTTPServer(('localhost',8080),Serv)
httpd.serve_forever()