import socket
import threading

#Class PortScanner
class Ps():
	def __checkPort(self, ip, port):
		try:
			sock = socket.socket()
			sock.settimeout(0.2)
			sock.connect((ip, port))
			#If connection passed without errors, append port to array
			self.openPorts.append(port)
		except:
			pass

	def getOpenPorts(self, ip, portRange):
		self.openPorts = []

		for i in range(portRange[0], portRange[1]):
			threading.Thread(target=self.__checkPort, args=(ip, i)).start()

		while 1:
			#If all threads have completed their task, return opened ports
			if threading.active_count() <= 1:
				return self.openPorts