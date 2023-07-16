from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pickle
import os
from maldetect.settings import BASE_DIR

def get_feat_vector(file):
    with open(os.path.join(BASE_DIR,"./maldetect_api/feat_store/perm_headers.pkl"), "rb") as f:
        perm_words = pickle.loads(f.read())
    with open(os.path.join(BASE_DIR,"./maldetect_api/feat_store/int_headers.pkl"), "rb") as f:
        int_words = pickle.loads(f.read())

    vector = [0]*(len(perm_words)+len(int_words))
    lines = file.split('<')
    for line in lines:
        if line.startswith("uses-permission") or line.startswith("uses-permission-sdk-23") or line.startswith("permission"):
            words = line.split('"')
            for word in words:
                try:
                    ind = perm_words.index(word)
                    vector[ind]=1
                except:
                    pass
        elif line.startswith("action") or line.startswith("category"):
            words = line.split('"')
            for word in words:
                try:
                    ind = int_words.index(word)
                    vector[len(perm_words)+ind]=1
                except:
                    pass
    return vector

    
def get_model():
    with open(os.path.join(BASE_DIR,"./maldetect_api/feat_store/dt_model.pkl"), "rb") as f:
        model = pickle.loads(f.read())
    return model

def is_malicious(xml):
    vector = np.array(get_feat_vector(xml))
    model = get_model()
    prediction = model.predict(vector.reshape(1,-1))
    return prediction


