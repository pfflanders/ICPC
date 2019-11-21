number, digits = input().split()
digits = int(digits)
number = number + number[(len(number)-digits):] + number[(len(number)-digits):] + number[(len(number)-digits):] + number[(len(number)-digits):] + number[(len(number)-digits):] + number[(len(number)-digits):]
number = float(number)
x = 1
y = 10000
while float(x/y) != float(number):
    if x / y > number:
        y += 1
    else:
        x += 1

for i in range(y):
    if x%i == 0 and y%i == 0:
        x/=i
print(str(int(x)) + '/' + str(int(y)))
