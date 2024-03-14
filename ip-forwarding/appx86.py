import socket
import threading
import argparse
import logging

format = '%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO, format=format)

class app():

	def handle(self, buffer, direction, src_address, src_port, dst_address, dst_port):
		if direction:
			logging.debug(""+str(src_address)+":"+str(src_port)+" -> "+str(dst_address)+":"+str(dst_port)+" "+str(len(buffer))+" bytes")
		else:
			logging.debug(""+str(src_address)+":"+str(src_port)+" -> "+str(dst_address)+":"+str(dst_port)+" "+str(len(buffer))+" bytes")
		return buffer

	def transfer(self, src, dst, direction):
		src_address, src_port = src.getsockname()
		dst_address, dst_port = dst.getsockname()
		while True:
			try:
				buffer = src.recv(4096)
				if len(buffer) == 0:
					break
				dst.send(app().handle(buffer, direction, src_address, src_port, dst_address, dst_port))
			except Exception as e:
				logging.error(repr(e))
				break
		logging.warning("Closing connect "+str(src_address)+":"+str(src_port)+"! ")
		src.close()
		logging.warning("Closing connect "+str(dst_address)+":"+str(dst_port)+"! ")
		dst.close()

	def server(self, local_host, local_port, remote_host, remote_port):
		server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		server_socket.bind((local_host, local_port))
		server_socket.listen(0x40)
		logging.info("Server started "+str(local_host)+":"+str(local_port)+"")
		logging.info("Connect to "+str(local_host)+":"+str(local_port)+" to get the content of "+str(remote_host)+":"+str(remote_port)+"")
		while True:
			src_socket, src_address = server_socket.accept()
			logging.info("[Establishing] "+str(src_address)+" -> "+str(local_host)+":"+str(local_port)+" -> ? -> "+str(remote_host)+":"+str(remote_port)+"")
			try:
				dst_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				dst_socket.connect((remote_host, remote_port))
				logging.info("[OK] "+str(src_address)+" -> "+str(local_host)+":"+str(local_port)+" -> "+str(dst_socket.getsockname())+" -> "+str(remote_host)+":"+str(remote_port)+"")
				s = threading.Thread(target=app().transfer, args=(dst_socket, src_socket, False))
				r = threading.Thread(target=app().transfer, args=(src_socket, dst_socket, True))
				s.start()
				r.start()
			except Exception as e:
				logging.error(repr(e))
		        # logger = logging.getLogger('urbanGUI')


	def main(self):
		parser = argparse.ArgumentParser()
		parser.add_argument("--listen-host", help="the host to listen", required=True)
		parser.add_argument("--listen-port", type=int, help="the port to bind", required=True)
		parser.add_argument("--connect-host", help="the target host to connect", required=True)
		parser.add_argument("--connect-port", type=int, help="the target port to connect", required=True)
		args = parser.parse_args()
		app().server(args.listen_host, args.listen_port, args.connect_host, args.connect_port)
		# print("TETS")

app().main()