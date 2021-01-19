#import os.path

#print(os.path.exists("D:/AdventOfCode/2 day/passwords.txt"))

fn = open("D:/AdventOfCode/2 day/passwords.txt").read().strip().split("\n")

data = [x for x in fn]
#print(len(data))

valid_pass = 0


# THE FIRST PART
#for x in data:
#    str = x.replace("-"," ").split()
#    let = str[2][0]
#    password = str[3]
#    min = int(str[0])
#    max = int(str[1])
#    if password.count(let) >= min and password.count(let) <= max:
#        valid_pass += 1

# THE SECOND PART
#data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

for x in data:
    str = x.replace("-"," ").split()
    let = str[2][0]
    password = str[3]
    min = int(str[0])-1
    max = int(str[1])-1
    if (password[min] == let and password[max] != let) or (password[min] != let and password[max] == let):
        print(password)
        valid_pass += 1

print(valid_pass)
