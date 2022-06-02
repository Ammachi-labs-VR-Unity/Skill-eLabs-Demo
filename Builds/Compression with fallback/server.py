import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
# Make sure the server is created at current directory

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        print('PATH: ' + path)
        # if(path.endswith(".gz")):
        #     self.send_header('Content-Encoding','gzip')
        #     super().do_GET() 
        #     return
        # print(self.headers)
        # self.end_headers()
        super().do_GET()
        # self.send_response(200)
        # self.send_header('Content-Encoding','gzip')
        # self.end_headers()
        # # Send the html message
        # os.chdir('.')  
        # super.do_GET()      
        # return

    def end_headers (self):
        path = self.path
        if(path.endswith(".gz")):
            self.send_header('Content-Encoding','gzip')
            SimpleHTTPRequestHandler.end_headers(self)
            return
        SimpleHTTPRequestHandler.end_headers(self)

    # def end_headers (self):
    #     # self.send_header('Content-Encoding', 'gzip')
    #     SimpleHTTPRequestHandler.end_headers(self)

server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=MyHandler)
# Start the web server
print("hello")
server_object.serve_forever()



# os.chdir('.')  

# DIRECTORY = '.'

# class Handler(SimpleHTTPRequestHandler):
#     def send_response(self, *args, **kwargs):
#         print("send_response")
#         SimpleHTTPRequestHandler.send_response(self, *args, **kwargs)
#         self.send_header('Content-Encoding', 'gzip')
#         os.chdir('.') 

#     def do_GET(self):
#     	self.do_GET()
# #         print   ('Get request received')
# #         self.send_response(200)
# #         self.send_header('Content-Encoding','gzip')
# #         self.end_headers()
# #         # Send the html message
# #         os.chdir('.')  
# #         super.do_GET()      
# #         return 

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, directory=DIRECTORY, **kwargs)

# # Create server object listening the port 80
# server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=Handler)
# # Start the web server
# print("hello")
# server_object.serve_forever()

# from http.server import BaseHTTPRequestHandler,HTTPServer
# import os
# os.chdir('.')  

# PORT_NUMBER = 7777

# #This class will handles any incoming request from
# #the browser 
# class myHandler(BaseHTTPRequestHandler):
	
# 	#Handler for the GET requests
# 	def do_GET(self):
# 		self.send_response(200)
# 		self.send_header('Content-type','text/html')
# 		self.end_headers()
# 		# Send the html message
# 		# self.wfile.write("Hello World !")
# 		return

# try:
# 	#Create a web server and define the handler to manage the
# 	#incoming request
# 	server = HTTPServer(('', PORT_NUMBER), myHandler)
# 	print('Started httpserver on port ' , PORT_NUMBER)
	
# 	#Wait forever for incoming htto requests
# 	server.serve_forever()

# except KeyboardInterrupt:
# 	print('^C received, shutting down the web server')
# 	server.socket.close()

# import os
# from http.server import HTTPServer, CGIHTTPRequestHandler
# # Make sure the server is created at current directory
# os.chdir('.')
# # Create server object listening the port 80
# server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
# # Start the web server
# server_object.serve_forever()