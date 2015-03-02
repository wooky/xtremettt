import json

class Query:
	AUTH = "auth"
	FULL = "full"
	STRIP = "strip"
	
	NAME = "name"
	TYPE = "type"
	PIC = "pic"
	
	DISCONNECT = "bye"

	def __init__(self, request, address, kwargs):
		self.request = request
		self.address = address
		self.commands = {}
		self.append(kwargs)
	
	def append(self, kwargs):
		self.commands.update(kwargs)
	
	def send(self):
		self.request.send(json.dumps(self.commands))
	
	def recv(self):
		try:
			self.commands = json.loads(self.request.recv(50000))
			return True
		except ValueError:
			print "[ERROR] An invalid response was received from " + self.address[0] + ":" + str(self.address[1])
			return False
	
	def send_with_response(self):
		self.send()
		return self.recv()
	
	def get(self, key):
		return self.commands.get(key)