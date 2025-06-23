# tree is use for decision tree algorithm
from sklearn import tree

def main():
    BallFeatures = [[35,0],[47,0],[90,1],[48,0],[90,1],
                    [35,0],[92,1],[35,0],[35,0],[35,0]]  # load and clean data  
                                                         #  =>  0 for 'rough' and 1 for 'smooth'

    BallNames = [1,1,2,1,2,
                 1,2,1,1,1]     # load and clean data   => 1 for 'tennis' and 2 for 'cricket'
    
    obj = tree.DecisionTreeClassifier()     # train the model

    obj = obj.fit(BallFeatures,BallNames)   # fit is use to train the model

    print(obj.predict([[93,1],[95,1],[42,0],[40,0]]))      # predict is use to test the model

if __name__ == "__main__":
    main()

"""
Output: [2 2 1 1]
"""