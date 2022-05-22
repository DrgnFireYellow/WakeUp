import time
import pygame.mixer
pygame.mixer.init()
alarm = pygame.mixer.Sound("alarm.wav")
length = int(input("In how many minutes should I wake you up? ")) * 60
time.sleep(length)
alarm.play()