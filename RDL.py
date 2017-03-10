import numpy as np
from math import sin, cos
import sys
from keras.models import Sequential
from keras.layers import Dense, Flatten
from qlearning4k.games.game import Game
from qlearning4k import Agent
from keras.optimizers import *

class FlatLander(Game):
	def __init__(self):
		self.reset()
	def reset(self):
		import random
		self.x = random.randint(-100, 100)
		self.y = 100+random.randint(-10, 10)
		self.r = random.randint(0, 360)
		self.vx = random.randint(-100, 10) / 10
		self.vy = random.randint(-100, 100) / 10
		self.over = False
		self.won = False
		self.fuel = 100
	@property
	def name(self):
		return 'FlatLander'
	@property
	def nb_actions(self):
		return 3
	def play(self, action):
		global fout
		rs = 1
		self.fuel -= 1
		if action == 0:
			self.r = (self.r-rs) % 360
		if action == 2:
			self.r = (self.r+rs) % 360
		if action == 1:
			vx = cos(self.r)
			vy = sin(self.r)
			self.vx += vx
			self.vy += vy
		self.x += self.vx
		self.y += self.vy
		if self.y < 10:
			self.won = abs(self.vx)<10 and abs(self.y)<10
			if abs(self.vx)<10 and abs(self.y)<10:
				pass
				#print('Won. ', self.vx, self.vy, self.r)
			else:
				pass
				#print('Crashed')
			self.over = True
		if self.y > 1000:
			#print('Went too hight')
			self.over = True
			self.won = False
		if self.fuel<1:
			#print('Low on fuel')
			self.over = True
			self.won = False
	def get_state(self):
		return np.array([self.x, self.y, self.r, self.vx, self.vy])
	def is_over(self):
		return self.over
	def is_won(self):
		return self.won
	def get_score(self):
		if self.won:
			modifier = 1
		else:
			modifier = -1
		return modifier
		

things = 5
time = 10
out = 3

m = Sequential()
m.add(Flatten(input_shape = (time, things)))
m.add(Dense(100, activation='relu'))
m.add(Dense(out))

print(m.output_shape)
print(len(m.output_shape) != 2)
print(m.output_shape[1] != 3)

m.compile(sgd(lr=.001), "mse")
FL = FlatLander()
agent = Agent(model=m, memory_size=10, nb_frames=time)
agent.train(FL, batch_size=time, nb_epoch=1000, epsilon=.001)
agent.play(FL)
