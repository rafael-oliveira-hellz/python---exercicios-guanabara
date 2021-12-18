## Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.init()
pygame.mixer.music.load('C:/Users/rafael.oliveirasilva/Desktop/Dev/BackEnd/Python/exercicios-em-aula/goosehouse.mp3')
pygame.mixer.music.play()
pygame.event.wait()