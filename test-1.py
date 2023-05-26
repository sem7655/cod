x = int(input())
y = int(input())
p = int(input())
years = 0
while x<y:
    x = int (x * (1+p / 100))
    years=years+1
print(years)
