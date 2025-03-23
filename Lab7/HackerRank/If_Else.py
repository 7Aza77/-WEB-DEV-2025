n = int(input("Enter your number: "))

if ((n %2 ==  0) and n>20 ) or ((n>=2 and n<=5) and (n%2 == 0)):
    print("Not Weird")

elif (n % 2 != 0) or ((n >= 6 or n<= 20) and (n%2 == 0)):
    print("Weird")
