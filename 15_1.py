import pygame

# Define colors and constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (102, 99, 112)
BLUE = (0, 53, 189)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
BLUE_GREEN = (0, 102, 128)
DARK_BLUE = (71, 136, 147)
W = 800
H = 1000
pi = 3.14

pygame.init()

FPS = 30
sc = pygame.display.set_mode((W, H))
pygame.draw.rect(sc, (33, 33, 120), (0, 0, W, 104))
pygame.draw.rect(sc, (141, 95, 211), (0, 104, W, 160))
pygame.draw.rect(sc, (205, 135, 222), (0, 160, W, 253))
pygame.draw.rect(sc, (222, 135, 170), (0, 253, W, 384))
pygame.draw.rect(sc, (255, 153, 85), (0, 384, W, 493))
pygame.draw.rect(sc, (0, 102, 128), (0, 493, W, H))

# Create bird surface
def create_bird():
    surf_bird = pygame.Surface((600, 436), pygame.SRCALPHA)

    # Draw beak
    pygame.draw.polygon(surf_bird, YELLOW, [[507, 223], [577, 216], [591, 227],
                                            [563, 243], [507, 236]])
    pygame.draw.polygon(surf_bird, BLACK, [[507, 223], [577, 216], [591, 227],
                                            [563, 243], [507, 236]], 1)
    pygame.draw.aalines(surf_bird, BLACK, False, [[521, 222], [544, 229], [579, 230], [590, 227]], 1)

    # Draw legs
    surf_for_ellipse_angle = pygame.Surface((56, 80), pygame.SRCALPHA)
    pygame.draw.ellipse(surf_for_ellipse_angle, WHITE, (0, 0, 54, 80))
    rotated_surf = pygame.transform.rotate(surf_for_ellipse_angle, 5*pi/3)
    surf_bird.blit(rotated_surf, (294, 278))
    surf_bird.blit(rotated_surf, (317, 268))

    surf_for_ellipse_angle = pygame.Surface((128, 30), pygame.SRCALPHA)
    pygame.draw.ellipse(surf_for_ellipse_angle, WHITE, (0, 0, 128, 30))
    rotated_surf = pygame.transform.rotate(surf_for_ellipse_angle, 340)
    surf_bird.blit(rotated_surf, (310, 335))
    surf_bird.blit(rotated_surf, (340, 310))

    # Draw claws
    surf_for_claws = pygame.Surface((500, 500), pygame.SRCALPHA)
    pygame.draw.polygon(surf_for_claws, YELLOW, [[411, 358], [443, 346], [458, 346], [472, 356], [472, 360], [464, 355], [445, 355],
                                            [437, 358], [451, 358], [476, 372], [454, 364], [437, 363], [449, 365], [471, 381],
                                            [430, 366], [421, 365], [415, 370], [408, 406], [403, 397], [402, 397], [406, 363]])
    pygame.draw.polygon(surf_for_claws, BLACK, [[411, 358], [443, 346], [458, 346], [472, 356], [472, 360], [464, 355], [445, 355],
                                            [437, 358], [451, 358], [476, 372], [454, 364], [437, 363], [449, 365], [471, 381],
                                            [430, 366], [421, 365], [415, 370], [408, 406], [403, 397], [402, 397], [406, 363]], 1)
    surf_bird.blit(surf_for_claws, (40, 5))
    surf_bird.blit(surf_for_claws, (20, 30))

    # Draw tail
    pygame.draw.polygon(surf_bird, WHITE, [[208, 270], [156, 267], [112, 248], [120, 215],
                                           [132, 183], [145, 159], [214, 243]])
    pygame.draw.polygon(surf_bird, BLACK, [[208, 270], [156, 267], [112, 248], [120, 215],
                                           [132, 183], [145, 159], [214, 243]], 1)

    # Draw wings
    pygame.draw.polygon(surf_bird, WHITE, [[202, 131], [182, 110], [108, 78], [97, 67], [65, 6], [65, 0], [69, 0], [108, 33],
                                           [151, 54], [205, 70], [273, 81], [294, 90], [313, 130], [323, 199], [320, 190], [323, 228]])
    pygame.draw.polygon(surf_bird, BLACK, [[202, 131], [182, 110], [108, 78], [97, 67], [65, 6], [65, 0], [69, 0], [108, 33],
                                           [151, 54], [205, 70], [273, 81], [294, 90], [313, 130], [323, 199], [320, 190], [323, 228]], 1)
    pygame.draw.polygon(surf_bird, WHITE, [[230, 240], [186, 216], [166, 197], [148, 174], [128, 165], [66, 153], [47, 142],
                                           [4, 86], [3, 82], [11, 82], [31, 96], [65, 111], [109, 120], [152, 124], [224, 122],
                                           [246, 128], [270, 163], [293, 218]])
    pygame.draw.polygon(surf_bird, BLACK, [[230, 240], [186, 216], [166, 197], [148, 174], [128, 165], [66, 153], [47, 142],
                                           [4, 86], [3, 82], [11, 82], [31, 96], [65, 111], [109, 120], [152, 124], [224, 122],
                                           [246, 128], [270, 163], [293, 218]], 1)

    # Draw body
    pygame.draw.ellipse(surf_bird, WHITE, (200, 211, 200, 96))
    pygame.draw.ellipse(surf_bird, WHITE, (383, 230, 86, 43))
    pygame.draw.ellipse(surf_bird, WHITE, (444, 205, 75, 47))
    pygame.draw.ellipse(surf_bird, BLACK, (489, 218, 14, 10))

    return surf_bird

# Create fish surface
def create_fish():
    surf_fish = pygame.Surface((200, 100), pygame.SRCALPHA)

    pygame.draw.polygon(surf_fish, LIGHT_GRAY, [[155, 34], [157, 29], [157, 25], [151, 17], [92, 10], [125, 30]])
    pygame.draw.polygon(surf_fish, BLACK, [[155, 34], [157, 29], [157, 25], [151, 17], [92, 10], [125, 30]], 1)

    pygame.draw.polygon(surf_fish, DARK_BLUE, [[65, 49], [35, 47], [13, 40], [21, 77]])
    pygame.draw.polygon(surf_fish, BLACK, [[65, 49], [35, 47], [13, 40], [21, 77]], 1)

    pygame.draw.polygon(surf_fish, LIGHT_GRAY, [[92, 62], [83, 74], [77, 76], [104, 80], [107, 76], [106, 65]])
    pygame.draw.polygon(surf_fish, BLACK, [[92, 62], [83, 74], [77, 76], [104, 80], [107, 76], [106, 65]], 1)

    pygame.draw.polygon(surf_fish, LIGHT_GRAY, [[144, 70], [145, 84], [151, 93], [175, 79], [165, 77], [155, 70]])
    pygame.draw.polygon(surf_fish, BLACK, [[144, 70], [145, 84], [151, 93], [175, 79], [165, 77], [155, 70]], 1)

    pygame.draw.polygon(surf_fish, DARK_BLUE, [[191, 54], [171, 39], [143, 30], [124, 30], [96, 36],
                                               [64, 49], [90, 61], [124, 70], [153, 70], [179, 62]])
    pygame.draw.polygon(surf_fish, BLACK, [[191, 54], [171, 39], [143, 30], [124, 30], [96, 36],
                                               [64, 49], [90, 61], [124, 70], [153, 70], [179, 62]], 1)
    pygame.draw.circle(surf_fish, BLUE, (166, 53), 9)
    pygame.draw.ellipse(surf_fish, BLACK, (163, 51, 6, 7))
    return surf_fish

# Create fish surface
def create_cloud():
    surf_cloud = pygame.Surface((207, 46), pygame.SRCALPHA)
    pygame.draw.arc(surf_cloud, WHITE, (0, 0, 103, 46), 0, pi, 3)
    pygame.draw.arc(surf_cloud, WHITE, (104, 0, 103, 46), 0, pi, 3)

    return surf_cloud

surf_bird = create_bird()
surf_fish = create_fish()
surf_cloud = create_cloud()

scale = pygame.transform.scale(surf_bird, (surf_bird.get_width() // 1.02, surf_bird.get_height() // 1.11))
sc.blit(scale, (0, 508))

scale = pygame.transform.scale(surf_bird, (surf_bird.get_width() // 4.02, surf_bird.get_height() // 4.79))
sc.blit(scale, (322, 493))

scale = pygame.transform.flip(surf_bird, True, False)
scale = pygame.transform.scale(scale, (surf_bird.get_width() // 3.02, surf_bird.get_height() // 3.15))
sc.blit(scale, (569, 517))

sc.blit(surf_fish, (569, 726))
sc.blit(surf_fish, (525, 880))
sc.blit(surf_fish, (78, 890))

sc.blit(surf_cloud, (389, 168))

scale = pygame.transform.rotate(surf_cloud, -10)
scale = pygame.transform.scale(scale, (scale.get_width() // 3.27, scale.get_height() // 2.55))
sc.blit(scale, (355, 78))
sc.blit(scale, (452, 62))
sc.blit(scale, (457, 106))
sc.blit(scale, (424, 130))

scale = pygame.transform.rotate(surf_cloud, -10)
sc.blit(scale, (120, 304))

scale = pygame.transform.scale(surf_cloud, (scale.get_width() // 3.00, scale.get_height() // 4.18))
sc.blit(scale, (393, 347))
sc.blit(scale, (421, 308))
sc.blit(scale, (313, 314))

scale = pygame.transform.scale(surf_cloud, (scale.get_width() // 2.00, scale.get_height() // 2.55))
sc.blit(scale, (546, 289))
sc.blit(scale, (670, 350))
sc.blit(scale, (714, 297))
sc.blit(scale, (689, 237))
sc.blit(scale, (407, 271))

scale = pygame.transform.rotate(surf_cloud, 10)
sc.blit(scale, (99, 25))
scale = pygame.transform.scale(scale, (scale.get_width() // 3.18, scale.get_height() // 4.15))
sc.blit(scale, (365, 242))
sc.blit(scale, (261, 266))
sc.blit(scale, (339, 209))
sc.blit(scale, (341, 267))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()