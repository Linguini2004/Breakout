WIDTH = 1000
HEIGHT = 570

class Ball(ZRect): pass
class Paddle(ZRect): pass
class LPaddle(ZRect): pass
class RPaddle(ZRect): pass
class Brick(ZRect): pass

import time
import random
paddle_image = Actor('paddle')
lpaddle_image = Actor('lpaddle')
rpaddle_image = Actor('rpaddle')
ball_image = Actor('ball')

music.play("wild wolf")

#ball_image = Ball(WIDTH / 4, HEIGHT / 4, 20, 20)
#ball_image.colour = "green"
ball_image.direction = 1, 1
ball_image.speed = 8


BAT_W = 150
BAT_H = 18
#paddle_image = Paddle(WIDTH / 2, HEIGHT - BAT_H, BAT_W, BAT_H)
#paddle_image.colour = "orange"

#lpaddle_image = LPaddle(0, HEIGHT / 2, BAT_H, BAT_W)
#lpaddle_image.colour = "blue"

#rpaddle_image = RPaddle(WIDTH - BAT_H, HEIGHT / 2, BAT_H, BAT_W)
#rpaddle_image.colour = "blue"

paddle_image = WIDTH / 2, HEIGHT - BAT_H
lpaddle_image = 0, HEIGHT / 2
rpaddle_image = WIDTH - BAT_H, HEIGHT / 2

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
    #screen.draw.filled_rect(ball_image, ball_image.colour)
    #screen.draw.filled_rect(paddle_image, paddle_image.colour)
    #screen.draw.filled_rect(lpaddle_image,lpaddle_image.colour)
    #screen.draw.filled_rect(rpaddle_image,rpaddle_image.colour)

    paddle_image.draw()
    lpaddle_image.draw()
    rpaddle_image.draw()
    ball_image.draw()

    for brick in bricks:
        screen.draw.filled_rect(brick, brick.colour)

def on_mouse_move(pos):
    x, y = pos
    print(repr(paddle_image))
    paddle_image.x = x
    lpaddle_image.y = y
    rpaddle_image.y = y

    #paddle_image.pos = paddle_image.centerx, paddle_image.centery - 2
    #lpaddle_image.pos = lpaddle_image.centerx + 2, lpaddle_image.centery
    #rpaddle_image.pos = rpaddle_image.centerx - 2, rpaddle_image.centery

def update():
    dx, dy = ball_image.direction
    ball_image.move_ip(ball_image.speed * dx, ball_image.speed * dy)

    ball_image.pos = ball_image.centerx, ball_image.centery

    if ball_image.colliderect(paddle_image):
        sounds.bounce.play()
        ball_image.direction = dx, -dy
    if ball_image.colliderect(lpaddle_image):
        sounds.bounce.play()
        ball_image.direction = -dx, dy
    if ball_image.colliderect(rpaddle_image):
        sounds.bounce.play()
        ball_image.direction = -dx, dy


    to_kill = ball_image.collidelist(bricks)
    if to_kill >= 0:
        sounds.laser.play()
        bricks.pop(to_kill)
        ball_image.direction = dx, -dy

    if ball_image.right >= WIDTH or ball_image.left <= 0:
        ball_image.direction = -dx, dy

    if ball_image.bottom >= HEIGHT or ball_image.top <= 0:
        ball_image.direction = dx, -dy

    if ball_image.bottom >= HEIGHT:
        sounds.game_over.play()
        time.sleep(2.5)
        exit()
    if ball_image.left <= 0:
        sounds.game_over.play()
        time.sleep(2.5)
        exit()
    if ball_image.right >= WIDTH:
        sounds.game_over.play()
        time.sleep(2.5)
        exit()

    if ball_image.top <= 0:
        ball_image.direction = dx, -dy


    if not bricks:
        sounds.victory.play()
        time.sleep(2)
        exit()
