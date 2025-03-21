import random


def can_place_shape(grid, shape):
    """Check if a shape can be placed anywhere on the grid"""
    if not hasattr(shape, "form") or not shape.form:
        return False, None

    size = [len(shape.form), len(shape.form[0])]

    for i in range(8):
        for j in range(8):
            valid = True
            for i1 in range(size[0]):
                for j1 in range(size[1]):
                    if shape.form[i1][j1]:
                        if (i + i1 > 7) or (j + j1 > 7) or grid[i + i1][j + j1]:
                            valid = False
                            break
                if not valid:
                    break

            if valid:
                return True, (
                    i,
                    j,
                )  # Return  a boolean and the position where it can be placed

    return False, None


def find_best_placement(grid, shape):
    """Find the best position to place a shape that might clear lines"""
    if not hasattr(shape, "form") or not shape.form:
        return None

    size = [len(shape.form), len(shape.form[0])]
    best_position = None
    max_potential_clears = -1

    for i in range(8):
        for j in range(8):
            valid = True
            for i1 in range(size[0]):
                for j1 in range(size[1]):
                    if shape.form[i1][j1]:
                        if (i + i1 > 7) or (j + j1 > 7) or grid[i + i1][j + j1]:
                            valid = False
                            break
                if not valid:
                    break

            if valid:
                # Simulate placing the shape here
                temp_grid = [row[:] for row in grid]  # Create a deep copy
                for i1 in range(size[0]):
                    for j1 in range(size[1]):
                        if shape.form[i1][j1]:
                            temp_grid[i + i1][
                                j + j1
                            ] = 1  # Just mark as filled, color doesn't matter

                # Count potential lines cleared
                potential_clears = 0
                for row in range(8):
                    if all(temp_grid[row]):
                        potential_clears += 1

                for col in range(8):
                    if all(temp_grid[row][col] for row in range(8)):
                        potential_clears += 1

                if potential_clears > max_potential_clears:
                    max_potential_clears = potential_clears
                    best_position = (i, j)

    return best_position


def simulate_placement(grid, shape, position):
    """Simulate placing a shape on the grid and return the new grid after clearing lines"""
    if not position or not hasattr(shape, "form") or not shape.form:
        return grid

    # Create a deep copy of the grid
    new_grid = [row[:] for row in grid]

    # Place the shape
    i, j = position
    size = [len(shape.form), len(shape.form[0])]
    for i1 in range(size[0]):
        for j1 in range(size[1]):
            if shape.form[i1][j1]:
                new_grid[i + i1][j + j1] = 1  # Mark as filled

    # Clear completed rows
    rows_to_clear = []
    for row in range(8):
        if all(new_grid[row]):
            rows_to_clear.append(row)

    for row in rows_to_clear:
        for col in range(8):
            new_grid[row][col] = 0

    # Clear completed columns
    cols_to_clear = []
    for col in range(8):
        if all(new_grid[row][col] for row in range(8)):
            cols_to_clear.append(col)

    for col in cols_to_clear:
        for row in range(8):
            new_grid[row][col] = 0

    return new_grid


def generate_shapes(grid):
    """
    Generate three shapes that can each be placed sequentially on the board.
    Each shape can be placed after the previous shape has been placed and any rows/columns cleared.
    """
    from shapes import Shape, forms, colors

    # Make copies to avoid modifying the original
    remaining_forms = [i for i in range(len(forms))]

    next_shapes = [0, 0, 0]  # Initialize with placeholders
    current_grid = [row[:] for row in grid]

    for shape_index in range(3):
        placeable_shape = None
        attempts = 0

        # Try to find a shape that can be placed
        while placeable_shape is None and attempts < 100:
            if not remaining_forms:
                # If we've exhausted all forms, start over
                remaining_forms = [i for i in range(len(forms))]

            # Pick a random form
            form_index = random.choice(remaining_forms)
            remaining_forms.remove(form_index)

            # Try each variant of this form
            for variant_index in range(len(forms[form_index])):
                test_shape = Shape([form_index, variant_index])
                can_place, position = can_place_shape(current_grid, test_shape)

                if can_place:
                    placeable_shape = test_shape
                    # Simulate placing this shape and clearing any lines
                    current_grid = simulate_placement(
                        current_grid, test_shape, position
                    )
                    break

            attempts += 1

        # If we couldn't find a placeable shape after many attempts, use a simple shape
        if placeable_shape is None:
            simple_shapes = [
                [0, 0],  # 2x2 square
                [7, 0],  # 2x1 rectangle
                [8, 0],  # 3x1 rectangle
            ]

            for shape_indices in simple_shapes:
                try:
                    simple_shape = Shape([shape_indices[0], shape_indices[1]])
                    can_place, position = can_place_shape(current_grid, simple_shape)

                    if can_place:
                        placeable_shape = simple_shape
                        current_grid = simulate_placement(
                            current_grid, simple_shape, position
                        )
                        break
                except Exception:
                    continue

        # If we still couldn't find a shape (board is nearly full), create a 1x1 shape
        if placeable_shape is None:
            try:
                # Create a custom 1x1 shape as a last resort
                one_by_one = Shape(-1)  # Using -1 as a special signal
                one_by_one.form = [[1]]
                one_by_one.color = random.choice(colors)
                placeable_shape = one_by_one
            except Exception:
                # If all else fails, keep the placeholder
                continue

        # Update the shape in our list
        next_shapes[shape_index] = placeable_shape

    return next_shapes
