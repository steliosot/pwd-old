# Stelios
import random as rand
from math import e
def printBestCandidate(candidate,n):
	sample_size = int(round(n/e,0))
	print("Sample size is: ", sample_size)
	best = 0
	for i in range(sample_size):
	 	if candidate[i]>candidate[best]:
	 		best = i

	for i in range(sample_size,n):
	 	if candidate[i] >= candidate[best]:
	 		best = i
	 		break

	if best >= sample_size:
	 	print("Best candidate found is ", best+1, " with talent ", candidate[best])
	else:
	 	print("Could not find a best candidate")

n=8
candidate=[]
for i in range(n):
	candidate.append(1+rand.randint(1,8) % 8)

print("Candidates: ", [i for i in range(9)])
print("Talents: ", [i for i in candidate])
printBestCandidate(candidate,n)