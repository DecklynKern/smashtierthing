import pygame, os
from aliases import *

pygame.init()

folder = input("folder: ")

people = []

while True:
    
    name = input("tag (enter blank if done): ")

    if name == "":
        break

    while True:

        char = input("char: ").replace(" ", "").replace(".", "").replace("/", "").lower()

        if char in aliases:
            char = aliases[char]

        if not os.path.exists("char images\\" + char + ".png"):
            print("invalid character/no character image")

        else:
            break
        
    people.append((name, char))

screen = pygame.display.set_mode((256, 256))
font = pygame.font.Font("super_smash_4_1_by_pokemon_diamond-d7zxu6d.ttf", 36)

try:
    os.mkdir(folder)

except FileExistsError:
    pass

for person in people:
    
    name, char = person

    img = pygame.image.load("char images\\" + char + ".png").convert_alpha()
    width, height = img.get_size()

    # i am aware all of the below is evil and hacky
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

    surf = pygame.Surface((256, 256)).convert_alpha()
    surf.blit(img, ((256 - width)/2, (256 - height)/2))

    nx = (256 - nWidth) / 2
    ny = 256 - nHeight

    # manually make a nice outline :)
    surf.blit(outline, (nx-2, ny))
    surf.blit(outline, (nx-2, ny-2))
    surf.blit(outline, (nx, ny-2))
    surf.blit(outline, (nx+2, ny-2))
    surf.blit(outline, (nx+2, ny))
    surf.blit(outline, (nx+2, ny+2))
    surf.blit(outline, (nx, ny+2))
    surf.blit(outline, (nx-2, ny+2))
    surf.blit(nameText, (nx, ny))

    outputImage = folder + name + ".png"

    if os.path.exists(outputImage):
        print(outputImage + "already exists, overwriting")

    else:
        print("created " + outputImage)

    pygame.image.save(surf, outputImage)

    screen.fill((0,0,0))
    screen.blit(surf, (0,0))
    pygame.event.pump()

    pygame.display.flip()
    
pygame.quit()
