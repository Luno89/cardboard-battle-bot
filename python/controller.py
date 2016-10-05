import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()
pygame.joystick.init()

# -------- Main Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.JOYBUTTONDOWN:
            print("joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released")
    
    screen.fill(WHITE)
    
    joystick_count = pygame.joystick.get_count()
    
    print("Number of joystick: {}".format(joystick_count))
    
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        
        name = joystick.get_name()        
        
        axes = joystick.get_numaxes()
        for i in range(axes):
            axis = joystick.get_axis(i)
            print("Axis {} value: {:>6.3f}".format(i, axis))
        
        buttons = joystick.get_numbuttons()
        print("Number of buttons: {}".format(buttons))
        for i in range(buttons):
            button = joystick.get_button(i)            
            print("Button {:>2} value: {}".format(i, button))
                  
        hats = joystick.get_numhats()
        print("Number of hats: {}".format(i, str(hats)))
        for i in range(hats):
            hat = joystick.get_hat(i)
        
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
