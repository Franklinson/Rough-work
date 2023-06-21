# ask the user to input their name and assign it to a variable name
#name = input ('What is your name ')

#print('Hello ', name )

#num1, num2 = input("Enter 2 numbers: ").split()

#num1 = int(num1)
#num2 = int(num2)

#sum = num1 + num2
#print("The sum of the numbers are {} + {} = {}".format(num1, num2, sum))


#Problem: Receive miles and convert to kilometers

Number = input("Enter Miles ")
Number = int(Number)

Kilometers = Number * 1.60934

print("{} equals {} kilometers".format(Number, Kilometers))

Age = eval(input("Enter age "))
if Age < 5:
    print("Yoo young for School")

elif Age == 5:
    print("Go to Kingetgarteb")

elif (Age > 5) and (Age <= 17):
    grade = Age -5
    print("Go to {} grade".format(grade))

else:
    print("Go to College")
