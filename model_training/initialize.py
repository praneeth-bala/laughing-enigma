from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import tqdm
import numpy.random as random
import pickle

pbdf = pd.read_csv("permission_benign.csv")
pmdf = pd.read_csv("permission_malware.csv")

pbdf2 = pd.read_csv("intent_benign.csv")
pmdf2 = pd.read_csv("intent_malware.csv")

perm_list = list(pbdf.columns)[1:]
int_list = list(pbdf2.columns)[1:]


with open("./perm_headers.pkl", "wb") as f:
    f.write(pickle.dumps(perm_list))

with open("./perm_headers.pkl", "rb") as f:
    perm_list = pickle.loads(f.read())

with open("./int_headers.pkl", "wb") as f:
    f.write(pickle.dumps(int_list))

with open("./int_headers.pkl", "rb") as f:
    int_list = pickle.loads(f.read())

model = DecisionTreeClassifier()

#Initialize malware and benign vectors from drebin csv
benign=[]
bfnames=pbdf["Unnamed: 0"].tolist()
assert len(bfnames)==len(pbdf2["Unnamed: 0"].tolist())
for x in tqdm.tqdm(bfnames):
    benign.append(np.concatenate(((pbdf[pbdf["Unnamed: 0"]==x].to_numpy()[0][1:].astype(np.float32)),pbdf2[pbdf2["Unnamed: 0"]==x].to_numpy()[0][1:].astype(np.float32))))

malware=[]
mfnames=pmdf["Unnamed: 0"].tolist()
for x in tqdm.tqdm(mfnames):
      malware.append(np.concatenate(((pmdf[pmdf["Unnamed: 0"]==x].to_numpy()[0][1:].astype(np.float32)),pmdf2[pmdf2["Unnamed: 0"]==x].to_numpy()[0][1:].astype(np.float32))))

random.seed(111)
blabel=[0 for i in range(len(benign))]
mlabel=[1 for i in range(len(malware))]
labels=np.array(blabel+mlabel).astype(np.int32)
data=np.concatenate((benign,malware)).astype(np.float32)
c = list(zip(data, labels))
random.shuffle(c)
data, labels = zip(*c)
labels=np.array(labels)
data=np.array(data)

model = model.fit(data, labels)

preds = model.predict(data)
print(accuracy_score(labels, preds))

with open("./dt_model.pkl", "wb") as f:
    f.write(pickle.dumps(model))

with open("./dt_model.pkl", "rb") as f:
    model = pickle.loads(f.read())

preds = model.predict(data)
print(accuracy_score(labels, preds))

model.predict(data[0].reshape(1,-1))[0]