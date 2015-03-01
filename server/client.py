import SocketServer
from query import Query

class Client(SocketServer.BaseRequestHandler):
	server = None
	
	def setup(self):
		print "Received connection from " + self.client_address[0] + ":" + str(self.client_address[1])
		self.lost = False
		self.shutdown = False
		
		if not Client.server.connect(self):
			print "Kicking " + self.client_address[0] + ":" + str(self.client_address[1]) + " due to full server"
			Query(self.request, None, {Query.FULL: True}).send()
			self.shutdown = True
	
	def handle(self):
		if self.shutdown: return
		
		q = Query(self.request, self.client_address, {Query.AUTH: True})
		if not q.send_with_response() or not q.get(Query.NAME) or not q.get(Query.TYPE):
			self.request.send("Invalid Protocol!\r\n")
			self.shutdown = True
			return
		else:
			self.name = q.get(Query.NAME)
			self.type = q.get(Query.TYPE)
			self.pic = q.get(Query.PIC)
		
		Query(self.request, None, {Query.STRIP: "Hello, " + self.name + " of type " + self.type + "!"}).send()
		"""while(not self.shutdown):
			l = self.request.recv(512)
			if not l:
				self.lost = True
				break
			elif l.strip() == "QUIT": break
			self.request.send(l)"""
	
	def finish(self):
		if self.lost:
			print "Lost connection from " + self.client_address[0] + ":" + str(self.client_address[1])
		else:
			if not self.shutdown:
				Query(self.request, None, {Query.DISCONNECT: True}).send()
			print "Closed connection from " + self.client_address[0] + ":" + str(self.client_address[1])
		Client.server.disconnect(self)