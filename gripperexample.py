import sys
import urx
import logging
import time
from urx.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper

'''if __name__ == '__main__':
	rob = urx.Robot("172.22.22.2")
	robotiqgrip = Robotiq_Two_Finger_Gripper()

	if(len(sys.argv) != 2):
		print "false"
		sys.exit()

	if(sys.argv[1] == "close") :
		robotiqgrip.close_gripper()
	if(sys.argv[1] == "open") :
		robotiqgrip.open_gripper()

	rob.send_program(robotiqgrip.ret_program_to_run())

	rob.close()
	print "true"
	sys.exit()
'''

#THIS WORKS!!
'''
rob = urx.Robot("172.22.22.2")
robotiqgrip = Robotiq_Two_Finger_Gripper(rob, 1.25)
#what this thing takes: self, robot, payload, speed, ...
logging.basicConfig()

if(len(sys.argv) != 2):
	print "faLse"
	sys.exit()

if(sys.argv[1] == "close") :
	robotiqgrip.close_gripper()
if(sys.argv[1] == "open") :
	robotiqgrip.open_gripper()

rob.send_program(robotiqgrip.ret_program_to_run())
rob.close()
sys.exit() 
'''

rob = urx.Robot("172.22.22.2")
robotiqgrip = Robotiq_Two_Finger_Gripper(rob, 1.25)

robotiqgrip.close_gripper()
time.sleep(3)
robotiqgrip.open_gripper()

rob.send_program(robotiqgrip.ret_program_to_run())
rob.close()
sys.exit()


