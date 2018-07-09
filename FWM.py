#!/usr/bin/python
#import numpy as np

def FWM(array):
	array_ = array
	median = 0
	total = sum(array_)
	if total % 2 == 0: #even median = total/2 + total/2 + 1
		index = 1
		while True:
			if sum(array_[0:index]) == int(total/2):
				median = index + 0.5
				return median
				break
			elif sum(array_[0:index]) == int(total/2) + 1:
				median = index - 0.5
				return median
				break
			elif sum(array_[0:index]) > int(total/2) + 1:
				median = index
				return median
				break
			else:
				index += 1
				
	else: #odd num median = total/2 + 1
		index = 1
		while True:
			if sum(array_[0:index]) >= int(total/2) + 1:
				median = index
				return median
				break
			else:
				index += 1
				
if __name__ == "__main__":
	#a = np.array((0,2,3,4,5,4,3,2,0))
	#b = np.array((0,2,3,4,4,3,2,0))
	a = (0,2,3,4,5,4,3,2,0)
	b = (0,2,3,4,4,3,2,0)
	print ("%f" % FWM(a))
	print ("%f" % FWM(b))
