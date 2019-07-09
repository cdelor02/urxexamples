# Echo client program
import socket
import time 
HOST = "172.22.22.2" # The remote host (arm IP address)
PORT = 30002 # The same port as used by the server

#HOST = "128.30.99.2"

#Establish socket connection
try:
  sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
  sock.settimeout(5)
  sock.connect((HOST,PORT))
except:
  print("Socket connect failed!")
  exit()
#send script to robot
#sock.sendall(cmd)

#wait for a few seconds and close socket
time.sleep(3)
if(sock):
  sock.close()
sock=None

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((HOST, PORT))
#time.sleep(1)
#s.send ("set_digital_out(2,False)" + "\n")
#data = s.recv(1024)
#s.close()
#print ("Received", repr(data))



