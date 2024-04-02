#Returns the appropriate description string based on which token type is being referenced.

def colorAlign(i):
    match i:
        case 0 | "E":
            return "Emerald (Green)"
        case 1 | "D":
            return "Diamond (White)"
        case 2 | "S":
            return "Sapphire (Blue)"
        case 3 | "O":
            return "Onyx (Black)   "
        case 4 | "R":
            return "Ruby (Red)     "
        case 5 | "G":
            return "Gold (Yellow)  "
        case _ :
            return "Error: Invalid Input."