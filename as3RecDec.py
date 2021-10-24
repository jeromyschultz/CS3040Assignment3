import sys
import re

token = 0
lineNum = 1
data = sys.stdin.read()
complexInput = data.split()
complexlen = len(complexInput)
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

def parse_Plans():
    parse_Floor()
    while(next_token() == 'floor'):
        parse_Floor()
    parse_Complex()

def parse_Complex():
    if expected('complex'):
        advance()
        parse_Building()
    while(next_token() == "building"):
        parse_Building()

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

def parse_FloorList():
    if expected('{'):
        advance()
        parse_FloorReference()
    while next_token() == ',':
        advance()
        parse_FloorReference()
    if expected('}'):
        advance()

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

def parse_RoomList():
    if expected('['):
        advance()
        parse_Room()
    while next_token() == ',':
        advance()
        parse_Room()
    if expected(']'):
        advance()

def parse_Room():
    parse_Number()
    if expected('by'):
        advance()
        parse_Number()

def parse_Name():
    if not name.fullmatch(next_token()):
        print("Name cannot contain non alphebetical numbers")
        advanceEnd()
    elif not next_token().isupper():
        print("Name is expected to be upper case")
        advanceEnd
    else:
        advance()

def parse_Number():
    if not next_token().isnumeric:
        print("Number Expected")
        advanceEnd()
    else:
        advance()

main()