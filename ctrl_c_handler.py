# ctrl-c handler

from signal import signal, SIGINT
from sys import exit

def handler(signal_received, frame):
	exit(0)

if __name__ == '__main__':
	signal(SIGINT, handler)

	counter = 1

	while counter == 1 :
		print "hello"


