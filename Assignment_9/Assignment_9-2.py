"""
2. Write a Python program using multiprocessing. Process to square a list of numbers using mulitple 
processes.
"""
import multiprocessing

def makeSquare(inputList):
    sqr = 1
    for num in inputList:
        sqr = num**2
        print(f"Square of {num} is {sqr}")

def main():
    inputList = [1,2,3,4,5,6,7,8,9]
    process1 = multiprocessing.Process(target=makeSquare, args=(inputList,))
    process1.start()
    process1.join()

if __name__ == "__main__":
    main()