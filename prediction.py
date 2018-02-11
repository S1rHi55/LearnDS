from sklearn import tree
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

x = [
    [181, 80, 41],
    [159, 78, 42],
    [182, 70, 41],
    [158, 68, 39],
    [184, 82, 41],
    [193, 91, 45],
    [182, 79, 41],
    [163, 78, 39],
    [181, 79, 41], 
    [169, 78, 42],
    [181, 80, 41],
    [160, 79, 41],
    [181, 60, 41],
    [162, 75, 42]
]

y = ['male',
     'female',
     'male',
     'female',
     'male',
     'male',
     'male',
     'female',
     'male',
     'female',
     'male',
     'female',
     'female',
     'female']

predictionValues = [[192, 84, 45], [143, 42, 36]]

def useModel(name, model):
    fitModel = model.fit(x,y)
    accuracy = accuracy_score(y, fitModel.predict(x)) * 100
    print(name)
    print(accuracy)
    predictNew = fitModel.predict(predictionValues)
    print(predictNew)

useModel('tree', tree.DecisionTreeClassifier())
useModel('quadratic', QuadraticDiscriminantAnalysis())
useModel('KNeighbors', KNeighborsClassifier())
