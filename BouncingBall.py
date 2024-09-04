import pygame
import math
import random
import numpy as np
pygame.init()
# program size
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
#color
BLACK = (0,0,0)
RED = (255,3,14)
ORANGE = (234,123,3)
#variable
running = True
    #circle
CIRCLE_CENTER = np.array((WIDTH/2,HEIGHT/2),dtype=np.float64)
CIRCLE_RADIUS = 150
    #ball
class Ball:
    def __init__(self,position,vel,is_in=True):
        self.pos = np.array(position,dtype=np.float64)
        self.v = np.array(vel,dtype=np.float64)
        self.is_in = is_in
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
BALL_RADIUS = 5
ball_pos = np.array([WIDTH/2, HEIGHT/2 - 120],dtype=np.float64)
ball_v = np.array([0,0],dtype=np.float64)
GRAVITY = 0.2
is_ball_in = True
    #angle lost
angle = 60
end_angle = math.radians(angle/2)
start_angle = math.radians(-angle/2)
spinning_speed = 0.01
balls = [Ball(ball_pos,ball_v)]
def draw_arh(screen,center,radius,start_ang,end_ang):
    start_point = center + (radius+1000) * np.array([math.cos(start_ang),math.sin(start_ang)],dtype=np.float64)
    end_point = center + (radius+1000) * np.array([math.cos(end_ang),math.sin(end_ang)],dtype=np.float64)
    pygame.draw.polygon(screen,BLACK,[center,start_point,end_point])
def is_in_angle(ballposition,start_ang,end_ang,center):
    dy = ballposition[1] - center[1]
    dx = ballposition[0] - center[0]
    start_angle = start_ang %(2*math.pi)
    end_angle = end_ang %(2*math.pi)
    if start_angle >end_angle:
        end_angle += 2*math.pi
    alpha = math.atan2(dy, dx)
    if start_ang <= alpha <= end_ang or start_angle<= alpha + 2*math.pi <= end_angle:
        return True

#main
while running:
    #draw window and QUIT button
    screen.fill(BLACK)
    mouse_x,mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    start_angle += spinning_speed
    end_angle += spinning_speed
    #main program
    for ball in balls:
        if ball.pos[0]> HEIGHT or ball.pos[0]<0 or ball.pos[1]>WIDTH or ball.pos[1] < 0:
            balls.remove(ball)
            balls.append(Ball([WIDTH/2, HEIGHT/2 - 120],[random.uniform(-3,3),random.uniform(-3,4)]))
            balls.append(Ball([WIDTH / 2, HEIGHT / 2 - 120], [random.uniform(-3, 3), random.uniform(-3, 4)]))
        ball.v[1] += GRAVITY
        ball.pos += ball.v
        dist = np.linalg.norm(ball.pos-CIRCLE_CENTER)
        if dist + BALL_RADIUS > CIRCLE_RADIUS:
            if is_in_angle(ball.pos,start_angle,end_angle,CIRCLE_CENTER):
                ball.is_in = False

            if ball.is_in:
                d = ball.pos - CIRCLE_CENTER
                d_unit = d/np.linalg.norm(d)
                ball.pos = CIRCLE_CENTER + (CIRCLE_RADIUS-BALL_RADIUS)*d_unit
                t = np.array([-d[1],d[0]],dtype=np.float64)
                projection_v = (np.dot(ball.v,t)/np.dot(t,t))*t
                ball.v = 2*projection_v - ball.v
                ball.v += t*spinning_speed #v =rw
    pygame.draw.circle(screen,ORANGE,CIRCLE_CENTER,CIRCLE_RADIUS,2)
    draw_arh(screen, CIRCLE_CENTER, CIRCLE_RADIUS, start_angle, end_angle)
    for ball in balls:
        pygame.draw.circle(screen, ball.color, ball.pos, BALL_RADIUS)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()