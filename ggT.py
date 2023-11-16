# numbers all must be from Z

# This was just for a maths exercise
# def modinv(a, m):
#     m0, x0, x1 = m, 0, 1
#     while a > 1:
#         q = a // m
#         m, a = a % m, m
#         x0, x1 = x1 - q * x0, x0
#     return x1 + m0 if x1 < 0 else x1

# def h31bMaths():
#     #Finding the modular inverse of 13 modulo 57
#     b = modinv(13, 57)

#     # Calculating x
#     x = (4 * b) % 57

#     print(x)


def euklid(a, b):
    if b == 0:
        return a
    else:
        return euklid(b, a % b)

def erwEuklid(a, b):
    counter = 0
    if b == 0:
        return (a, 1, 0)
    else:
        ggT, x, y = erwEuklid(b, a % b)
        # print("Current iteration: " + counter)
        #print("This is ggT: " + ggT + "\nThis is x: " + x + "\nThis is y: " + y)
        
        counter += 1
        return (ggT, y, x - (a // b) * y)

def main():
    running = True
    while running:
        whichEuklid = input("What Euklidean Algorithm do you want to execute?\nType n for the normal one, e for the extended one.\nEnter anything else to exit. (n/e) ")
        if whichEuklid == 'n':
            print("You are calling the normal euklidean algorithm.")
            a = int(input("Your a for the normal euklidean algorithm: "))
            b = int(input("Your b for the normal euklidean algorithm: "))
            print(euklid(a, b))
        elif whichEuklid == 'e':
            print("You are calling the extended euklidean algorithm.")
            a = int(input("Your a for the extended euklidean algorithm: "))
            b = int(input("Your b for the extended euklidean algorithm: "))
            print(erwEuklid(a, b))
        else:
            print("You exited.\nYou fool!\nWe had a good thing, you stupid son of a bitch!\nWe had Fring, we had a lab, we had everything we needed, and it all ran like clockwork! "
                  + "You could have shut your mouth, cooked, and made as much money as you ever needed! It was perfect!\nBut no! You just had to blow it up! "
                  + "You, and your pride and your ego! You just had to be the man! If you'd done your job, known your place, we'd all be fine right now!")
            running = False

if __name__ == "__main__":
    main()