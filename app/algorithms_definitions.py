from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import pandas
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn import svm


def get_train_data():
    # read data and labes from files
    train_x = pandas.read_csv('app/train/X_train.txt', header=None, delimiter=' ')
    train_y = pandas.read_csv('app/train/y_train.txt', header=None, delimiter=' ')

    # create list of list for training data
    train_x = np.array(train_x)

    # create list of labels for train data
    train_labels = []
    y_array = np.array(train_y)
    for y in y_array:
        train_labels.append(y[0])

    return train_x, train_labels


def get_test_data():
    # read test data
    test_x = pandas.read_csv('app/test/X_test.txt', header=None, delimiter=' ')
    test_y = pandas.read_csv('app/test/y_test.txt', header=None, delimiter=' ')
    test_x = np.array(test_x)
    test_labels = []
    y_array = np.array(test_y)
    for y in y_array:
        test_labels.append(y[0])

    return test_x, test_labels


def get_predict_and_effectiveness(clf, test_x, test_labels):
    # testing
    test_predict_labels = clf.predict(test_x)
    # checking the results
    labels_len = len(test_labels)
    wrong_predict_count = 0
    for x in range(labels_len):
        if test_labels[x] != test_predict_labels[x]:
            wrong_predict_count += 1

    effectiveness = 100 - (wrong_predict_count / labels_len * 100)

    return test_predict_labels, effectiveness


def svm_function(kernel='rbf'):
    clf = svm.SVC(gamma='scale', kernel=kernel)
    return get_function('svm', clf)


def kNN_function(neighbors=5, metric='minkowski'):
    clf = KNeighborsClassifier(n_neighbors=neighbors, metric=metric)
    return get_function('kNN', clf)


def dt_function():
    clf = DecisionTreeClassifier()
    return get_function('DecisionTreeClassifier', clf)


def rf_function():
    clf = RandomForestClassifier()
    return get_function('RandomForestClassifier', clf)


def get_function(function_name, clf):
    train_x, train_labels = get_train_data()
    clf.fit(train_x, train_labels)
    scores = cross_val_score(clf, train_x, train_labels, cv=5)
    cross_val_score_mean = scores.mean()

    # testing
    test_x, test_labels = get_test_data()
    test_predict_labels, effectiveness = get_predict_and_effectiveness(clf, test_x, test_labels)

    plt.scatter(test_x[:, 0], test_x[:, 1], c=test_predict_labels, label='Features points')
    plt.title("Plot for {} algorithm. Effectiveness: {:.2f}%. Mean of cross_val_score: {:.2f}".format(function_name,
                                                                                                      effectiveness,
                                                                                                      scores.mean()))
    plt.legend()
    path = 'app/static/images/%s.png' % function_name
    plt.savefig(path)

    return cross_val_score_mean, effectiveness, path


print(" **** ")
print(svm_function())
print(" **** ")
print(kNN_function())
print(" **** ")
print(dt_function())
print(" **** ")
print(rf_function())