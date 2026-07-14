import turtle

def draw_square(side_length, color):
    """Draws a square with the given side length and color."""
    turtle.color(color)
    turtle.pensize(2)
    turtle.speed(3)  # Moderate speed for visibility

    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)

# Main program
if __name__ == "__main__":
    try:
        # Get side length from user
        side = float(input("Enter the side length of the square (positive number): "))
        if side <= 0:
            raise ValueError("Side length must be positive.")

        # Get color from user
        color = input("Enter the color of the square (e.g., red, blue, green): ").strip().lower()
        if not color:
            raise ValueError("Color cannot be empty.")

        draw_square(side, color)

        turtle.done()  # Keeps the window open until closed manually

    except ValueError as e:
        print(f"Error: {e}")
