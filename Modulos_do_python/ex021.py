import pygame
pygame.init()
pygame.mixer.music.load('Modulos_do_python/ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input("Pressione Enter para parar a música...")
pygame.mixer.music.stop()
