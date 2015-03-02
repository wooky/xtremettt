import SocketServer, thread
from client import Client
from serverboard import ServerBoard

class Server:
	def __init__(self, port):
		self.clients = []
	
		self.s = GoodServer(("", port), Client)
		Client.server = self
		
		print "Running server on " + self.get_address()[0] + ":" + str(self.get_address()[1])
		
	def run(self):
		self.s.serve_forever()
	
	def get_address(self):
		return self.s.server_address
	
	def connect(self, client):
		if len(self.clients) >= 2: return False
		
		self.clients.append(client)
		if len(self.clients) == 2:
			for c in self.clients: c.play()
			thread.start_new_thread(ServerBoard, self.clients)
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
	#allow_reuse_address = True
	 
	def __init__(self, server_address, RequestHandlerClass):
		SocketServer.TCPServer.__init__(self, server_address, RequestHandlerClass) 