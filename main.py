from src.map import map_checker, map_loader, check_player_position
import pygame
import math
import sys

map_path = None
world_map = None
# take arguments from the command line
if len(sys.argv) != 2:
    sys.exit('Usage: python main.py map_file.map\n')
else:
    map_path = sys.argv[1]
    map_checker(map_path)
    world_map = map_loader(map_path)
    if not world_map:
        sys.exit('The map file is empty')

# window size clc
WIN_WIDTH, WIN_HEIGHT = 800, 600

# every tile size in the map, tile size is 80x80 pixels
TILE_SIZE = 80

# player position must check on wall
player_x, player_y = check_player_position(world_map, TILE_SIZE)

# player angle
player_angle = 0

# player view angle
FOV = math.pi / 3 # 60 degrees

# number of rays
NUM_RAYS = 240

# maximum depth
MAX_DEPTH = 800

# angle between two rays
DELTA_ANGLE = FOV / NUM_RAYS

# distance to projection plane
DISTANCE_PROJ_PLANE = (WIN_WIDTH // 2) / math.tan(FOV / 2)

# wall color
WALL_COLOR = (0, 255, 0)

# Initialize Pygame
pygame.init()

# create window
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# create clock
clock = pygame.time.Clock()

# wall check function
def is_wall(x, y):

    # x and y are the coordinates of the point we want to check
    map_x, map_y = int(x / TILE_SIZE), int(y / TILE_SIZE)

    # if the coordinates are within the map boundaries and there is a wall at that coordinate, return True
    if 0 <= map_x < len(world_map[0]) and 0 <= map_y < len(world_map):
        return world_map[map_y][map_x] == 1

    # if the coordinates are outside the map boundaries or there is no wall at that coordinate, return False
    return False

def raycasting(screen):

    # a loop for each ray
	for ray in range(NUM_RAYS):
        # calculate the ray angle
		ray_angle = player_angle - FOV / 2 + ray * DELTA_ANGLE

        # for each depth
		for depth in range(MAX_DEPTH):

            # calculate the target x coordinate of the ray
			target_x = player_x + depth * math.cos(ray_angle)
            # calculate the target y coordinate of the ray
			target_y = player_y + depth * math.sin(ray_angle)

            # if the target point is a wall
			if is_wall(target_x, target_y):
                # calculate the distance to the wall
				wall_height = TILE_SIZE * WIN_HEIGHT / (depth * math.cos(player_angle - ray_angle))
                # calculate the color intensity
				color_intensity = 1 - min(1, depth / MAX_DEPTH)
                # calculate the color
				color = (WALL_COLOR[0] * color_intensity, WALL_COLOR[1] * color_intensity, WALL_COLOR[2] * color_intensity)
                # draw the wall
				pygame.draw.line(screen, color,
                 (ray * WIN_WIDTH / NUM_RAYS, WIN_HEIGHT // 2 - wall_height // 2),
                 (ray * WIN_WIDTH / NUM_RAYS, WIN_HEIGHT // 2 + wall_height // 2))
				break

# movement function
def movement():
    global player_x, player_y, player_angle
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        # rotate the player to the left
        player_angle -= 0.05

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_angle += 0.05

        # rotate the player to the right
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        # check if the player is going to hit a wall
        if not is_wall(player_x + 5 * math.cos(player_angle), player_y + 5 * math.sin(player_angle)):
            player_x += 5 * math.cos(player_angle)
            player_y += 5 * math.sin(player_angle)

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        # check if the player is going to hit a wall
        if not is_wall(player_x - 5 * math.cos(player_angle), player_y - 5 * math.sin(player_angle)):
            player_x -= 5 * math.cos(player_angle)
            player_y -= 5 * math.sin(player_angle)

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit(0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    movement()
    raycasting(screen)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()

if __name__ == "__main__":
    pass
