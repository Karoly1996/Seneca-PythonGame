# copy over your a1_partd.py file here

from a1_partc import Queue

def get_overflow_list(grid):
    rows = len(grid)
    cols = len(grid[0])
    overflow_list = []

    for r in range(rows):
        for c in range(cols):
            neighbours = 0
            # Update along a row
            if r > 0 and r < rows - 1: 
                neighbours += 2
            else:
                neighbours += 1
            # Update along a column
            if c > 0 and c < cols - 1: 
                neighbours += 2
            else: 
                neighbours += 1
            
            if abs(grid[r][c]) >= neighbours:
                overflow_list.append((r, c))
    
    return overflow_list if overflow_list else None

def overflow(grid, a_queue):
    # Trigger 1: check whether there is any overflowing cell
    def is_overflowcell(grid):
        return get_overflow_list(grid) is not None
    
    # Trigger 2: signs of all non-zero cells should be same
    def diff_sign(grid):
        first_sign = None
        for row in grid:
            for cell in row:
                if cell != 0:
                    if first_sign is None:
                        # True for positive sign
                        first_sign = cell > 0
                    elif (cell > 0) != first_sign:
                        return True
        return False

    # Major handling procedure
    def apply_overflow(grid, a_queue):
        rows = len(grid)
        cols = len(grid[0])
        overflow_cells = get_overflow_list(grid)
        sign = 1 if grid[overflow_cells[0][0]][overflow_cells[0][1]] > 0 else -1
        neighbours_list = []

        for r, c in overflow_cells:
            grid[r][c] = 0
            if r > 0:
                neighbours_list.append((r-1,c)) # up
            if r < rows - 1: 
                neighbours_list.append((r+1,c)) # down
            if c > 0: 
                neighbours_list.append((r,c-1)) # left
            if c < cols - 1: 
                neighbours_list.append((r,c+1)) # right
        
        for r, c in neighbours_list:
            grid[r][c] = (abs(grid[r][c]) + 1)*sign

        grid_copy = [row[:] for row in grid]  # make a copy
        a_queue.enqueue(grid_copy)

    # Recursive part after the first handling
    def recursive_overflow(grid, a_queue):
        # base case
        if is_overflowcell(grid) is False or diff_sign(grid) is False:
            return 0
        
        apply_overflow(grid, a_queue)
        return 1 + recursive_overflow(grid, a_queue)

    # main code
    # initial conditions
    if is_overflowcell(grid) is True and diff_sign(grid) is True:
        apply_overflow(grid, a_queue)
        return 1 + recursive_overflow(grid, a_queue)
    
    return 0
