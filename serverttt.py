from server.server import Server
PORT = 10101

if __name__ == "__main__":
	s = Server(PORT)
	try:
		s.run()
	except KeyboardInterrupt:
		s.shutdown()
	