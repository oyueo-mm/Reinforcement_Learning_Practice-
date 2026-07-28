import random
from Env import GridWorld
from utils import *
import pygame

WIDTH = 700
HEIGHT = 700
CELL_SIZE = 100

env = GridWorld(WIDTH, HEIGHT, CELL_SIZE)

# 0, 1, 2, 3 : 상, 하, 좌, 우
actions = [0, 1, 2, 3]

# Q-table
q_table = {}

episodes = 2000
learning_rate = 0.1
discount_factor = 0.9
epsilon = 1.0
epsilon_decay = 0.995
epsilon_min = 0.01

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("강화학습")

for episode in range(episodes):
	state = env.reset()
	total_reward = 0
	done = False
	for step in range(1000):
		q_values = get_q(state, q_table)
		if random.random() < epsilon:
			action = random.choice(actions)
		else:
			action = np.argmax(q_values)
		next_state, reward, done = env.step(action)
		next_q = get_q(next_state, q_table)
		q_values[action] += learning_rate * (reward + discount_factor * np.max(next_q) - q_values[action])
		state = next_state
		total_reward += reward
		if done:
			break
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
		env.render(screen)
	epsilon = max(epsilon * epsilon_decay, epsilon_min)
	if episode % 400 == 0 and episode != 0:
		print()
		show_best(env, q_table, screen, 0.05, episode)

show_best(env, q_table, screen, 0.5)
print()
show_direction(env, q_table)

pygame.quit()