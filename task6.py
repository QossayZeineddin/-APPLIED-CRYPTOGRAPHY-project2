import random as rd

char = '1234567890ABCDEF'  # 16 bytes
string = ''
length = 32

for i in range(0, length):
    string += rd.choice(char)

print("The IV created is: ")    
print(string)