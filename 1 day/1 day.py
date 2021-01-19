#print(os.path.exists("D:/AdventOfCode/1 day/ numbers.txt"))

data = open("D:/AdventOfCode/1 day/numbers.txt").read().strip().split("\n")

data = [int(x) for x in data if int(x) < 2020]

total = 0

def _2020(data):
    for i in data:
        total = 0
        for j in data:
            total = i + j
            if total > 2020:
                total = 0
            elif total == 2020:
                return i * j
    return 0
    

print(_2020(data))