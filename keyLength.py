import sys

if __name__=='__main__':
	
	rep_seq = []
	rep_seq_spaces = []
	tallys = [0]*20

	if len(sys.argv) != 2:
		print("Usage: python3 keyLength.py filename")
		exit(0)
	else:

		try:
			with open(sys.argv[1]) as fh:
				lines = fh.readlines()
		except:
			print("No file named '" + sys.argv[1] + "'")
			exit(0)

		for line in lines:
			line.replace(" ", "")
			line.replace("\n", "")
			for length in range(3,5+1):
				for i in range(len(line)-length+1):
					q = line[i:i+length]
					for j in range(i+1,len(line)-length+1):
						r = line[j:j+length]
						if q == r:
							rep_seq.append(q)
							rep_seq_spaces.append(j-i)

		for n in rep_seq_spaces:
			for i in range(1,20):
				if n % i == 0:
					tallys[i] = tallys[i] + 1

		s = sum(tallys)
		if s == 0:
			print("No repeating sequences")
		else :
			print("Chance key length is: ")
			for i in range(1,len(tallys)):
				print(str(i) + " = " + str(round((tallys[i]/s)* 100,2)) + "%")
