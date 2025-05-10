def main():
    print(range(5))         # range(0, 5)
    print(type(range(5)))   # <class 'range'>
    print(list(range(5)))   # [0, 1, 2, 3, 4]
    print(list(range(2,6))) # [2, 3, 4, 5]
    print(list(range(2,10,2))) # [2, 4, 6, 8]
    print(list(range(10,5,-1))) # [10, 9, 8, 7, 6]
    
if __name__ == "__main__":
    main()