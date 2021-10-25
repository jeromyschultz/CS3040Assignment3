import sys
import re

token = 0
lineNum = 1

# Reading in data
data = sys.stdin.read()

complexInput = data.split()
complexlen = len(complexInput)

# Regular expression for checking if name
name = re.compile("[A-Z_]+")

buildingNumber = 'A'
listRooms = []
listBuilding = []


def main():
    parse_Plans()
    print_SF()


# Returns the next token
def next_token():
    if complexInput:
        return complexInput[token]


# Advances token forward
def advance():
    if complexInput:
        complexInput.pop(0)


def advanceEnd():
    print(complexInput)
    complexInput.clear()


# Returns true if expected matches next_token and prints an error if false
def expected(value):
    if next_token() != value:
        print("\'" + value + "\' expected on line " + str(lineNum))
        advanceEnd()
        return False
    else:
        return True


# Parses plans
def parse_Plans():
    listRooms.append(parse_Floor())
    while next_token() == 'floor':
        listRooms.append(parse_Floor())
    parse_Complex()


# Parses complex
def parse_Complex():
    if expected('complex'):
        advance()
        parse_Building()
    while next_token() == "building":
        parse_Building()


# Parses Building
# Buidling data about the floors they contained should be stored for calculate the square footage of buidlings
def parse_Building():
    if expected('building'):
        advance()
        global buildingNumber
        buildingNumber = parse_Name()
    if expected('with'):
        advance()
    if next_token() == 'floor' or next_token() == 'floors':
        advance()
        parse_FloorList()
    else:
        print("\'floor(s)\' expected on line " + str(lineNum))



# Parses FloorList
# This should store the list of floors in a building
def parse_FloorList():
    if expected('{'):
        advance()
        listBuilding.append((buildingNumber, parse_FloorReference()))
    while next_token() == ',':
        advance()
        listBuilding.append((buildingNumber, parse_FloorReference()))
    if expected('}'):
        advance()


# Parses floors references
def parse_FloorReference():
    return parse_Name()


def parse_Floor():
    floorFootage = 0
    floorName = ""
    if expected('floor'):
        advance()
        floorName = parse_Name()
    if expected('has'):
        advance()
    if next_token() == 'room' or next_token() == 'rooms':
        advance()
        floorFootage = parse_RoomList()
    else:
        print("\'room(s)\' expected on line " + str(lineNum))
        advanceEnd()

    return floorName, floorFootage


# Parse list of rooms
def parse_RoomList():
    totalFootage = 0
    if expected('['):
        advance()
        totalFootage += parse_Room()
    while next_token() == ',':
        advance()
        totalFootage += parse_Room()
    if expected(']'):
        advance()
    return totalFootage


# Parses rooms
# This should store room dimensions to be used in floor square footage calculation
def parse_Room():
    footage = parse_Number()
    if expected('by'):
        advance()
        footage *= parse_Number()
    return footage


# Parses Names
def parse_Name():
    value = next_token()
    if not name.fullmatch(next_token()):
        print("Name cannot contain non alphabetical numbers")
        advanceEnd()
        return ""
    else:
        advance()
    return value


# Parses Numbers
# Should convert string to number to be used in calculations
def parse_Number():
    if not next_token().isnumeric:
        print("Number Expected")
        advanceEnd()
        return 0
    else:
        value = int(next_token())
        advance()
        return value


def print_SF():
    sf = dict()
    for building in listBuilding:
        if building[0] not in sf.keys():
            sf[building[0]] = 0

    for b in listBuilding:
        sf[b[0]] += getSFByRoom(b[1])

    for key in sf:
        print(" Area for building " + key + ": " + str(sf[key]) + " square feet.")


def getSFByRoom(room):
    for r in listRooms:
        if room == r[0]:
            return r[1]

    #Error - room doesn't exist
    print("Invalid reference to room " + room)
    quit()


main()
