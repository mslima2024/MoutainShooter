import pygame
print("Setup Start")
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print("Setup End")

print("Loop Start")

while True:
    # Check all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Quitting...') # commit test
            pygame.quit() # close window
            quit() # end pygame
