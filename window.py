# Example file showing a basic pygame "game loop"
import pygame
import math
import numpy as np
import librosa as lb
import wave_display as wvdsp


# pygame setup
pygame.init()
pygame.mixer.init(frequency=44100)
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

filename = './audio_file/human_133.mp3' 
wv = wvdsp.WaveDisplay(filename, sr=44100)
wv.get_ft(n_fft=2940)
song = pygame.mixer.Sound(filename)
waveform = pygame.sndarray.array(song)
# song.play()
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    points = wv.get_ft_frame(screen.get_width(), screen.get_height())
    inv_points = [(screen.get_width()-x, screen.get_height()-y) for x, y in points]
    pygame.draw.lines(screen, "#00f7ff", False, points)
    pygame.draw.lines(screen, "#00f7ff", False, inv_points)


    # flip() the display to put your work on screen
    pygame.display.flip()
    wv.update()
    clock.tick(60)  # limits FPS to 60
    

pygame.quit()