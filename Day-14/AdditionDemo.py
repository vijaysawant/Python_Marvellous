# Positive Scenario - 1
# python AdditionDemo.py < AdditionDemo_Input.txt > AdditionDemo_Outout.txt 2> AdditionDemo_Error.txt

# Negative Scenario - 2
# cat AdditionDemo_Input.tx =>  '10 20'
# python AdditionDemo.py < AdditionDemo_Input.txt > AdditionDemo_Outout.txt 2> AdditionDemo_Error.txt

no1 = int(input())
no2 = int(input())

ans = no1 + no2

print("Addition is : ",ans)


"""
$ python AdditionDemo.py < AdditionDemo_Input.txt > AdditionDemo_Outout.txt
$ python AdditionDemo.py < AdditionDemo_Input.txt > AdditionDemo_Outout.txt 2> AdditionDemo_Error.txt
$ python AdditionDemo.py < AdditionDemo_Input.txt > AdditionDemo_Outout.txt 2> AdditionDemo_Error.txt
$ python AdditionDemo.py < AdditionDemo_Input.txt > AdditionDemo_Outout.txt 2>> AdditionDemo_Error.txt
$ python AdditionDemo.py < AdditionDemo_Input.txt >> AdditionDemo_Outout.txt 2> AdditionDemo_Error.txt
"""