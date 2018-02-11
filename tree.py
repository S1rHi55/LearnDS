from sklearn import tree
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier

# height, width, show size

x = [
    [181, 80, 41],
    [159, 78, 42],
    [182, 70, 41],
    [158, 68, 39],
    [184, 82, 41], [193, 91, 45], [182, 79, 41],
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
     'male','male','male',
     'female',
     'male',
     'female',
     'male',
     'female',
     'female',
     'female']

clfTree = tree.DecisionTreeClassifier()
clfQuad = QuadraticDiscriminantAnalysis()
clfKNeighbors = KNeighborsClassifier()

clfTreeFitted = clfTree.fit(x,y)
clfQuadFitted = clfQuad.fit(x,y)
clfKNeighborsFitted = clfKNeighbors.fit(x,y)

predictionValues = [[192, 84, 45], [143, 42, 36]]

predictionTree = clfTreeFitted.predict(predictionValues)
predictionQuad = clfQuadFitted.predict(predictionValues)
predictionKNeighbors = clfKNeighborsFitted.predict(predictionValues)

print(predictionTree)
print(predictionQuad)
print(predictionKNeighbors)