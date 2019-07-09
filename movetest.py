# Echo client program
import socket
#import time #this just delays the robot, maybe not the best idea
HOST = "172.22.22.2" # The remote host (arm IP address)
PORT = 30002 # The same port as used by the server


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print "Sending robot pose!!"

s.send ("movej(p[-0.2, -0.53, 0.43, 0.36, -0.45, -0.42], a=1.0, v=0.1)" + "\n")

time.sleep(5)

data = s.recv(1024)

s.close()

'''
print "Starting MOVEMENT(!) Program"

count = 0
while (count < 1):
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.connect((HOST, PORT))
 time.sleep(0.5)

print "Set output 1 and 2 high"

s.send ("set_digital_out(1,True)" + "\n")
 time.sleep(0.1)
 
 s.send ("set_digital_out(2,True)" + "\n")
 time.sleep(2)

print "Robot starts Moving to 3 positions based on joint positions"

s.send ("movej([-1.95, -1.58, 1.16, -1.15, -1.55, 1.18], a=1.0, v=0.1)" + "\n")
 time.sleep(10)

s.send ("movej([-1.95, -1.66, 1.71, -1.62, -1.56, 1.19], a=1.0, v=0.1)" + "\n")
 time.sleep(10)

s.send ("movej([-1.96, -1.53, 2.08, -2.12, -1.56, 1.19], a=1.0, v=0.1)" + "\n")
 time.sleep(10)

print "Robot starts Moving to 3 positions based on pose positions"

s.send ("movej(p[0.00, 0.3, 0.4, 2.22, -2.22, 0.00], a=1.0, v=0.1)" + "\n")
 time.sleep(10)

s.send ("movej(p[0.00, 0.3, 0.3, 2.22, -2.22, 0.00], a=1.0, v=0.1)" + "\n")
 time.sleep(10)

s.send ("movej(p[0.00, 0.3, 0.2, 2.22, -2.22, 0.00], a=1.0, v=0.1)" + "\n")
 time.sleep(10)

print "Set output 1 and 2 low"

s.send ("set_digital_out(1,False)" + "\n")

time.sleep(0.1)
 
 s.send ("set_digital_out(2,False)" + "\n")
 time.sleep(0.1)

count = count + 1
 print "The count is:", count

print "Program finish"

time.sleep(1)
 data = s.recv(1024)

s.close()
 print ("Received", repr(data))

print "Status data received from robot"
'''



