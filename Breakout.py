WIDTH = 1000
HEIGHT = 570

class Ball(ZRect): pass
class Brick(ZRect): pass

import time
import random
paddle_image = Actor('paddle')
lpaddle_image = Actor('lpaddle')
rpaddle_image = Actor('rpaddle')
ball_image = Actor('ball')

music.play("wild wolf")

ball_image.pos = WIDTH / 2, HEIGHT / 2
ball_image.direction = 1, 1
ball_image.speed = 6


BAT_W = 150
BAT_H = 18

paddle_image.pos = WIDTH / 2, HEIGHT - BAT_H
lpaddle_image.pos = BAT_H / 2, HEIGHT / 2
rpaddle_image.pos = WIDTH - (BAT_H / 2), HEIGHT / 2

Num_Brick = 50
Brick_W = WIDTH / 10
Brick_H = Brick_W / 4
BRICK_COLOURS = ["purple", "lightgreen", "lightblue", "orange"]

bricks = []
for i in range(Num_Brick):
    row = (i // 10) + 1
    v1 = row - 1
    brick = Brick((i - (v1 * 10)) * Brick_W, (row * Brick_H) - Brick_H, Brick_W, Brick_H)
    brick.colour = BRICK_COLOURS[i % len(BRICK_COLOURS)]
    bricks.append(brick)

def draw():
    screen.clear()

    paddle_image.draw()
    lpaddle_image.draw()
    rpaddle_image.draw()
    ball_image.draw()

    #for brick in bricks:
    #    screen.draw.filled_rect(brick, brick.colour)

def on_mouse_move(pos):
    x, y = pos
    paddle_image.x = x
    lpaddle_image.y = y
    rpaddle_image.y = y

def update():
    dx, dy = ball_image.direction
    ball_image.move_ip(ball_image.speed * dx, ball_image.speed * dy)

    print(ball_image._rect)
    print(paddle_image._rect)
    if ball_image.colliderect(paddle_image):
        sounds.bounce.play()
        ball_image.direction = dx, -dy
        print("1")
    if ball_image.colliderect(lpaddle_image):
        sounds.bounce.play()
        ball_image.direction = -dx, dy
        print("2")
    if ball_image.colliderect(rpaddle_image):
        sounds.bounce.play()
        ball_image.direction = -dx, dy
        print("3")


    # to_kill = ball_image.collidelist(bricks)
#     if to_kill >= 0:
#         sounds.laser.play()
#         bricks.pop(to_kill)
#         ball_image.direction = dx, -dy

#     if ball_image.right >= WIDTH or ball_image.left <= 0:
#         ball_image.direction = -dx, dy

#     if ball_image.bottom >= HEIGHT or ball_image.top <= 0:
#         ball_image.direction = dx, -dy

#     if ball_image.bottom >= HEIGHT:
#         sounds.game_over.play()
#         time.sleep(2.5)
#         exit()
#     if ball_image.left <= 0:
#         sounds.game_over.play()
#         time.sleep(2.5)
#         exit()
#     if ball_image.right >= WIDTH:
#         sounds.game_over.play()
#         time.sleep(2.5)
#         exit()

#     if ball_image.top <= 0:
#         ball_image.direction = dx, -dy


#     if not bricks:
#         sounds.victory.play()
#         time.sleep(2)
#         exit()
