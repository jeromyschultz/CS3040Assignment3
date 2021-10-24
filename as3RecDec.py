token = 0
print("Enter a string")
complexInput = input().split()
complexlen = len(complexInput)

def main():
    parse_Plans()


#Returns the next token
def next_token():
    return complexInput[token]

#Advances token forward
def advance():
    if complexInput:
        complexInput.pop(0)

#Returns true if expected matches next_token and prints an error if false
def expected(value):
    if next_token != value:
        print("\'" + value + "\' expected")
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
        parse_Name()
    if expected('with'):
        advance()
    if expected('floors') or expected('floor'):
        advance()
        parse_FloorList()

def parse_FloorList():
    if expected('{'):
        advance()
        parse_FloorReference()
    while next_token() == ',':
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
    if next_token() != 'room' or next_token != 'rooms':
        print("\'room(s)\' expected")
    else:
        advance()
        parse_RoomList()

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
    if not next_token().isalpha():
        print("Name cannot contain non alphebetical numbers")
    elif not next_token().isupper():
        print("Name is expected to be upper case")
    else:
        advance()

def parse_Number():
    if not next_token().isnumeric:
        print("Number Expected")
    else:
        advance()

main()