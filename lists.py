numbers = [1,2,3,4,5]
for count in numbers:
    print(count)
sum = sum(numbers)
print("the sum is: ", sum)
max = max(numbers)
print("the max is: ", max)

squares = [x**2 for x in range(1,10)]
print("the square of 10 numbers are: ", squares)

oddnumbers = [x for x in range (1,100) if  x%2 !=0]
print ("odd numbers are: ", oddnumbers)
