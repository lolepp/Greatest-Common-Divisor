# Script that describes the greatest common divisor algorithm and the extended one in a comfortable loop.
# Numbers all must be whole numbers but will anyway be converted to int.
# This was originally just for a maths exercise.

def euklid(a, b):
    if b == 0:
        return a
    else:
        return euklid(b, a % b)

def extEuklid(a, b):
    # Special counter if you need to know on which iteration you are.
    # counter = 0
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x, y = extEuklid(b, a % b)
        # print("Current iteration: " + counter)
        # counter += 1
        # print("This is gcd: " + gcd + "\nThis is x: " + x + "\nThis is y: " + y)
        return (gcd, y, x - (a // b) * y)

def main():
    running = True
    while running:
        whichEuklid = input("What Euklidean Algorithm do you want to execute?\nType n for the normal one, e for the extended one.\nEnter anything else to exit. (n/e/...) ")
        if whichEuklid == 'n' or 'N':
            print("You are calling the normal euklidean algorithm.")
            a = int(input("Your a for the normal euklidean algorithm: "))
            b = int(input("Your b for the normal euklidean algorithm: "))
            print(euklid(a, b))
        elif whichEuklid == 'e' or 'E':
            print("You are calling the extended euklidean algorithm.")
            a = int(input("Your a for the extended euklidean algorithm: "))
            b = int(input("Your b for the extended euklidean algorithm: "))
            print(extEuklid(a, b))
        else:
            print("You exited.\nYou fool!\nWe had a good thing, you stupid son of a bitch!\nWe had Fring, we had a lab, we had everything we needed, "
                  + "and it all ran like clockwork! You could have shut your mouth, cooked, and made as much money as you ever needed! It was perfect!\n"
                  + "But no! You just had to blow it up! You, and your pride and your ego! You just had to be the man! If you'd done your job, "
                  + "known your place, we'd all be fine right now!")
            running = False

if __name__ == "__main__":
    main()