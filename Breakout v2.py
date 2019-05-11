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
ball_image = Actor('ball')#

music.play("wild wolf")

ball = Ball(WIDTH / 4, HEIGHT / 4, 20, 20)
ball.colour = "green"
ball.direction = 1, 1
ball.speed = 8


BAT_W = 150
BAT_H = 18
paddle = Paddle(WIDTH / 2, HEIGHT - BAT_H, BAT_W, BAT_H)
paddle.colour = "orange"

lpaddle = LPaddle(0, HEIGHT / 2, BAT_H, BAT_W)
lpaddle.colour = "blue"

rpaddle = RPaddle(WIDTH - BAT_H, HEIGHT / 2, BAT_H, BAT_W)
rpaddle.colour = "blue"

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
    screen.draw.filled_rect(ball, ball.colour)
    screen.draw.filled_rect(paddle, paddle.colour)
    screen.draw.filled_rect(lpaddle,lpaddle.colour)
    screen.draw.filled_rect(rpaddle,rpaddle.colour)

    paddle_image.draw()
    lpaddle_image.draw()
    rpaddle_image.draw()
    ball_image.draw()

    for brick in bricks:
        screen.draw.filled_rect(brick, brick.colour)

def on_mouse_move(pos):
    x, y = pos
    paddle.centerx = x
    lpaddle.centery = y
    rpaddle.centery = y

    paddle_image.pos = paddle.centerx, paddle.centery - 2
    lpaddle_image.pos = lpaddle.centerx + 2, lpaddle.centery
    rpaddle_image.pos = rpaddle.centerx - 2, rpaddle.centery

def update():
    dx, dy = ball.direction
    ball.move_ip(ball.speed * dx, ball.speed * dy)

    ball_image.pos = ball.centerx, ball.centery

    if ball.colliderect(paddle):
        sounds.bounce.play()
        ball.direction = dx, -dy
    if ball.colliderect(lpaddle):
        sounds.bounce.play()
        ball.direction = -dx, dy
    if ball.colliderect(rpaddle):
        sounds.bounce.play()
        ball.direction = -dx, dy


    to_kill = ball.collidelist(bricks)
    if to_kill >= 0:
        sounds.laser.play()
        bricks.pop(to_kill)
        ball.direction = dx, -dy

    if ball.right >= WIDTH or ball.left <= 0:
        ball.direction = -dx, dy

    if ball.bottom >= HEIGHT or ball.top <= 0:
        ball.direction = dx, -dy

    if ball.bottom >= HEIGHT:
        sounds.game_over.play()
        time.sleep(2.5)
        exit()
    if ball.left <= 0:
        sounds.game_over.play()
        time.sleep(2.5)
        exit()
    if ball.right >= WIDTH:
        sounds.game_over.play()
        time.sleep(2.5)
        exit()

    if ball.top <= 0:
        ball.direction = dx, -dy


    if not bricks:
        sounds.victory.play()
        time.sleep(2)
        exit()
