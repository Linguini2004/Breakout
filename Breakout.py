WIDTH = 1062
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

paddle_image.pos = WIDTH / 2, HEIGHT - (BAT_H / 2)
lpaddle_image.pos = BAT_H / 2, HEIGHT / 2
rpaddle_image.pos = WIDTH - (BAT_H / 2), HEIGHT / 2

Num_Brick = 6
b_in_row = 6

Brick_W = 177
Brick_H = 52
BRICK_IMAGES = ["blue_brick", "green_brick", "orange_brick", "purple_brick"]

bricks = []
# for i in range(Num_Brick):
#     row = (i // b_in_row) + 1
#     v1 = row - 1
#     brick_image = BRICK_IMAGES[i % len(BRICK_IMAGES)]
#     x = i - (v1 * b_in_row) * Brick_W
#     print("x:", x)
#     y = (row * Brick_H) - Brick_H
#     brick = Actor(brick_image, (x, y))
#     brick = Brick((i - (v1 * 10)) * Brick_W, (row * Brick_H) - Brick_H, Brick_W, Brick_H)
#     bricks.append(brick)
#    print(brick._rect)

for n_row in range(2):
    for n_column in range(6):
        x = n_column * Brick_W
        y = n_row * Brick_H
        i = x + (y * 6)
        print("Row: %s, Col: %s, X: %s, H: %s" % (n_row, n_column, x, y))
        brick_image = BRICK_IMAGES[i % len(BRICK_IMAGES)]
        brick = Actor(brick_image, (x, y))
        bricks.append(brick)

def draw():
    screen.clear()

    paddle_image.draw()
    lpaddle_image.draw()
    rpaddle_image.draw()
    ball_image.draw()

    for brick in bricks:
        brick.draw()

def on_mouse_move(pos):
    x, y = pos
    paddle_image.x = x
    lpaddle_image.y = y
    rpaddle_image.y = y

def update():
    dx, dy = ball_image.direction
    ball_image.move_ip(ball_image.speed * dx, ball_image.speed * dy)

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
