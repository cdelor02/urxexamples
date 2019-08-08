# keycontrol.py
# Charlie DeLorey
# 08/01/2019
# purpose: control arm with keyboard keys
# **program takes the current gripper state ("open" or "close") as commandline argument**
# Currently no support for end effector orientation (rx, ry, rz)

"""
               KEY MAPPING

  Open gripper:           Close gripper:
    |  |                        ||
   /    \                      /  \
   |    |                      |  |
      h                         g


In the horizontal plane:
    
     / \
      w
 < a     d >
      s
     \ /


In the vertical plane:
    
     / \
      i
 < j     l >
      k
     \ /


"""
import time 
import urx
import logging
import sys
import math
from urx.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper
from signal import signal, SIGINT
from sys import exit

def handler(signal_received, frame):
    exit(0)

#function for getting character input from keyboard
class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

getch = _Getch()


#function for calculating axis adjustment
def calc_dist(l):
    return (l / math.sqrt(2))


if __name__ == "__main__":
    rob = urx.Robot("172.22.22.2")

    signal(SIGINT, handler)

    robotiqgrip = Robotiq_Two_Finger_Gripper(rob, 1.2)

    gripstate = sys.argv[1]


    l = 0.05
    v = 0.03
    a = 0.1
    pose = rob.getl()
    counter = 1

    while counter == 1 :

	#THE COMMANDS MOVE THE END EFFECTOR RELATIVE TO THE VIEWER (i.e. "forward" means toward the viewer)

	inp = getch()
	if inp == "s":
		pose[0] += l
       		rob.movep(pose, acc=a, vel=v, wait=False) #forward x
	if inp == 'a':
		pose[1] += calc_dist(l) #change y
		pose[2] -= calc_dist(l) #change z; combined, they will move the ee correctly
        	rob.movep(pose, acc=a, vel=v, wait=False) #left
	if inp == "w":
		pose[0] -= l
		rob.movep(pose, acc=a, vel=v, wait=False) #back x
	if inp == 'd':
		pose[1] -= calc_dist(l)
		pose[2] += calc_dist(l)
        	rob.movep(pose, acc=a, vel=v, wait=False) #right
	if inp == 'i':
		pose[1] -= calc_dist(l)
		pose[2] -= calc_dist(l)
        	rob.movep(pose, acc=a, vel=v, wait=False)
	if inp == 'j':
		pose[1] += calc_dist(l)
		pose[2] -= calc_dist(l)
        	rob.movep(pose, acc=a, vel=v, wait=False)
	if inp == 'k':
		pose[1] += calc_dist(l)
		pose[2] += calc_dist(l)
        	rob.movep(pose, acc=a, vel=v, wait=False)
	if inp == 'l':
		pose[1] -= calc_dist(l)
		pose[2] += calc_dist(l)
        	rob.movep(pose, acc=a, vel=v, wait=False)	

	if inp == "h": #open gripper  (if not already open)
		if gripstate == "close":
			robotiqgrip.open_gripper()
			gripstate = "open"
	if inp == "g": #close gripper (if not already closed)
		if gripstate == "open":
			robotiqgrip.close_gripper()
			gripstate = "close"

	
    rob.close()


