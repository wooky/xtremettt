import socket
from server.server import Server
PORT = 10101

if __name__ == "__main__":
	s = None
	try:
		s = Server(PORT)
		print "Press CTRL+C to stop server"
		s.run()
	except socket.error:
		print "A server is already running on port " + str(PORT) + ". Try changing the port number"
	except KeyboardInterrupt:
		s.shutdown()
	