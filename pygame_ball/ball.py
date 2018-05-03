import pygame ,sys
pygame.init()

screen = pygame.display.set_mode([640,480])

screen.fill([255,255,255])
my_ball = pygame.image.load("beach_ball.png")  #从硬盘加载一个图像
screen.blit(my_ball,[50,50])  #把my_ball表面复制到screen表面上.
pygame.display.flip()  #通过display.flip()调用使它可见.
pygame.time.delay(2000)#延迟2000毫秒
screen.blit(my_ball,[150,50])  #把my_ball表面复制到screen表面上.
pygame.draw.rect(screen,[255,255,255],[50,50,90,90],0)

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()