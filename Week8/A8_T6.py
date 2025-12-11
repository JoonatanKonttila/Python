import svgwrite
from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle

def drawSquare(PDwg: Drawing) -> None:
    print("Insert square")
    x = int(input("- Left edge position: "))
    y = int(input("- Top edge position: "))
    side = int(input("- Side length: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    PDwg.add(Rect(insert=(x, y), size=(side, side), fill=fill, stroke=stroke))
    print()

def drawCircle(PDwg: Drawing) -> None:
    print("Insert circle")
    cx = int(input("- Center X position: "))
    cy = int(input("- Center Y position: "))
    radius = int(input("- Radius: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    PDwg.add(Circle(center=(cx, cy), r=radius, fill=fill, stroke=stroke))
    print()

def saveSvg(PDwg: Drawing) -> None:
    filename = input("Insert filename: ")
    print(f'Saving file to "{filename}"')
    proceed = input("Proceed (y/n)?: ")
    if proceed.lower() == 'y':
        PDwg.save(filename)
        print("Vector saved successfully!\n")
    return None


def showMenu() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Save svg")
    print("0 - Exit")

def main() -> None:
    print("Program starting.\n")
    Dwg = svgwrite.Drawing()
    while True:
        showMenu()
        choice = input("Your choice: ").strip()
        print()
        if choice == "0":
            print("Exiting program.\n")
            break
        elif choice == "1":
            drawSquare(Dwg)
        elif choice == "2":
            drawCircle(Dwg)
        elif choice == "3":
            saveSvg(Dwg)
        else:
            print("Unknown option! Try again.\n")
    print("Program ending.")

if __name__ == "__main__":
    main()
