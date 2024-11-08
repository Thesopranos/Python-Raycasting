import sys

def map_checker(map_path):
	# check .map file
	if not map_path.endswith('.map'):
		sys.exit('The map file must be a .map file')

	# check map file
	with open(map_path, 'r') as file:
		map_lines = file.readlines()

	# check map lines
	for i, line in enumerate(map_lines):
		line = line.strip()

		# check line characters
		for j, char in enumerate(line):
			if char not in ['0', '1']:
				sys.exit(f'Invalid character {char} at line {i + 1}, column {j + 1}')

	return True, None

def map_loader(map_path):
	# load map file
	with open(map_path, 'r') as file:
		map_lines = file.readlines()

	# create map
	world_map = []
	for line in map_lines:
		world_map.append([int(char) for char in line.strip()])

	return world_map

def check_player_position(world_map, tile_size):
	# check player position
	for i, line in enumerate(world_map):
		for j, char in enumerate(line):
			if char == 0:
				return j * tile_size, i * tile_size
	return None

