import pygame ,sys
pygame.init()

screen = pygame.display.set_mode([640,480])

screen.fill([255,255,255])
my_ball = pygame.image.load("beach_ball.png")  #从硬盘加载一个图像
x=50
y=50
screen.blit(my_ball,[x,y])  #把my_ball表面复制到screen表面上.
pygame.display.flip()  #通过display.flip()调用使它可见.
for looper in range(1,100):
    pygame.time.delay(20)
    pygame.draw.rect(screen,[255,255,255],[x,y,90,90])
    x=x+5
    screen.blit(my_ball,[x,y])
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()