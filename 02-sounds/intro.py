#!/usr/bin/env python

import pygame, sys 
from pygame.locals import *

pygame.init()

sound = pygame.mixer.Sound('gameover.wav')
sound.play()

import time
time.sleep(3)
sound.stop()