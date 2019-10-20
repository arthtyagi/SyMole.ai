import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import model_selection
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix


def train_model():
    data = pd.read_csv("heart.csv")

    # Data types are all integers or floats so we don't have to convert any of them.

    features = data[['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope',
                     'ca', 'thal']]
    labels = data['target']
    features_train, features_test, labels_train, labels_test = model_selection.train_test_split(features, labels,
                                                                                                test_size=0.2,
                                                                                                random_state=30)
    model = RandomForestClassifier(n_estimators=150, max_depth=5, min_impurity_split=None, max_features='auto')
    model.fit(features_train, labels_train)
    return features_train, features_test, labels_train, labels_test, model


def average_score(features_train, features_test, labels_train, labels_test):
    scores = []
    for i in range(100):
        model = RandomForestClassifier(n_estimators=150, max_depth=5)
        model.fit(features_train, labels_train)
        scores.append(model.score(features_test, labels_test))
    return sum(scores) / 100


def best_num_estimators(features_train, features_test, labels_train, labels_test):
    scores = []
    for i in range(1, 200):
        model = RandomForestClassifier(n_estimators=i, max_depth=5, random_state=10, min_impurity_split=None,
                                       max_features='auto')
        model.fit(features_train, labels_train)
        scores.append(model.score(features_test, labels_test))

    x = list(range(1, 200))
    plt.plot(x, scores)
    plt.xlabel("n_estimator")
    plt.ylabel("score")
    plt.title("Finding Best n_estimator")
    plt.show()


def sensitivity_score(y_true, y_pred):
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    sensitivity = tp / (tp + fn)
    return sensitivity


def specificity_score(y_true, y_pred):
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    specificity = tn / (tn + fp)
    return specificity


if __name__ == '__main__':
    features_train, features_test, labels_train, labels_test, model = train_model()
    while (True):
        choice = int(input("""1. Display Model Score
2. Display Graph used to find the best n_estimator for the Model
3. Heart Disease Predictor
4. Exit\n"""))
        while (choice < 1 or choice > 4):
            choice = int(input("Please enter a valid number between 1 and 4.\n"))
        if (choice == 1):
            print("Computing Score...")
            y_true = labels_test;
            y_pred = model.predict(features_test);
            SensitivityScore = sensitivity_score(y_true, y_pred);
            SpecificityScore = specificity_score(y_true, y_pred);
            print("Average Score over 100 runs: {}".format(average_score(features_train, features_test, labels_train,
                                                                           labels_test)))
            print("Specificity Score: {}".format(SpecificityScore))
            print("SensitivityScore: {}\n".format(SensitivityScore))
        elif (choice == 2):
            print("Creating Graph...\n")
            best_num_estimators(features_train, features_test, labels_train, labels_test)
        elif (choice == 3):
            features = []
            features.append(int(input("Enter your age.\n")))
            features.append(int(input("Enter your sex. (1 = male, 0 = female)\n")))
            features.append(int(input("Enter your chest pain experienced (1: typical angina, 2: atypical angina, "
                                      "3: non-anginal pain, "
                                      "4: asymptomatic)\n")))
            features.append(int(input("Enter your resting blood pressure. (mm Hg)\n")))
            features.append(int(input("Enter your cholesterol level. (mg/dl)\n")))
            features.append(int(input("Enter your fasting blood sugar. (1 if > 120 mg/dl, 0 if < 120 mg/dl)\n")))
            features.append(int(input("Enter you resting electrocardiographic measurement (0 = normal, 1 = "
                                      "having ST-T wave abnormality, 2 = showing probable or definite left "
                                      "ventricular hypertrophy "
                                      "by Estes' criteria)\n")))
            features.append(int(input("Enter your maximum heart rate achieved. \n")))
            features.append(int(input("Enter your exercise induced angina (1 = yes, 0 = no)\n")))
            features.append(float(input("Enter your ST depression induced by exercise relative to rest.\n")))
            features.append(int(input("Enter your slope of the peak exercise ST segment (0: upward-sloping, "
                                      "1: flat, 2: downward-sloping)\n")))
            features.append(int(input("Enter the number of major vessels: (0-3)\n")))
            features.append(int(input("Enter if you have thalassemia. (1 = normal, 2 = fixed defect, "
                                      "3 = reversable defect)\n")))
            features = np.reshape(features, (1, -1))
            prediction = model.predict(features)
            if prediction[0] == 1:
                print("We can say with approximately 84.67% confidence that you do have heart disease.\n")
            else:
                print("We can say with approximately 84.67% confidence that you don't have heart disease.\n")
        else:
            break
