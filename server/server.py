import SocketServer

class Server(SocketServer.BaseRequestHandler):
	clients = 0
	
	def setup(self):
		print "Received connection from " + self.client_address[0] + ":" + str(self.client_address[1])
		self.lost = False
		self.shutdown = False
		
		if Server.clients > 1:
			print "Server is full!"
			self.request.send("Server is full!")
			self.request.close()
			self.shutdown = True
		else:
			Server.clients += 1
	
	def handle(self):
		while(not self.shutdown):
			l = self.request.recv(512)
			if not l:
				self.lost = True
				break
			elif l.strip() == "QUIT": break
			self.request.send(l)
	
	def finish(self):
		if self.lost:
			print "Lost connection from " + self.client_address[0] + ":" + str(self.client_address[1])
			Server.clients -= 1
		else:
			if not self.shutdown:
				self.request.send("y... you too\r\n")
				Server.clients -= 1
			print "Closed connection from " + self.client_address[0] + ":" + str(self.client_address[1])

#Stolen from https://gist.github.com/pklaus/c4c37152e261a9e9331f god bless			
class GoodServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	# Ctrl-C will cleanly kill all spawned threads
	daemon_threads = True
	# much faster rebinding
	allow_reuse_address = True
	 
	def __init__(self, server_address, RequestHandlerClass):
		SocketServer.TCPServer.__init__(self, server_address, RequestHandlerClass) 