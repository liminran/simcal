import pygame
import math

# 初始化 pygame
pygame.init()

# 设置窗口
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("画爱心")

# 定义颜色
RED = (255, 0, 0)

# 爱心图形函数
def draw_heart(surface, x, y, size):
    # 使用 parametric 方程画出爱心
    points = []
    for t in range(0, 360, 1):
        # 转换角度为弧度
        t_rad = math.radians(t)
        # 爱心的 parametric 方程
        heart_x = size * 16 * math.sin(t_rad) ** 3
        heart_y = size * (13 * math.cos(t_rad) - 5 * math.cos(2 * t_rad) - 2 * math.cos(3 * t_rad) - math.cos(4 * t_rad))
        # 将坐标平移到中心位置 (x, y)
        points.append((x + heart_x, y - heart_y))

    # 画出爱心形状
    pygame.draw.polygon(surface, RED, points)

# 主程序
def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill((255, 255, 255))  # 白色背景
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 画爱心，位置在 (400, 300)，大小为 15
        draw_heart(screen, 400, 300, 15)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
