import sys
import re

token = 0
lineNum = 1

#Reading in data
data = sys.stdin.read()

complexInput = data.split()
complexlen = len(complexInput)

#Regular expression for checking if name
name = re.compile("[A-Z_]+")

def main():
    parse_Plans()

#Returns the next token
def next_token():
    if complexInput:
        return complexInput[token]

#Advances token forward
def advance():
    if complexInput:
        complexInput.pop(0)

def advanceEnd():
    print(complexInput)
    complexInput.clear()

#Returns true if expected matches next_token and prints an error if false
def expected(value):
    if next_token() != value:
        print("\'" + value + "\' expected on line " + str(lineNum))
        advanceEnd()
        return False
    else:
        return True

#Parses plans
def parse_Plans():
    parse_Floor()
    while(next_token() == 'floor'):
        parse_Floor()
    parse_Complex()

#Parses complex
def parse_Complex():
    if expected('complex'):
        advance()
        parse_Building()
    while(next_token() == "building"):
        parse_Building()
#Parses Building
# Buidling data about the floors they contained should be stored for calculate the square footage of buidlings
def parse_Building():
    if expected('building'):
        advance()
        parse_Name()
    if expected('with'):
        advance()
    if next_token() == 'floor' or next_token() == 'floors':
        advance()
        parse_FloorList()
    else:
        print("\'floor(s)\' expected on line " + str(lineNum))

#Parses FloorList
# This should store the list of floors in a building
def parse_FloorList():
    if expected('{'):
        advance()
        parse_FloorReference()
    while next_token() == ',':
        advance()
        parse_FloorReference()
    if expected('}'):
        advance()

#Parses floors references
def parse_FloorReference():
    parse_Name()

def parse_Floor():
    if expected('floor'):
        advance()
        parse_Name()
    if expected('has'):
        advance()
    if next_token() == 'room' or next_token() == 'rooms':
        advance()
        parse_RoomList()
    else:
        print("\'room(s)\' expected on line " + str(lineNum))
        advanceEnd()

#Parse list of rooms
def parse_RoomList():
    if expected('['):
        advance()
        parse_Room()
    while next_token() == ',':
        advance()
        parse_Room()
    if expected(']'):
        advance()
#Parses rooms
# This should store room dimensions to be used in floor square footage calculation
def parse_Room():
    parse_Number()
    if expected('by'):
        advance()
        parse_Number()
#Parses Names
def parse_Name():
    if not name.fullmatch(next_token()):
        print("Name cannot contain non alphebetical numbers")
        advanceEnd()
    else:
        advance()

#Parses Numbers
# Should convert string to number to be used in calculations
def parse_Number():
    if not next_token().isnumeric:
        print("Number Expected")
        advanceEnd()
    else:
        advance()

main()