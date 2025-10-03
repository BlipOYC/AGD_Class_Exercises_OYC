from string import ascii_lowercase

def code(p_message, p_shift):
    try:
        p_message = p_message.lower()
    except AttributeError:
        raise TypeError("The message must be a string.")
    if not isinstance(p_shift, int):
        raise TypeError("The shift must be an int.")
    codedMessage = ""
    for char in p_message:
        if char in ascii_lowercase:
            num = ord(char)
            num += p_shift
            if num > ord("z"):
                num -= 26
            elif num < ord("a"):
                num += 26
            char = chr(num)
            codedMessage += char
        else:
            codedMessage += char
    return codedMessage

#Main
#shift = 3
#msg = input("Enter your message: ")
#codedMessage = code(msg, shift)
#print(f"The coded message is {codedMessage}")