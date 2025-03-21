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
    [  # shape 1 - 2x2 square
        [
            [1, 1],
            [1, 1]
        ]
    ],
    [  # shape 2 - 3x2 rectangle
        [
            [1, 1, 1],
            [1, 1, 1]
        ],
        [
            [1, 1],
            [1, 1],
            [1, 1]
        ]
    ],
    [  # shape 3 - 3x3 square
        [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
    ],
    [  # shape 4 - L shape (3 length)
        [
            [1, 1, 1],
            [1, 0, 0],
            [1, 0, 0]
        ],
        [
            [1, 1, 1],
            [0, 0, 1],
            [0, 0, 1]
        ],
        [
            [1, 0, 0],
            [1, 0, 0],
            [1, 1, 1]
        ],
        [
            [0, 0, 1],
            [0, 0, 1],
            [1, 1, 1]
        ],
    ],
    [  # shape 5 - L (2 with 3 length)
        [
            [1, 1, 1],
            [1, 0, 0]
        ],
        [
            [1, 1, 1],
            [0, 0, 1]
        ],
        [
            [0, 0, 1],
            [1, 1, 1]
        ],
        [
            [1, 0, 0],
            [1, 1, 1]
        ],
        [
            [1, 0],
            [1, 0],
            [1, 1]
        ],
        [
            [0, 1],
            [0, 1],
            [1, 1]
        ],
        [
            [1, 1],
            [0, 1],
            [0, 1]
        ],
        [
            [1, 1],
            [1, 0],
            [1, 0]
        ],
    ],
    [  # shape 6 - Z shape
        [
            [0, 1, 1],
            [1, 1, 0]
        ],
        [
            [1, 1, 0],
            [0, 1, 1]
        ],
        [
            [1, 0],
            [1, 1],
            [0, 1]
        ],
        [
            [0, 1],
            [1, 1],
            [1, 0]],
    ],
    [  # shape 7 - T shape
        [
            [0, 1, 0],
            [1, 1, 1]
        ],
        [
            [1, 0],
            [1, 1],
            [1, 0]
        ],
        [
            [1, 1, 1],
            [0, 1, 0]
        ],
        [
            [0, 1],
            [1, 1],
            [0, 1]
        ],
    ],
    [  # shape 8 - 2x1 rectangle
        [
            [1, 1]
        ],
        [
            [1],
            [1]
        ]
    ],
    [  # shape 9 - 3x1 rectangle
        [
            [1, 1, 1]
        ],
        [
            [1],
            [1],
            [1]
        ]
    ],
    [  # shape 10 - S shape
        [
            [1, 0],
            [1, 1]
        ],
        [
            [1, 1],
            [0, 1]
        ],
        [
            [1, 1],
            [1, 0]
        ],
        [
            [0, 1],
            [1, 1]
        ],
    ],
    [  # shape 11 - 4x1 rectangle
        [
            [1, 1, 1, 1]
        ],
        [
            [1],
            [1],
            [1],
            [1]
        ]
    ],
    [  # shape 12 - 5x1 rectangle
        [
            [1, 1, 1, 1, 1]
        ],
        [
            [1],
            [1],
            [1],
            [1],
            [1]
        ]
    ],
]


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
    """Generate three random shapes with uniform probability"""
    next_shapes = []

    # Try to generate 3 unique shapes
    while len(next_shapes) < 3:
        try:
            # Simply choose a random shape index (uniform probability)
            form_index = random.randint(0, len(forms) - 1)

            # Choose a random variant of that shape
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
