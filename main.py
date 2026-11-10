def count_ways_in_maze(maze_string):
    maze_coordinates = dict()
    max_row = 0
    max_col = 0
    
    for row_index, line in enumerate(maze_string.strip().splitlines()):
        if row_index > max_row:
            max_row = row_index
        for col_index, value in enumerate(line.split()):
            if col_index > max_col:
                max_col = col_index
            maze_coordinates[tuple((row_index, col_index))] = int(value)
            
    total_rows = max_row + 1
    total_cols = max_col + 1
    
    ways_cache = dict()
    ways_cache[tuple((0, 0))] = 1
    
    for r in range(total_rows):
        for c in range(total_cols):
            current_cell = tuple((r, c))
            if maze_coordinates.get(current_cell) == 1:
                ways_cache[current_cell] = 0
                continue
            if r == 0 and c == 0:
                continue
                
            from_top = ways_cache.get(tuple((r - 1, c)), 0)
            from_left = ways_cache.get(tuple((r, c - 1)), 0)
            ways_cache[current_cell] = from_top + from_left
            
    destination_cell = tuple((max_row, max_col))
    return ways_cache.get(destination_cell, 0)

maze_layout = """
0 0 0
0 1 0
0 0 0
"""

print(count_ways_in_maze(maze_layout))
