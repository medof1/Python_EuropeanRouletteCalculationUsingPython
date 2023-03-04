import random

print("\nDEFAULT VALUE:")
print("Max Martingale = 13")
print("Sample= 3000")
print("Batch= 1000 \n")
print("Write 0 if u want to use default value \n")

maxMartingale = int(input('Max Martingale: '))
startingSample = int(input('How many sample: '))
startingBatch = int(input('How many batch: '))

martingale = 1
maxSample = startingSample
batch,sample,number = 1,0,0
number = random.randint(0,1)
prevNumber = number
status = ""
losedoll = 0
lose = 0

if startingSample == 0:
	maxSample = 3000
if startingBatch == 0:
	startingBatch = 1000
if maxMartingale == 0:
	maxMartingale = 13

def printing():
	global status, martingale, sample, batch, number
	if number == 0:
		stat = "ZERO"
	elif number >= 1 and number <= 18:
		stat = "LOW"
	else:
		stat = "HIGH"
	print(str(batch), str(sample) + ', ' + str(stat) + ', Bets no. ' + str(int(martingale)) , status)

def baccarat():
	global maxSample, startingSample, startingBatch, batch, sample, number, prevNumber, martingale, status
	if batch <= startingBatch:
		if sample < maxSample:
			number = random.randint(0,36)
			if prevNumber >= 1 and prevNumber <= 18:
				if number >= 19 and number <= 36 or number == 0:
					status = "LOSE"
				elif number >= 1 and number <= 18:
					status = "WIN"
			elif prevNumber >= 19 and prevNumber <= 36:
				if number >= 0 and number <= 18:
					status = "LOSE"
				elif number >= 19 and number <= 36:
					status = "WIN"
			else:
				status = "NO BETS"
			if status == "NO BETS":
				pass
			else:
				sample += 1
			printing()
			prevNumber = number
			if status == "LOSE":
				martingale += 1
			elif status == "WIN":
				martingale = 1
		else:
			sample = 0
			batch += 1

while(1):
	if batch <= startingBatch:
		baccarat()
		if martingale > maxMartingale:
			lose += 1
			martingale = 1
			sample = 0
			batch += 1
	else:
		winrate = ((batch - lose)/batch)*100
		print("LOSEDOLL = ", lose, "WINRATE = ", winrate, "%")
		break