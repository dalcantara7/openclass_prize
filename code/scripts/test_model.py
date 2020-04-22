import pickle 
import numpy as np

def predict(input_data):
    vectorizer = pickle.load(open("code/scripts/vectorizer.pickle", "rb"))
    mlb = pickle.load(open("code/scripts/multi-label_binarizer.pickle", "rb"))

    X_trans = vectorizer.transform([input_data]) #<--- Needs to be an iterable

    models = []
    with open("code/scripts/models.pickle", "rb") as f:
        models = pickle.load(f)
    
    class_preds = []
    for i in range(len(models)):
        class_preds.append(models[i].predict(X_trans)[0])

    as_np = np.array([np.array(class_preds)]) #<--- Yes it really needed to be in this form to work
    labels = mlb.inverse_transform(as_np)

    to_return = list(labels[0])

    return to_return