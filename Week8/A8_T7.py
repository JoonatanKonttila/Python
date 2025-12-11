from svgwrite import Drawing, cm
from svgwrite.shapes import Rect, Circle, Polygon
import math

def drawSquare(PDwg: Drawing) -> None:
    print("Insert square")
    x = int(input("- Left edge position: "))
    y = int(input("- Top edge position: "))
    side = int(input("- Side length: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    PDwg.add(Rect(insert=(x, y), size=(side, side), fill=fill, stroke=stroke))
    return None

def drawCircle(PDwg: Drawing) -> None:
    print("Insert circle")
    cx = int(input("- Center X: "))
    cy = int(input("- Center Y: "))
    radius = int(input("- Radius: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    PDwg.add(Circle(center=(cx, cy), r=radius, fill=fill, stroke=stroke))
    return None

def drawHexagon(PDwg: Drawing) -> None:
    print("Insert hexagon details:")
    cx = int(input("Middle point X: "))
    cy = int(input("Middle point Y: "))
    apothem = float(input("Apothem length: "))
    fill = input("Insert fill: ")
    stroke = input("Insert stroke: ")
    radius = apothem / math.cos(math.radians(30))
    points = []
    for i in range(6):
        angle_deg = 30 + i * 60
        angle_rad = math.radians(angle_deg)
        x = round(cx + radius * math.cos(angle_rad))
        y = round(cy - radius * math.sin(angle_rad))
        points.append((x, y))
    PDwg.add(Polygon(points=points, fill=fill, stroke=stroke))
    return None

def saveSvg(PDwg: Drawing) -> None:
    filename = input("Insert filename: ")
    print(f'Saving file to "{filename}"')
    proceed = input("Proceed (y/n)?: ")
    if proceed.lower() == 'y':
        PDwg.save(filename)
        print("Vector saved successfully!")
    return None

def showMenu() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Draw hexagon")
    print("4 - Save svg")
    print("0 - Exit")

def main() -> None:
    print("Program starting.")
    Dwg = Drawing()
    while True:
        showMenu()
        choice = input("Your choice: ")
        if choice == "1":
            drawSquare(Dwg)
        elif choice == "2":
            drawCircle(Dwg)
        elif choice == "3":
            drawHexagon(Dwg)
        elif choice == "4":
            saveSvg(Dwg)
        elif choice == "0":
            print("Exiting program.")
            break
    print("\nProgram ending.")

if __name__ == "__main__":
    main()
