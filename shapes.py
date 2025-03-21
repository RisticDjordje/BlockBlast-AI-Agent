import random

# Define colors for the shapes
colors = [
    (255, 191, 0),  # Yellow
    (255, 143, 0),  # Orange
    (252, 48, 28),  # Red
    (112, 199, 48),  # Green
    (62, 181, 208),  # Light Blue
    (35, 64, 143),  # Dark Blue
]

# Define shape forms
forms = [
    [[[1, 1], [1, 1]]],  # shape 1 - 2x2 square
    [[[1, 1, 1], [1, 1, 1]], [[1, 1], [1, 1], [1, 1]]],  # shape 2
    [[[1, 1, 1], [1, 1, 1], [1, 1, 1]]],  # shape 3
    [
        [[1, 1, 1], [1, 0, 0], [1, 0, 0]],  # shape 4
        [[1, 1, 1], [0, 0, 1], [0, 0, 1]],
        [[1, 0, 0], [1, 0, 0], [1, 1, 1]],
        [[0, 0, 1], [0, 0, 1], [1, 1, 1]],
    ],
    [
        [[1, 1, 1], [1, 0, 0]],  # shape 5
        [[1, 1, 1], [0, 0, 1]],
        [[0, 0, 1], [1, 1, 1]],
        [[1, 0, 0], [1, 1, 1]],
        [[1, 0], [1, 0], [1, 1]],
        [[0, 1], [0, 1], [1, 1]],
        [[1, 1], [0, 1], [0, 1]],
        [[1, 1], [1, 0], [1, 0]],
    ],
    [
        [[0, 1, 1], [1, 1, 0]],  # shape 6
        [[1, 1, 0], [0, 1, 1]],
        [[1, 0], [1, 1], [0, 1]],
        [[0, 1], [1, 1], [1, 0]],
    ],
    [
        [[0, 1, 0], [1, 1, 1]],  # shape 7
        [[1, 1, 1], [0, 1, 0]],
        [[1, 0], [1, 1], [1, 0]],
        [[0, 1], [1, 1], [0, 1]],
    ],
    [[[1, 1]], [[1], [1]]],  # shape 8 - 2x1 rectangle
    [[[1, 1, 1]], [[1], [1], [1]]],  # shape 9 - 3x1 rectangle
    [
        [[1, 0], [1, 1]],  # shape 10
        [[1, 1], [0, 1]],
        [[1, 1], [1, 0]],
        [[0, 1], [1, 1]],
    ],
    [[[1, 1, 1, 1]], [[1], [1], [1], [1]]],  # shape 11 - 4x1 rectangle
    [[[1, 1, 1, 1, 1]], [[1], [1], [1], [1], [1]]],  # shape 12 - 5x1 rectangle
]

# Probability array for choosing shapes
probs = [0, 127, 202, 242, 307, 434, 561, 688, 815, 942, 1069, 1144, 1200]


class Shape:
    def __init__(self, form):
        try:
            if form != -1:
                self.form = forms[form[0]][form[1]]
            else:
                # Handle special case for 1x1 shape
                self.form = [[1]]

            self.color = random.choice(colors)
        except Exception:
            # Fallback to ensure we always have a valid shape
            self.form = [[1]]
            self.color = random.choice(colors)


def generate_shapes():
    """Generate three random shapes"""
    next_shapes = []

    # Try to generate 3 unique shapes
    while len(next_shapes) < 3:
        try:
            r_int = random.randint(0, 1199)
            form_index = None

            # Find which form index this random number corresponds to
            for i in range(12):
                if probs[i] <= r_int < probs[i + 1]:
                    form_index = i
                    break

            if form_index is not None:
                variant_index = random.randint(0, len(forms[form_index]) - 1)
                current = Shape([form_index, variant_index])

                # Check if this shape is already in our list (avoid duplicates)
                valid = True
                for existing_shape in next_shapes:
                    if (
                        hasattr(existing_shape, "form")
                        and existing_shape.form == current.form
                    ):
                        valid = False
                        break

                if valid:
                    next_shapes.append(current)
        except Exception:
            # If we encounter any error, add a simple 1x1 shape as fallback
            fallback = Shape(-1)
            next_shapes.append(fallback)

    return next_shapes
