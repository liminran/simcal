import pygame
import os

# 初始化 pygame
pygame.init()

# 设置窗口
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("马奔跑动画")

# 定义颜色
WHITE = (255, 255, 255)

# 加载马的图片
def load_horse_images():
    horse_images = []
    for i in range(1, 5):  # 假设有 horse1.png, horse2.png, horse3.png, horse4.png
        image = pygame.image.load(f"horse{i}.png")
        horse_images.append(image)
    return horse_images

# 主程序
def main():
    clock = pygame.time.Clock()
    running = True
    horse_images = load_horse_images()
    horse_index = 0  # 当前显示的马的图片索引
    horse_x = 100  # 马的起始位置
    horse_y = height - 150  # 马的垂直位置（可以根据需要调整）

    while running:
        screen.fill(WHITE)  # 白色背景
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 切换马的图片来模拟奔跑
        screen.blit(horse_images[horse_index], (horse_x, horse_y))

        # 更新图片索引，循环播放
        horse_index = (horse_index + 1) % len(horse_images)

        # 更新马的水平位置，模拟奔跑
        horse_x += 5
        if horse_x > width:  # 如果马跑出屏幕，则重置回左边
            horse_x = -horse_images[0].get_width()

        pygame.display.update()
        clock.tick(15)  # 控制动画帧率

    pygame.quit()

if __name__ == "__main__":
    main()
