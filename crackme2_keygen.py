
username = []
firstPart = []
secondPart = []
x = 0
username = input("Enter username: ")
if(len(username)< 5 or len(username) > 9):
    print("username cannot be less than 4 characters or greater than 9 characters !")
    exit()
#the number to shift the second part of the password    
shiftNumber = len(username) - 1 

for chars in username:
    # increment the ascii characters
    char = int(ord(chars)) + x  
    # append the character to firstPart
    firstPart.append(chr(char))  
    x = x + 1
# reverse the obtained firstPart
rev = list(reversed(firstPart)) 
# the final form of the firstPart
firstPart = ''.join(rev)   
#generate the second part by shifting character in the end of the username 
reversedUsername = list(reversed(username))
#slice username to take only needed charcaters to complete 10 characters password.
for chars in reversedUsername[:10 - len(username)]:
    char = int(ord(chars)) +  shiftNumber
    secondPart.append(chr(char))

print("The password is " + "[" + firstPart + str(''.join(secondPart)) + "]")
