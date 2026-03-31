def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    # Bug: typo in variable name
    return lenght * width

def main():
    """Main function to test the calculator."""
    length = 10
    width = 5
    area = calculate_area(length, width)
    print(f"Area: {area}")

if __name__ == "__main__":
    main()
