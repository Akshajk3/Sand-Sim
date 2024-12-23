import pygame
import random


pygame.init()

WHITE = (255, 255, 255)

class SandSim:
    def __init__(self):
        self.width = 161
        self.height = 161
        self.prev_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.sand_size = 5
        self.running = True
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode(((800, 800)))
        pygame.display.set_caption("Sand Sim")
    
    def update_sand(self):
        self.prev_grid = [row[:] for row in self.grid]

        for i in range(self.width - 1):
            for j in range(self.height - 1):
                if self.prev_grid[i][j] == 1:
                    if j + 1 < self.height and self.prev_grid[i][j + 1] == 0:
                        self.grid[i][j] = 0
                        self.grid[i][j + 1] = 1
                    elif i - 1 >= 0 and j + 1 < self.height and self.prev_grid[i - 1][j + 1] == 0 and self.prev_grid[i + 1][j + 1] == 0:
                        direction = random.choice([True, False])
                        if direction:
                            self.grid[i][j] = 0
                            self.grid[i - 1][j + 1] = 1
                        else:
                            self.grid[i][j] = 0
                            self.grid[i + 1][j + 1] = 1
                    elif i - 1 >= 0 and j + 1 < self.height and self.prev_grid[i - 1][j + 1] == 0:
                        self.grid[i][j] = 0
                        self.grid[i - 1][j + 1] = 1
                    elif i + 1 < self.width and j + 1 < self.height and self.prev_grid[i + 1][j + 1] == 0:
                        self.grid[i][j] = 0
                        self.grid[i + 1][j + 1] = 1
    
    def poll_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.reset_grid()

        if pygame.mouse.get_pressed()[0]:
            x = int(pygame.mouse.get_pos()[0] / self.sand_size)
            y = int(pygame.mouse.get_pos()[1] / self.sand_size)
            self.place_sand(x, y)

        if pygame.mouse.get_pressed()[2]:
            x = int(pygame.mouse.get_pos()[0] / self.sand_size)
            y = int(pygame.mouse.get_pos()[1] / self.sand_size)
            self.remove_sand(x, y)
    
    def draw(self):
        for i in range(self.width - 1):
            for j in range(self.height - 1):
                if (self.grid[i][j] == 1):
                    rect = pygame.Rect(i * self.sand_size, j * self.sand_size, self.sand_size, self.sand_size)
                    pygame.draw.rect(self.display, WHITE, rect)
    
    def place_sand(self, x, y):
        self.grid[x][y] = 1

    def remove_sand(self, x, y):
        self.grid[x][y] = 0

    def reset_grid(self):
        self.prev_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
                
    def update(self):
        while self.running:
            self.display.fill((0, 0, 0))
            self.update_sand()
            self.poll_events()
            self.draw()

            fps = round(self.clock.get_fps())
            pygame.display.set_caption(f"Sand Sim - FPS: {fps}")

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    sim = SandSim()
    sim.update()