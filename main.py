def StrongNumber(x):
    sum = 0
    for i in str(x):
        fact = 1
        for j in range(1,int(i)+1):
            fact = fact*int(j)
        sum = sum + fact
    return sum
number = int(input("Enter a number : "))
if number == StrongNumber(number):
    print(f"{number} is a strong number")
else:
    print(f"{number} is not an strong number")
