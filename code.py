import pygame
import random
import math

# 初始化 pygame
pygame.init()

# 设置窗口
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("烟花效果")

# 定义颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
COLORS = [RED, GREEN, BLUE, YELLOW]

# 烟花类
class Firework:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = random.choice(COLORS)
        self.particles = []

    def explode(self):
        num_particles = random.randint(50, 100)
        for _ in range(num_particles):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(2, 5)
            velocity = (math.cos(angle) * speed, math.sin(angle) * speed)
            particle = Particle(self.x, self.y, velocity, self.color)
            self.particles.append(particle)

    def draw(self, screen):
        for particle in self.particles:
            particle.move()
            particle.draw(screen)

    def is_finished(self):
        return len(self.particles) == 0

# 粒子类
class Particle:
    def __init__(self, x, y, velocity, color):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.color = color
        self.life = 255  # 粒子生命值（透明度）

    def move(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.velocity = (self.velocity[0] * 0.99, self.velocity[1] * 0.99)  # 阻力
        self.life -= 2  # 粒子逐渐消失

    def draw(self, screen):
        if self.life > 0:
            pygame.draw.circle(screen, self.color + (self.life,), (int(self.x), int(self.y)), 3)

# 主程序
def main():
    clock = pygame.time.Clock()
    fireworks = []

    running = True
    while running:
        screen.fill((0, 0, 0))  # 清屏
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 每隔一段时间发射烟花
        if random.random() < 0.02:
            firework = Firework(random.randint(50, width - 50), height)
            fireworks.append(firework)
            firework.explode()

        # 绘制和更新烟花
        for firework in fireworks:
            firework.draw(screen)
            if firework.is_finished():
                fireworks.remove(firework)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
