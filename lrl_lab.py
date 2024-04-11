# Lawson Loryea
def encoder(input):
    input = str(input)
    string = ""
    for i in input:
        y = int(i)
        y = y + 3
        string = string + str(y)
    return string

def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        choice = int(input("Please enter an option: "))
        if choice == 1:
            z = int(input("Please enter your password to encode: "))
            Encoded_Password = encoder(z)
            print("Your password has been encoded and stored!")
        if choice == 2:
            print("The encoded password is", Encoded_Password +"," + "and the original password is", Decoded_Password)
        if choice == 3:
            break











if __name__ == "__main__":
    main()

