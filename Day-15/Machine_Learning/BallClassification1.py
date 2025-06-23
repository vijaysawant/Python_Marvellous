# THIS PROGRAM WILL SHOW ERROR LIKE BELOW
# tree is use for decision tree algorithm
from sklearn import tree

def main():
    BallFeatures = [[35,'rough'],[47,'rough'],[90,'smooth'],[48,'rough'],[90,'smooth'],
                    [35,'rough'],[92,'smooth'],[35,'rough'],[35,'rough'],[35,'rough']]  # load and clean data

    BallNames = ['tennis','tennis','cricket','tennis','cricket',
                 'tennis','cricket','tennis','tennis','tennis']     # load and clean data
    
    obj = tree.DecisionTreeClassifier()     # train the model

    obj = obj.fit(BallFeatures,BallNames)   # fit is use to train the model

    print(obj.predict([93,'smooth']))      # predict is use to test the model

if __name__ == "__main__":
    main()
"""
visawant@fedora:~/Desktop/Python_Marvellous/Day-15/Machine_Learning$ python BallClassification1.py 
Traceback (most recent call last):
  File "/home/visawant/Desktop/Python_Marvellous/Day-15/Machine_Learning/BallClassification1.py", line 18, in <module>
    main()
  File "/home/visawant/Desktop/Python_Marvellous/Day-15/Machine_Learning/BallClassification1.py", line 13, in main
    obj = obj.fit(BallFeatures,BallNames)   # fit is use to train the model
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/visawant/.local/lib/python3.12/site-packages/sklearn/base.py", line 1363, in wrapper
    return fit_method(estimator, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/visawant/.local/lib/python3.12/site-packages/sklearn/tree/_classes.py", line 1024, in fit
    super()._fit(
  File "/home/visawant/.local/lib/python3.12/site-packages/sklearn/tree/_classes.py", line 252, in _fit
    X, y = validate_data(
           ^^^^^^^^^^^^^^
  File "/home/visawant/.local/lib/python3.12/site-packages/sklearn/utils/validation.py", line 2966, in validate_data
    X = check_array(X, input_name="X", **check_X_params)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/visawant/.local/lib/python3.12/site-packages/sklearn/utils/validation.py", line 1053, in check_array
    array = _asarray_with_order(array, order=order, dtype=dtype, xp=xp)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/visawant/.local/lib/python3.12/site-packages/sklearn/utils/_array_api.py", line 757, in _asarray_with_order
    array = numpy.asarray(array, order=order, dtype=dtype)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: could not convert string to float: 'rough'
"""