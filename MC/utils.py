import random
import pygame

def greedy_action(state, Q):
	values = Q[state]
	max_value = max(values)
	candidates = []
	for i, value in enumerate(values):
		if value == max_value:
			candidates.append(i)
	return random.choice(candidates)

def choose_action(state, epsilon, Q):
	if random.random() < epsilon:
		return random.randint(0, 3)
	return greedy_action(state, Q)

def show_best(screen, env, Q, delay=0.5, episode=0):
    state = env.reset()
    total_reward = 0
    done = False
    step = 0
    max_steps = 500
    while not done and step < max_steps:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        step += 1
        env.render(screen)
        action = choose_action(state, 0, Q)
        state, reward, done = env.step(action)
        total_reward += reward
        if episode != 0:
            print(f"[episode {episode}] step: {step}, state: {state}, action : {action}, reward: {reward}, Q: {Q[state]}")
        else:
            print(f"step: {step}, state: {state}, action : {action}, reward: {reward}, Q: {Q[state]}")
        pygame.time.delay(int(delay * 1000))
    print("===================================================")

def show_direction(env, Q):
    arrow = ["↑", "↓", "←", "→"]
    for y in range(7):
        for x in range(7):
            if [x, y] in env.bombs:
                print("■", end=" ")
            elif [x, y] == env.goal:
                print("G", end=" ")
            else:
                action = choose_action((x, y), 0, Q)
                print(arrow[action], end=" ")
        print()