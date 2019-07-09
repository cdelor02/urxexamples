import time 
import urx
import logging

rob = urx.Robot("172.22.22.2")

l = 0.1
v = 0.1
a = 0.05
r = 0.05
pose = rob.getl()
print "Current pose: ", rob.getl()
#pose[2] -= l
#rob.movep(pose, acc=a, vel=v, wait=True)
#rob.movel((pose[0] - 0.1, pose[1] - 0.1, pose[2], pose[3], pose[4], pose[5]), a, v, relative=True)
print "New pose: ", rob.getl()
wait = False

rob.close()
