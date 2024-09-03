import time
import pygame
import math
import _pyinstaller_hooks_contrib
pygame.init()
running = True
GREY = (150, 156, 150)
WHITE = (255,255,255)
BLACK = (0,0,0)
RNAD = (123,2,23)
display = (500, 600)
total_sec = 0
total = 0
start = False
end = False
font = pygame.font.SysFont('sans',50)
text1 = font.render('+',True,BLACK)
text2 = font.render('-',True,BLACK)
text3 = font.render('start',True,BLACK)
text4 = font.render('reset',True,BLACK)
text5 = font.render('TIMEUP!',True,BLACK)
screen = pygame.display.set_mode(display)
def draws():
    pygame.draw.rect(screen, WHITE, (100, 50, 50, 50))
    pygame.draw.rect(screen, WHITE, (100, 200, 50, 50))
    pygame.draw.rect(screen, WHITE, (200, 50, 50, 50))
    pygame.draw.rect(screen, WHITE, (200, 200, 50, 50))
    pygame.draw.rect(screen, WHITE, (300, 50, 150, 50))
    pygame.draw.rect(screen, WHITE, (300, 200, 150, 50))

    screen.blit(text1, (113, 45))
    screen.blit(text1, (213, 45))
    screen.blit(text2, (117, 190))
    screen.blit(text2, (217, 190))
    screen.blit(text3, (334, 45))
    screen.blit(text4, (330, 195))
    pygame.draw.rect(screen, BLACK, (50, 520, 400, 50))
    pygame.draw.rect(screen, WHITE, (60, 530, 380, 30))

    pygame.draw.circle(screen, BLACK, (250, 400), 100)
    pygame.draw.circle(screen, WHITE, (250, 400), 95)
    pygame.draw.circle(screen, BLACK, (250, 400), 5)

    pygame.draw.line(screen, BLACK, (250, 400), (250, 310))
while running:
    screen.fill(GREY)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if end:
        screen.fill(WHITE)
        screen.blit(text5,(250,300))
        time.sleep(3)
        end = False
    else:
        draws()
    # pygame.draw.rect(screen,WHITE,(100,50,50,50))
    # pygame.draw.rect(screen, WHITE, (100, 200, 50, 50))
    # pygame.draw.rect(screen, WHITE, (200, 50, 50, 50))
    # pygame.draw.rect(screen, WHITE, (200, 200, 50, 50))
    # pygame.draw.rect(screen, WHITE, (300, 50, 150, 50))
    # pygame.draw.rect(screen, WHITE, (300, 200, 150, 50))
    #
    # screen.blit(text1,(113,45))
    # screen.blit(text1,(213,45))
    # screen.blit(text2,(117,190))
    # screen.blit(text2,(217,190))
    # screen.blit(text3,(334,45))
    # screen.blit(text4,(330,195))
    # pygame.draw.rect(screen, BLACK, (50, 520, 400, 50))
    # pygame.draw.rect(screen, WHITE, (60, 530, 380, 30))
    #
    # pygame.draw.circle(screen,BLACK,(250,400),100)
    # pygame.draw.circle(screen, WHITE, (250, 400), 95)
    # pygame.draw.circle(screen, BLACK, (250, 400), 5)
    #
    # pygame.draw.line(screen,BLACK,(250,400),(250,310))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 100 < mouse_x < 150 and 50 < mouse_y < 100:
                        total_sec += 60
                        print('+')
                    if 200 < mouse_x < 250 and 50 < mouse_y < 100:
                        total_sec += 1
                        print('+')
                    if 100 < mouse_x < 150 and 200 < mouse_y < 250:
                        total_sec -= 60
                        print('-')
                    if 200 < mouse_x < 250 and 200 < mouse_y < 250:
                        total_sec -= 1
                        print('-')
                    if 300 < mouse_x < 450 and 50 < mouse_y < 100:
                        total = total_sec
                        start = True
                        print('start')
                    if 300 < mouse_x < 450 and 200 < mouse_y < 250:
                        total_sec = 0
                        start = False
                        print('reset')
        if start:
            total_sec -= 1
            time.sleep(1)
            pygame.draw.rect(screen, RNAD, (60, 530, int(380 * (total_sec / total)), 30))
        mins = total_sec//60
        secs = total_sec % 60
        times = str(mins) + " : " + str(secs)
        texttime = font.render(times,True,BLACK)
        screen.blit(texttime,(120,120))
        x_sec = 250 + 90 * math.sin(6 * secs * math.pi / 180)
        y_sec = 400 - 90 * math.cos(6 * secs * math.pi / 180)
        pygame.draw.line(screen, BLACK, (250, 400), (int(x_sec), int(y_sec)))
        x_min = 250 + 40 * math.sin(6 * mins * math.pi / 180)
        y_min = 400 - 40 * math.cos(6 * mins * math.pi / 180)
        pygame.draw.line(screen, RNAD, (250, 400), (int(x_min), int(y_min)))
        if total_sec < 0:
            total = 0
            start = False
            end = True
    # if total != 0:
    #     pygame.draw.rect(screen,RNAD,(60,530,int(380*(total_sec/total)),30))
    pygame.display.flip()

pygame.quit()
