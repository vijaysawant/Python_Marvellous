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

    def InsertAtPosition(self, No, iPos):
        if (iPos < 1 or iPos > self.iCount+1):
            print("Invali position")
            return
        if iPos == 1:
            self.InsertFirst(No)
        elif iPos == self.iCount+1:
            self.InsertLast(No)
        else:
            newn = Node(No)
            temp = self.First
            for i in range(1, iPos-1, 1):
                temp = temp.Next
            
            newn.Next = temp.Next
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
    
    def DeleteLast(self):
        if(self.First == None):             # LL is empty
            return
        elif (self.First.Next == None):     # LL contains one Node
            del self.First
            self.First = None
        else:                               # LL contains more than one Node
            temp = self.First
            while(temp.Next.Next != None):
                temp = temp.Next
            del temp.Next

            temp.Next = None
            self.iCount = self.iCount - 1

def main():
    print("Demonstration of Singly Linear Linked List")

    sobj = SingleLL()

    # Insert calls
    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)

    # sobj.Display()
    # iRet = sobj.Count()
    # print(f"Number of nodes in LL are : {iRet}")


    sobj.InsertLast(101)
    sobj.InsertLast(111)
    sobj.InsertLast(121)
    
    sobj.Display()
    iRet = sobj.Count()
    print(f"Number of nodes in LL are : {iRet}")

    # # Delete calls
    # sobj.DeleteFirst()

    # sobj.Display()
    # iRet = sobj.Count()
    # print(f"Number of nodes in LL are : {iRet}")

    # sobj.DeleteLast()
    # sobj.Display()
    # iRet = sobj.Count()
    # print(f"Number of nodes in LL are : {iRet}")

    sobj.InsertAtPosition(No=105, iPos=5)
    sobj.Display()
    iRet = sobj.Count()
    print(f"Number of nodes in LL are : {iRet}")

if __name__ == "__main__":
    main()