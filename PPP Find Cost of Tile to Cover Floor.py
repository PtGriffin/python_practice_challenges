"""6. **Find Cost of Tile to Cover W x H Floor** - Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user."""

def AreaFloor(x, y):
    width = x
    height = y
    area = float(width*height)

    cost = float(input("What is the cost of the floor per square foot? " ))
    assert type(cost) == float

    floorCost = area/cost
    report = "$"+str(floorCost)

    return(report)

print(AreaFloor(10,50))
