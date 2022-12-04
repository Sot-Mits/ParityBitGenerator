print("Python")
print("This program prints a parity bit on a binary 7-bit integer")
print("Even (0) or Odd (1) Parity Method?")

parityMethod = -1
#Choosing parity method & vaildating
while True:
    try:
        parityMethod = int(input())
        if (parityMethod == 1):
            print("You have chosen an odd parity method")
            break
        elif (parityMethod == 0):
            print("You have chosen an even parity method")
            break
        else:
            print("Please enter 0 or 1")
    except:
        parityMethod = -1
        print("Please enter an integer")


userInput =  (-1)
#Choosing data & validating
while True:
    print("Please enter 7 bits")
    try:
        userInput = str(input())

        #Checking Length
        legalLength = 0
        if len(userInput) == 7:
            legalLength = 1
        
        #Checking Input
        legalInput = 0
        if ((('0' in userInput) == True) or (('1' in userInput) == True)):
            legalInput = 1
            print(legalInput)
    
        #Evaluating
        if ((legalLength == 1) and (legalInput == 1)):
            print("You have entered 7 bits")
            break
    
        elif ((legalLength == 1) and (legalInput == 0)):
            print("You have entered 7 characters, but they're not bits")
            
        elif ((legalLength == 0) and (legalInput == 1)):
            print("You have entered an incorrect amount of bits")
        
        elif ((legalLength == 0) and (legalInput == 0)):
            print("You have entered neither 7 characters, nor bits")
    
    except:
        print("Please enter 7 bits")

#Generating Parity Bit
numberOfOnes = 0
for bit in userInput:
    if (bit == 1):
        numberOfOnes += 1
parityBit = (((numberOfOnes % 2) + parityMethod) % 2)

#Printing
transmittedByte = userInput + str(parityBit)
print("Transmitted byte will be " + transmittedByte)