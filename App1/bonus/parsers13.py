def parse(feet_inches):
    part = feet_inches.split(" ")
    feet = float(part[0])
    inches = float(part[1])
    return {"feet": feet, "inches": inches}