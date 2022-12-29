from autoprognosis.plugins.prediction.classifiers import Classifiers

c = Classifiers()

classifiers_list = c.list_available()

print(classifiers_list)
