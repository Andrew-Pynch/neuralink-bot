import pygame, math

"""
Building this to find a better way to render blood vessels
since vasculature patterns resemble trees
"""

pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()
coordinate_list = []
red = (255, 0, 0)
 
def drawTree(x1, y1, angle, depth, coordinate_list):
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
        pygame.draw.line(screen, red, (x1, y1), (x2, y2), 2)
        drawTree(x2, y2, angle - 20, depth - 1, coordinate_list)
        coordinate_list.append([x2, y2])
        drawTree(x2, y2, angle + 20, depth - 1, coordinate_list)
        coordinate_list.append([x2, y2])
    
    return coordinate_list
 
def input(event):
    if event.type == pygame.QUIT:
        exit(0)
 
drawTree(300, 550, -45, 9, coordinate_list)
print(coordinate_list)

pygame.display.flip()
while True:
    input(pygame.event.wait())