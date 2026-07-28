import random
import pygame
from Env import GridWorld
from utils import *
import time

env = GridWorld(700, 700, 100)

Q = {}

for x in range(7):
	for y in range(7):
		Q[(x, y)] = [0.0, 0.0, 0.0, 0.0]
# print(Q)
# print(len(Q))

gamma = 0.99
learning_rate = 0.1
epsilon = 1.0
epsilon_decay = 0.995
epsilon_min = 0.01

episodes = 3000
max_steps = 500

pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Monte Carlo Grid World")

goal_count = 0
for episode in range(episodes):
	state = env.reset()
	trajectory = []
	done = False
	while (not done) and (len(trajectory) < max_steps):
		action = choose_action(state, epsilon, Q)
		next_state, reward, done = env.step(action)
		trajectory.append((state, action, reward))
		state = next_state
		if reward == 100:
			goal_count += 1
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
		env.render(screen)
	G = 0
	for state, action, reward in reversed(trajectory):
		G = reward + gamma * G
		Q[state][action] += learning_rate * (G - Q[state][action])
	if episode % 500 == 0 and episode > 0:
		# print(goal_count)
		show_best(screen, env, Q, delay=0.15, episode=episode)
	epsilon = max(epsilon_min, epsilon * epsilon_decay)

print(goal_count)
show_best(screen, env, Q, delay=0.5)
"""
for i in range(7):
	for j in range(7):
		print(Q[(i, j)], end = " | ")
	print()
"""

show_direction(env, Q)