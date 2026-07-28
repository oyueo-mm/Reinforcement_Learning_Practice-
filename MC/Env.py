import pygame
import random

class GridWorld:
	def __init__(self, WIDTH=700, HEIGHT=700, CELL_SIZE=100):
		self.WIDTH = WIDTH
		self.HEIGHT = HEIGHT
		self.CELL_SIZE = CELL_SIZE
		self.WHITE = (255, 255, 255)
		self.BLACK = (0, 0, 0)
		self.RED = (255, 0, 0)
		self.GREEN = (0, 255, 0)
		self.BLUE = (0, 0, 255)
		
		self.agent = [0, 0]
		self.goal = [6, 6]
		self.bombs = [[3, 3], [3, 4], [3, 5], [2, 3], [1, 3], [5, 5], [4, 5], [1, 6], [1, 4], [3, 0], [3, 1], [5, 2]]

	def reset(self):
		self.agent = [0, 0]
		return tuple(self.agent)

	def step(self, action):
		reward = -0.1
		done = False
		# 0, 1, 2, 3 : 상, 하, 좌, 우

		if action == 0:
			self.agent[1] -= 1
		elif action == 1:
			self.agent[1] += 1
		elif action == 2:
			self.agent[0] -= 1
		elif action == 3:
			self.agent[0] += 1

		if (self.agent[0] < 0) or (self.agent[0] >= (self.WIDTH // self.CELL_SIZE)) or (self.agent[1] < 0) or (self.agent[1] >= (self.HEIGHT // self.CELL_SIZE)):
			reward = -1
			self.agent[0] = max(0, min(self.agent[0], (self.WIDTH // self.CELL_SIZE) - 1))
			self.agent[1] = max(0, min(self.agent[1], (self.HEIGHT // self.CELL_SIZE) - 1))

		# 목표
		if self.agent == self.goal:
			reward = 100
			done = True
		# 폭탄
		if self.agent in self.bombs:
			reward = -100
			# done = True
		return tuple(self.agent), reward, done

	def render(self, screen):
		screen.fill(self.WHITE)
		for x in range(0, self.WIDTH, self.CELL_SIZE):
			pygame.draw.line(screen, self.BLACK, (x, 0), (x, self.HEIGHT))
		for y in range(0, self.HEIGHT, self.CELL_SIZE):
			pygame.draw.line(screen, self.BLACK, (0, y), (self.WIDTH, y))

		pygame.draw.rect(screen, self.GREEN, (self.goal[0] * self.CELL_SIZE, self.goal[1] * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))
		pygame.draw.rect(screen, self.RED, (self.agent[0] * self.CELL_SIZE, self.agent[1] * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))
		for bomb in self.bombs:
			pygame.draw.rect(screen, self.BLACK, (bomb[0] * self.CELL_SIZE, bomb[1] * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))

		pygame.display.update()

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((700, 700))

    env = GridWorld(700, 700, 100)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        env.render(screen)

    pygame.quit()