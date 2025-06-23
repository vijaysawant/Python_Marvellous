# THIS PROGRAM WILL SHOW ERROR LIKE BELOW
# tree is use for decision tree algorithm
from sklearn import tree

def main():
    BallFeatures = [[35,0],[47,0],[90,1],[48,0],[90,1],
                    [35,0],[92,1],[35,0],[35,0],[35,0]]  # load and clean data

    BallNames = ['tennis','tennis','cricket','tennis','cricket',
                 'tennis','cricket','tennis','tennis','tennis']     # load and clean data
    
    obj = tree.DecisionTreeClassifier()     # train the model

    obj = obj.fit(BallFeatures,BallNames)   # fit is use to train the model

    print(obj.predict([93,1]))      # predict is use to test the model

if __name__ == "__main__":
    main()

"""
visawant@fedora:~/Desktop/Python_Marvellous/Day-15/Machine_Learning$ python BallClassification2.py 
Traceback (most recent call last):
  File "/home/visawant/Desktop/Python_Marvellous/Day-15/Machine_Learning/BallClassification2.py", line 19, in <module>
    main()
  File "/home/visawant/Desktop/Python_Marvellous/Day-15/Machine_Learning/BallClassification2.py", line 16, in main
    print(obj.predict([93,1]))      # predict is use to test the model
          ^^^^^^^^^^^^^^^^^^^
  File "/home/visawant/.local/lib/python3.12/site-packages/sklearn/tree/_classes.py", line 530, in predict
    X = self._validate_X_predict(X, check_input)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/visawant/.local/lib/python3.12/site-packages/sklearn/tree/_classes.py", line 489, in _validate_X_predict
    X = validate_data(
        ^^^^^^^^^^^^^^
  File "/home/visawant/.local/lib/python3.12/site-packages/sklearn/utils/validation.py", line 2954, in validate_data
    out = check_array(X, input_name="X", **check_params)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/visawant/.local/lib/python3.12/site-packages/sklearn/utils/validation.py", line 1091, in check_array
    raise ValueError(msg)
ValueError: Expected 2D array, got 1D array instead:
array=[93.  1.].
Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.
visawant@fedora:~/Desktop/Python_Marvellous/Day-15/Machine_Learning$ 


"""