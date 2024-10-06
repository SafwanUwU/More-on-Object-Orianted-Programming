class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return 3.1416 * self.radius ** 2  # Using an approximation for pi

    def perimeter(self):
        return 2 * 3.1416 * self.radius  # Using an approximation for pi

radius = float(input("Enter Radius: "))
NewCircle = Circle(radius)

print(f"Area: {NewCircle.area()}")
print(f"Perimeter: {NewCircle.perimeter()}")
