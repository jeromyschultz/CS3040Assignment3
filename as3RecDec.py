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
    for x in range(complexlen):
        print(next_token())
        advance()

def parse_Complex():
    return None

def parse_Building():
    return None

def parse_FloorList():
    return None

def parse_FloorReference():
    return None

def parse_Floor():
    return None

def parse_RoomList():
    return None

def parse_Room():
    return None

def parse_Name(expected):
    if next_token == expected:
        advance()
    else:
        print("Expected \"" + expected + "\" on line ")

def parse_Number():
    if next_token().isnumeric:
        advance()
    else:
        print("Number Expected")

main()