# Data Structure using Python
# Linked List

class Node:
    def __init__(self, No):
        self.Data = No
        self.Next = None

class SingleLL:
    def __init__(self):
        self.First = None
        self.iCount = 0
    
    def InsertFirst(self, No):
        newn = Node(No)
        if(self.First == None):  # LL is empty
            self.First = newn
        else:                   # LL Contains at least one node
            newn.Next = self.First
            self.First = newn
        self.iCount = self.iCount + 1
    
    def InsertLast(self, No):
        newn = Node(No)
        if(self.First == None):  # LL is empty
            self.First = newn
        else:                   # LL Contains at least one node
            temp = self.First
            while(temp.Next != None):
                temp = temp.Next
            temp.Next = newn
            
        self.iCount = self.iCount + 1


    def Display(self):
        temp = self.First
        while(temp != None):
            print(f"[ {temp.Data} ]-->", end="")
            temp = temp.Next
        print("None")

    def Count(self):
        return self.iCount
    
    def DeleteFirst(self):
        if(self.First == None):
            return
        else:
            temp = self.First
            self.First = self.First.Next
            del temp
            self.iCount = self.iCount - 1

def main():
    print("Demonstration of Singly Linear Linked List")

    sobj = SingleLL()

    # Insert calls
    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)

    sobj.Display()
    iRet = sobj.Count()
    print(f"Number of nodes in LL are : {iRet}")


    sobj.InsertLast(101)
    sobj.InsertLast(111)
    sobj.InsertLast(121)
    
    sobj.Display()
    iRet = sobj.Count()
    print(f"Number of nodes in LL are : {iRet}")

    # Delete calls
    sobj.DeleteFirst()

    sobj.Display()
    iRet = sobj.Count()
    print(f"Number of nodes in LL are : {iRet}")

if __name__ == "__main__":
    main()