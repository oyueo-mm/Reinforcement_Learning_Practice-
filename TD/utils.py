import numpy as np
import time
import pygame

def get_q(state, q_table):
	if state not in q_table:
		q_table[state] = np.zeros(4)
	return q_table[state]

def show_best(env, q_table, screen, delay = 0.5, episode = 0):
	state = env.reset()
	total_reward = 0
	env.render(screen)
	time.sleep(delay)
	for step in range(100):
		q_values = get_q(state, q_table)
		action = np.argmax(q_values)
		next_state, reward, done = env.step(action)
		state = next_state
		total_reward += reward

		env.render(screen)
		
		if done:
			break
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
		if episode > 0:
			print(f"\r[episode {episode}] step: {step}, state: {state}, action : {action}, reward: {reward}, Q : {q_values}", end=" ", flush=True)
		else:
			print(f"\rstep: {step}, state: {state}, action : {action}, reward: {reward}, Q : {q_values}", end=" ", flush=True)
		time.sleep(delay)

def show_direction(env, q_table):
	arrow = ["↑", "↓", "←", "→"]
	for y in range(7):
		for x in range(7):
			if [x, y] in env.bombs:
				print("■", end=" ")
			elif [x, y] == env.goal:
				print("G", end=" ")
			else:
				q_values = get_q((x, y), q_table)
				action = np.argmax(q_values)
				print(arrow[action], end=" ")
		print()