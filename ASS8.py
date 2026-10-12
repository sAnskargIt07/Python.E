import math

def calculate_area(shape, **kwargs):

    if shape == "circle":
        radius = kwargs.get("radius")

        if radius is not None:
            return math.pi * radius ** 2
        else:
            raise ValueError("Radius is required for circle")

    elif shape == "rectangle":
        width = kwargs.get("width")
        height = kwargs.get("height")

        if width is not None and height is not None:
            return width * height
        else:
            raise ValueError("Width and height are required for rectangle")

    elif shape == "triangle":
        base = kwargs.get("base")
        height = kwargs.get("height")

        if base is not None and height is not None:
            return 0.5 * base * height
        else:
            raise ValueError("Base and height are required for triangle")

    else:
        raise ValueError("Unsupported shape type")


# Example usage

try:
    circle_area = calculate_area("circle", radius=5)
    print(f"Area of the circle: {circle_area}")

    rectangle_area = calculate_area("rectangle", width=4, height=6)
    print(f"Area of the rectangle: {rectangle_area}")

    triangle_area = calculate_area("triangle", base=3, height=4)
    print(f"Area of the triangle: {triangle_area}")

except ValueError as e:
    print(e)