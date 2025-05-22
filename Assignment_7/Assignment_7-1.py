"""
1. Write two lambda functions:
- One to calculate square of a number
- Another to calculate cube of a number

Input: Enter a number : 3
Output: 
Square: 9
Cube: 27
"""
import math

CalSquare = lambda num: math.pow(num,2)
CalCube = lambda num: math.pow(num,3)

CalSquare_X = lambda num:  num*num
CalCube_X = lambda num: num*num*num

def main():
    inputNum = int(input("Enter a number : "))
    
    print("Square > in-build way  : ",int(CalSquare(inputNum)))
    print("Square > regular way   : ",CalSquare_X(inputNum))
    
    print("Cube > in-build way  : ", int(CalCube(inputNum)))
    print("Cube > regular way   : ",CalCube_X(inputNum))

if __name__ == "__main__":
    main()

"""
To calculate cube of num using the below lambda function which uses ** as operator, 
then it gives different output for built-in function and for regular implementation
# CalCube_X = lambda num: num**num

So instead of using above function to calculate cube, use simple way 
it will give exact same output of built-in function
# CalCube_X = lambda num: num*num*num


Output:

vijay@fedora:~/Desktop/Python_Marvellous/Assignment_7$ python Assignment_7-1.py 
Enter a number : 2
Square > in-build way  :  4
Square > regular way   :  4
Cube > in-build way  :  8
Cube > regular way   :  4

vijay@fedora:~/Desktop/Python_Marvellous/Assignment_7$ python Assignment_7-1.py 
Enter a number : 3
Square > in-build way  :  9
Square > regular way   :  9
Cube > in-build way  :  27
Cube > regular way   :  27

vijay@fedora:~/Desktop/Python_Marvellous/Assignment_7$ python Assignment_7-1.py 
Enter a number : 4
Square > in-build way  :  16
Square > regular way   :  16
Cube > in-build way  :  64
Cube > regular way   :  256

vijay@fedora:~/Desktop/Python_Marvellous/Assignment_7$ python Assignment_7-1.py 
Enter a number : 5
Square > in-build way  :  25
Square > regular way   :  25
Cube > in-build way  :  125
Cube > regular way   :  3125

vijay@fedora:~/Desktop/Python_Marvellous/Assignment_7$ python Assignment_7-1.py 
Enter a number : 6
Square > in-build way  :  36
Square > regular way   :  36
Cube > in-build way  :  216
Cube > regular way   :  46656

"""