from server.server import *
PORT = 10101

if __name__ == "__main__":
	s = GoodServer(("", PORT), Server)
	print "Running server on port " + str(PORT)
	try:
		s.serve_forever()
	except KeyboardInterrupt:
		print "Shutting down server..."
		s.shutdown()
	