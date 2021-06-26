import pygame, os
from aliases import *

people = []

folder = input("folder: ")

while True:
    name = input("tag: ")
    if name == "":
        break
    char = input("char: ")
    people.append((name,char))

pygame.init()

font = pygame.font.Font("super_smash_4_1_by_pokemon_diamond-d7zxu6d.ttf", 36)

screen = pygame.display.set_mode((256, 256))

try:
    os.mkdir(folder)

except FileExistsError:
    pass

for person in people:
    name, char = person

    img = pygame.image.load(char + ".png").convert_alpha()
    width, height = img.get_size()

    if width > height:
        height = int(height/width * 256)
        width = 256

    else:
        width = int(width/height * 256)
        height = 256

    img = pygame.transform.scale(img, (width, height))

    nameText = font.render(name, 1, (255, 255, 255))
    nWidth, nHeight = nameText.get_size()

    outline = font.render(name, 1, (0, 0, 0))

    if nWidth > 256:
        nHeight = int(nWidth/256 * nHeight)
        nWidth = 256
        nameText = pygame.transform.scale(nameText, (256, nHeight))
        outline = pygame.transform.scale(outline, (256, nHeight))

    surf = pygame.Surface((256, 256))
    surf.blit(img, ((256 - width)/2, (256 - height)/2))

    nx =(256 - nWidth) / 2
    ny = 256 - nHeight

    surf.blit(outline, (nx-2, ny))
    surf.blit(outline, (nx-2, ny-2))
    surf.blit(outline, (nx, ny-2))
    surf.blit(outline, (nx+2, ny-2))
    surf.blit(outline, (nx+2, ny))
    surf.blit(outline, (nx+2, ny+2))
    surf.blit(outline, (nx, ny+2))
    surf.blit(outline, (nx-2, ny+2))
    surf.blit(nameText, (nx, ny))

    pygame.image.save(surf, folder + name + ".png")

    screen.fill((0,0,0))
    screen.blit(surf, (0,0))
    pygame.event.pump()

    pygame.display.flip()
    
pygame.quit()
