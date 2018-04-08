import sys

print ("1: Brian")
print("2: Alex")
print("3: Solomon")
print("4: Dylan")
print("5: Teddy")
print("6: Jackie")
print("7: Boghossian")
print("8: Bough")

names = ["Brian", "Alex", "Solomon", "Dylan", "Teddy", "Jackie", "Boghossian", "Bough"]

id = raw_input("Enter your ID number: ")
print ( id )

f = open("choices_" + id, "w")

print("Please rank the above people from 1 to 7. Please give yourself 0.")

check = [False, False, False, False, False, False, False, False]

def errorCheck(num):
    if ( num < 0 or num > 7):
        print("you fucked up")
        sys.exit(0)

for name in names:
    s = int(raw_input(name + ": "))
    if ( check[s] ):
        print("you fucked up")
        sys.exit(0)
    check[s] = True
    errorCheck(s)
    f.write("" + str(s) + "\n")
