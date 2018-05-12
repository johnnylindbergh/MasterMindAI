#!/usr/bin/python
import random
import math

def genPrimes(n):
	#x= 0
	n = n-1
	count = 2
	primes = []
	while True:
		isprime = True
		
		for x in range(2, int(math.sqrt(count) + 1)):
			if count % x == 0: 
				isprime = False
				break
		
		if isprime:
			primes.append(count)
			#print "len:", len(primes)
			if (len(primes) > n):
				
				return primes
		count += 1
	
class Game:
	def  __init__(self, attempts, cols, colors):
		self.cols = cols
		self.numColors = colors;
		self.numAttempts = attempts;
		self.attemptCount = 0;
		self.colors = [i for i in range(1, colors+1)]
		self.primeColors = genPrimes(colors)
		self.guesses = [[0 for i in xrange(cols)] for i  in xrange(attempts)]
		self.results  =  [[0,0] for i  in xrange(attempts)]
		self.sequence =  [random.randint(1, colors)  for  i  in xrange(cols)];
	def display(self):
		for guess in range(self.numAttempts):
			for color in range(self.cols):
				print "|",
				print self.guesses[guess][color],
				print "|",
			
			print self.results[guess],
			print "\n"
	def play(self, seq):
		self.guesses[self.attemptCount] = seq
		results = self.getResults(seq)
		self.results[self.attemptCount] = results
		self.attemptCount+=1
	def testResults(self, seq1, seq2):
			results = [0,0]
			checked = []
			for color in range(self.cols):
				if seq1[color] == seq2[color]:
					results[0]+=1
				else :
					if seq2[color] in seq1 and seq2[color] not in checked:
						results[1]+=1
						checked.append(seq2[color])
			return results

		
	def getResults(self, seq):
		results = [0,0]
		for color in range(self.cols):
			if seq[color] == self.sequence[color]:
				results[0]+=1
			else :
				if self.sequence[color] in seq :
					results[1]+=1
		return results
		
class AI:
	def __init__(self, game):
		self.game = game
		self.possible = []
	def getPossibleSeq(self):
		for a in self.game.colors:
			for b in self.game.colors:
				for c in self.game.colors:
					for d in self.game.colors:
						self.possible.append([a,b,c,d])
	def elimination(self, seq, results):
#		product = 1
#		for color in seq:
#			product *= self.game.primeColors[color-1]
#		if (results[0] + results[1]) == self.game.cols:
#			possible = []
#			for sequence in self.possible:
#				productTest = 11

#				for color in sequence:
#					productTest *= self.game.primeColors[color-1]
#				if productTest == product:
#					possible.append(sequence)
#			self.possible = possible
#		if (results[0] == 1):
#			possible = []
#			for sequence in self.possible:
#				for color in seq:
#					if color in sequence:
#						possible.append(sequence)
#						break
#			self.possible = possible
#		if (results[0] + results[1]) == 0:
#			possible = []
#			for sequence in self.possible:
#				notInSeq = True
#				for color in sequence:
#					if color in seq:
#						notInSeq = False
#				if notInSeq:
#					possible.append(sequence)
#			self.possible = possible
#						
		possible = []
		for sequence in self.possible:
			if self.game.testResults(seq, sequence) == results:
				possible.append(sequence)
		self.possible = possible				
 
			
		
		
			
			
			
	 
				
def main():
	x = Game(10,4,6)	
	ai = AI(x)
	ai.getPossibleSeq()

	while len(ai.possible) > 0 :
		#print ai.possible
		
		play = ai.possible[random.randint(0,len(ai.possible)-1)]
		print play
		res = []	
		results = input("black:")
	
		res.append(int(results))
		results = input("white:")
		res.append(int(results))
		ai.elimination(play, res)

def userPlay():
	x = Game(10, 4, 6);
	ai = AI(x)
	ai.getPossibleSeq()
	
	while x.attemptCount < x.numAttempts:
		p = input("sequence:")
		seq = []
		for char in str(p):
			seq.append(int(char))	
				
		x.play(seq)
		
		x.display();
	print x.sequence

main()
	
	
		