import SocketServer
from client import Client

class Server:
	def __init__(self, port):
		self.clients = []
	
		self.s = GoodServer(("", port), Client)
		Client.server = self
		
		print "Running server on port " + str(port)
		print "Press CTRL+C to stop server"
		
	def run(self):
		self.s.serve_forever()
	
	def connect(self, client):
		if len(self.clients) >= 2: return False
		
		self.clients.append(client)
		return True
	
	def disconnect(self, client):
		try:
			self.clients.remove(client)
		except ValueError: pass
		
	def shutdown(self):
		print "Shutting down server..."
		self.s.shutdown()

#Stolen from https://gist.github.com/pklaus/c4c37152e261a9e9331f god bless			
class GoodServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	# Ctrl-C will cleanly kill all spawned threads
	daemon_threads = True
	# much faster rebinding
	allow_reuse_address = True
	 
	def __init__(self, server_address, RequestHandlerClass):
		SocketServer.TCPServer.__init__(self, server_address, RequestHandlerClass) 