import random
import sys
import pygame
pygame.init()
import time
from pygame import mixer

display_width = 800
display_height = 600
display_layout = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Tanchiki")
Resources = pygame.image.load("zemelya.png")

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (200, 200, 0)
tank_width = (40)
tank_height = (20)
up = (0, -1)
down = (0, 1)
right = (1, 0)
left = (-1, 0)


s_font = pygame.font.SysFont("Times New Roman", 25)
m_font = pygame.font.SysFont("Times New Roman", 50)
l_font = pygame.font.SysFont("Times New Roman", 75)
vs_font = pygame.font.SysFont("Times New Roman", 25)
def show_winner(winner):
    text = s_font.render("winner: "+ winner, True, white)
    display_layout.blit(text, (0, 0))
    pygame.display.update()
    time.sleep(2)


player2_sprite = pygame.image.load("tanchik.png")
player1_pos = [0, 0]
player2_pos = [0, 0]
def finish():
    pygame.quit()
    sys.exit()
def main():
    player1_sprite = pygame.image.load("tanchik.png")
    player1_reсt = player1_sprite.get_rect()
    player1_surf = player1_sprite
    timer1 = pygame.time.get_ticks()
    head = up
    bullets_player1 = []
    player_font_score = s_font
    player_count = 0
    lastshot1 = pygame.time.get_ticks()
    player1_reсt.x = 700
    player1_reсt.y = 500

    player2_sprite = pygame.image.load("tanchik.png")
    player2_reсt = player2_sprite.get_rect()
    player2_surf = player2_sprite
    timer2 = pygame.time.get_ticks()
    head2 = up
    bullets_player2 = []
    player_font_score = s_font
    player2_count = 0

    lastshot2 = pygame.time.get_ticks()

    walls = []
    wall1 = pygame.Rect(100, 200, 100, 10)
    walls.append(wall1)
    wall2 = pygame.Rect(400, 299, 100, 10)
    walls.append(wall2)
    wall3 = pygame.Rect(250, 40, 190, 10)
    walls.append(wall3)
    wall4 = pygame.Rect(100, 200, 100, 10)
    walls.append(wall4)
    wall5 = pygame.Rect(10, 423, 100, 10)
    walls.append(wall5)
    wall6 = pygame.Rect(250, 300, 100, 10)
    walls.append(wall6)
    wall7 = pygame.Rect(400, 423, 10, 100)
    walls.append(wall7)
    wall8 = pygame.Rect(250, 300, 10, 100)
    walls.append(wall8)
    wall9 = pygame.Rect(600, 300, 10, 100)
    walls.append(wall9)

    mixer.music.load('background_music.mp3')
    print("music started playing....")
    mixer.music.set_volume(0.1)
    mixer.music.play()


    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                finish()
            now = pygame.time.get_ticks()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e and now - lastshot2 >= 2000:
                lastshot2 = now
                bullet = {
                    "rect":pygame.Rect(player2_reсt.centerx, player2_reсt.centery, 10,10),
                    "direction":head2
               }
                bullets_player2.append(bullet)


            if event.type == pygame.KEYDOWN and event.key == pygame.K_n and now - lastshot1 >= 2000:
                lastshot1 = now
                bullet = {
                    "rect":pygame.Rect(player1_reсt.centerx, player1_reсt.centery, 10,10),
                    "direction":head
                }
                bullets_player1.append(bullet)



        keys = pygame.key.get_pressed()  # Checking pressed keys
        now = pygame.time.get_ticks()

        if keys[pygame.K_UP] and now - timer1 > 20:
            player1_surf = pygame.transform.rotate(player1_sprite, 0)
            player1_reсt.y -= 1
            if player1_reсt.y < 0 or player1_reсt.collidelist(walls) != -1:
                player1_reсt.y += 1
            head = up
            timer1 = now

        if keys[pygame.K_DOWN] and now - timer1 > 20:
            player1_surf = pygame.transform.rotate(player1_sprite, -180)
            player1_reсt.y += 1
            if player1_reсt.y > 590 or player1_reсt.collidelist(walls) != -1:
                player1_reсt.y -= 1
            head = down
            timer1 = now
        if keys[pygame.K_RIGHT] and now - timer1 > 20:
            player1_surf = pygame.transform.rotate(player1_sprite, -90)
            player1_reсt.x += 1
            if player1_reсt.x > 790 or player1_reсt.collidelist(walls) != -1:
                player1_reсt.x -= 1
            head = right
            timer1 = now
        if keys[pygame.K_LEFT] and now - timer1 > 20:
            player1_surf = pygame.transform.rotate(player1_sprite, -270)
            player1_reсt.x -= 1
            if player1_reсt.x < 0 or player1_reсt.collidelist(walls) != -1:
                player1_reсt.x += 1
            head = left
            timer1 = now




        if keys[pygame.K_w] and now - timer2 > 20:
            player2_surf = pygame.transform.rotate(player2_sprite, 0)
            player2_reсt.y -= 1
            if player2_reсt.y < 0 or player2_reсt.collidelist(walls) != -1:
                player2_reсt.y += 1
            head2 = up
            timer2 = now
        if keys[pygame.K_s] and now - timer2 > 20:
            player2_surf = pygame.transform.rotate(player2_sprite, -180)
            player2_reсt.y += 1
            if player2_reсt.y > 590 or player2_reсt.collidelist(walls) != -1:
                player2_reсt.y -= 1
            head2 = down
            timer2 = now
        if keys[pygame.K_d] and now - timer2 > 20:
            player2_surf = pygame.transform.rotate(player2_sprite, -90)
            player2_reсt.x += 1
            if player2_reсt.x > 790 or player2_reсt.collidelist(walls) != -1:
                player2_reсt.x -= 1
            head2 = right
            timer2 = now
        if keys[pygame.K_a] and now - timer2 > 20:
            player2_surf = pygame.transform.rotate(player2_sprite, -270)
            player2_reсt.x -= 1
            if player2_reсt.x < 0 or player2_reсt.collidelist(walls) != -1:
                player2_reсt.x += 1
            head2 = left
            timer2 = now



        for bullet in bullets_player1:
            bullet["rect"].x += bullet["direction"][0]* 1
            bullet["rect"].y += bullet["direction"][1] * 1
        bullets_player1 = [b for b in bullets_player1 if 0 <= b["rect"].x <= display_width and 0 <= b["rect"].y <= display_height and b["rect"].collidelist(walls) == -1]


        for bullet in bullets_player2:
            bullet["rect"].x += bullet["direction"][0]* 1
            bullet["rect"].y += bullet["direction"][1] * 1
        bullets_player2 = [b for b in bullets_player2 if 0 <= b["rect"].x <= display_width and 0 <= b["rect"].y <= display_height and b["rect"].collidelist(walls) == -1]

        display_layout.fill(black)
        display_layout.blit(player1_surf, player1_reсt)
        display_layout.blit(player2_surf, player2_reсt)
        for bullet in bullets_player1:
            pygame.draw.rect(display_layout, red, bullet["rect"])

        for bullet in bullets_player2:
            pygame.draw.rect(display_layout, red, bullet["rect"])
        for wall in walls:
            pygame.draw.rect(display_layout, white, wall)
        pygame.display.update()

        for bullet in bullets_player1:
            if player2_reсt.colliderect(bullet["rect"]):
                show_winner("player1")
                player1_reсt.x = 700
                player1_reсt.y = 500
                player2_reсt.x = 0
                player2_reсt.y = 0
                bullets_player1.clear()
                bullets_player2.clear()
        bullets_player1 = [p for p in bullets_player1 if not player2_reсt.colliderect(p["rect"])]

        for bullet in bullets_player2:
            if player1_reсt.colliderect(bullet["rect"]):
                show_winner("player2")
                player1_reсt.x = 700
                player1_reсt.y = 500
                player2_reсt.x = 0
                player2_reсt.y = 0
                bullets_player1.clear()
                bullets_player2.clear()
        bullets_player2 = [p for p in bullets_player2 if not player1_reсt.colliderect(p["rect"])]




main()
