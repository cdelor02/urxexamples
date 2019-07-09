# purpose: closes gripper, moves to 4 points, opens gripper

import time 
import urx
import logging
import sys
from urx.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper


if __name__ == "__main__":
    rob = urx.Robot("172.22.22.2")

    robotiqgrip = Robotiq_Two_Finger_Gripper(rob, 1.2)

    robotiqgrip.close_gripper()
    time.sleep(1)

    try:
        l = 0.1
        v = 0.03
        a = 0.1
        r = 0.05
        pose = rob.getl()
        print pose
        pose[2] += l
        print "goal pose:"
        print pose
        rob.movep(pose, acc=a, vel=v, wait=False)
        while True:
            p = rob.getl(wait=True)
            if p[2] > pose[2] - 0.05:
                break
		
	print "sleeping for 2 seconds"
	time.sleep(2)
		
		
        pose[1] += l 
        print "goal pose:"
        print pose
        rob.movep(pose, acc=a, vel=v, wait=False)
        while True:
            p = rob.getl(wait=True)
            if p[1] > pose[1] - 0.05:
                break
		
	print "sleeping for 2 seconds"
	time.sleep(2)
        
        pose[2] -= l
        print "goal pose:"
        print pose
        rob.movep(pose, acc=a, vel=v, wait=False)
        while True:
            p = rob.getl(wait=True)
            if p[2] < pose[2] + 0.05:
                break
		
	print "sleeping for 2 seconds"        
	time.sleep(2)
		
		
        pose[1] -= l
        print "goal pose:"
        print pose
        rob.movep(pose, acc=a, vel=v, wait=False)

	

    finally:
        robotiqgrip.open_gripper()
        time.sleep(1)
        rob.close()


