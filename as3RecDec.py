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
    complexInput.pop(0)

def parse_Plans():
    parse_Floor()
    while(next_token() == 'floor'):
        parse_Floor()
    parse_Complex()

def parse_Complex():
    return None

def parse_Building():
    return None

def parse_FloorList():
    return None

def parse_FloorReference():
    return None

def parse_Floor():
    if(next_token() != 'floor'):
        print("\'floor\' expected")
    else:
        advance()
    parse_Name()
    if(next_token() != 'has'):
        print("\'has\' expected")
    else:
        advance()
    if(next_token() != 'room' or next_token != 'rooms'):
        print("\'room(s)\' expected")
    else:
        advance()
    parse_RoomList()

def parse_RoomList():
    if(next_token() != '['):
        print("\'[\' expected")
    else:
        advance()
        parse_Room()
    while(next_token() == ','):
        advance()
        parse_Room()
    if(next_token() != ']'):
        print("\']\' expected")
    else:
        advance()

def parse_Room():
    parse_Number()
    if(next_token() != 'by'):
        print("\'by\' expected")
    else:
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