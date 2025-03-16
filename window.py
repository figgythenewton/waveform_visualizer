# Example file showing a basic pygame "game loop"
import pygame
import math
import numpy as np
import librosa as lb
import audio_utils as u


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1025, 577))
clock = pygame.time.Clock()
running = True

y, sr = lb.load('./audio_file/human_133.mp3', sr=48000)
cp_m = lb.stft(y)

stft_idx = 0
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    current_stft_frame = cp_m[:, stft_idx]
    points = list(zip(np.arange(screen.get_width()), np.clip(np.abs(current_stft_frame), a_min=0, a_max=screen.get_height())))
    pygame.draw.lines(screen, "black", False, points)
    # flip() the display to put your work on screen
    pygame.display.flip()
    stft_idx += 1
    clock.tick(60)  # limits FPS to 60
    

pygame.quit()