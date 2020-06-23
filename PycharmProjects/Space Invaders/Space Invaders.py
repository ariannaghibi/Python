import pygame
import random
import math

# Initialize the pygame and customize the window
pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption('Space Invaders Game by Arian Naghibi')
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
background = pygame.image.load('space.png')

# Player
player_jet = pygame.image.load('jet.png')
explosion = pygame.image.load('regularexplosion02.png')
playerX = 370
playerY = 480
playerX_dx = 0
playerY_dy = 0

# Enemy
enemy_ufo = []
enemyX = []
enemyY = []
enemyX_dx = []
enemyY_dy = []
enemies = 15

for enemy in range(enemies):
    enemy_ufo.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(-40)
    enemyX_dx.append(4)
    enemyY_dy.append(0)

# Bullet
bullet = pygame.image.load('bullet.png')
bulletX = 0
bulletY = -1000
bulletX_dx = 0
bulletY_dy = -10
bullet_state = "ready"

# Meteor
space_meteor = pygame.image.load('meteor.png')
meteorX1 = random.randint(100, 800)
meteorY1 = -40
meteorX2 = random.randint(100, 800)
meteorY2 = -40
meteorX3 = 840
meteorY3 = random.randint(0, 300)
meteorX4 = 840
meteorY4 = random.randint(0, 300)
meteorX_dx = -3
meteorY_dy = 3

# Score
score = 0
high_score = 0
font = pygame.font.Font("freesansbold.ttf", 24)

# Game over
font2 = pygame.font.Font("freesansbold.ttf", 48)


# Functions
def show_score():
    score_board = font.render("Score: " + str(score), True, (255, 255, 255))
    high_score_board = font.render("High Score: " + str(high_score), True, (255, 255, 255))
    screen.blit(score_board, (10, 10))
    screen.blit(high_score_board, (10, 40))


def end_game():
    game_over_menu = font2.render("GAME OVER", True, (255, 255, 255))
    start_command = font.render("press enter to start the game", True, (255, 255, 255))
    screen.blit(game_over_menu, (250, 250))
    screen.blit(start_command, (234, 350))
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    waiting = False


def explosion_effect(x, y):
    screen.blit(explosion, (x, y))
    pygame.display.update()


def player(x, y):
    screen.blit(player_jet, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_ufo[i], (x, y))


def fire_bullet(x, y):
    screen.blit(bullet, (x + 16, y + 16))


def meteor(x, y):
    screen.blit(space_meteor, (x, y))


def is_collision(x1, x2, y1, y2):
    distance = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    if distance <= 48:
        return True
    else:
        return False


# Main loop
game_over = False
running = True
while running:
    if game_over:
        player_explosion_sound = pygame.mixer.Sound("explosion.wav")
        player_explosion_sound.play()
        explosion_effect(playerX, playerY)
        end_game()
        game_over = False
        meteorX1 = random.randint(100, 800)
        meteorY1 = -40
        meteorX2 = random.randint(100, 800)
        meteorY2 = -40
        meteorX3 = 840
        meteorY3 = random.randint(0, 300)
        meteorX4 = 840
        meteorY4 = random.randint(0, 300)
        bulletY = -1000
        bullet_state = "ready"
        for j in range(enemies):
            enemyX[j] = random.randint(0, 735)
            enemyY[j] = -40
        playerX = 370
        playerY = 480
        playerX_dx = 0
        playerY_dy = 0
        if high_score < score:
            high_score = score
        score = 0
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    player(playerX, playerY)
    meteor(meteorX1, meteorY1)
    meteor(meteorX2, meteorY2)
    meteor(meteorX3, meteorY3)
    meteor(meteorX4, meteorY4)
    show_score()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            running = False
        # Key bindings
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_dx = -6
            if event.key == pygame.K_RIGHT:
                playerX_dx = 6
            if event.key == pygame.K_DOWN:
                playerY_dy = 6
            if event.key == pygame.K_UP:
                playerY_dy = -6
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = pygame.mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bulletX = playerX
                    bulletY = playerY
                    bullet_state = "fire"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_dx = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerY_dy = 0

    playerX += playerX_dx
    playerY += playerY_dy
    meteorX1 += meteorX_dx
    meteorY1 += meteorY_dy
    meteorX2 += meteorX_dx
    meteorY2 += meteorY_dy
    meteorX3 += meteorX_dx
    meteorY3 += meteorY_dy
    meteorX4 += meteorX_dx
    meteorY4 += meteorY_dy

    # Enemy Movement
    for i in range(enemies):
        enemy(enemyX[i], enemyY[i], i)
        enemyX[i] += enemyX_dx[i]

        if enemyX[i] > 736:
            enemyX[i] = 736
            enemyX_dx[i] = -4
            enemyY_dy[i] = 80
            enemyY[i] += enemyY_dy[i]
        if enemyX[i] < 0:
            enemyX[i] = 0
            enemyX_dx[i] = 4
            enemyY_dy[i] = 80
            enemyY[i] += enemyY_dy[i]
        if enemyY[i] > 600:
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = -40
        # Bullet & enemy collision checking
        if is_collision(enemyX[i], bulletX, enemyY[i], bulletY):
            enemy_explosion_sound = pygame.mixer.Sound("explosion2.wav")
            enemy_explosion_sound.play()
            explosion_effect(enemyX[i], enemyY[i])
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = -40
            bulletY = -1000
            bullet_state = "ready"
            score += 1

        # Player and enemy collision checking
        if is_collision(enemyX[i], playerX, enemyY[i], playerY):
            game_over = True
    # Player and meteor collision checking
    if is_collision(meteorX1, playerX, meteorY1, playerY) or is_collision(meteorX2, playerX, meteorY2, playerY) or is_collision(meteorX3, playerX, meteorY3, playerY) or is_collision(meteorX4, playerX, meteorY4, playerY):
        game_over = True
    # Fire bullet
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY += bulletY_dy
    # Border checking
    if playerX > 736:
        playerX = 736
    if playerX < 0:
        playerX = 0
    if playerY > 536:
        playerY = 536
    if playerY < 0:
        playerY = 0
    if bulletY < -40:
        bulletY = -1000
        bullet_state = "ready"
    if meteorY1 > 680 or meteorX1 < -80:
        meteorX1 = random.randint(100, 800)
        meteorY1 = -40
    if meteorY2 > 680 or meteorX2 < -80:
        meteorX2 = random.randint(100, 800)
        meteorY2 = -40
    if meteorY3 > 680 or meteorX3 < -80:
        meteorX3 = 840
        meteorY3 = random.randint(0, 300)
    if meteorY4 > 680 or meteorX4 < -80:
        meteorX4 = 840
        meteorY4 = random.randint(0, 300)
    pygame.display.update()
