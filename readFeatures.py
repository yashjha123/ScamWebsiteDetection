import pickle as pkl
import numpy as np
from sklearn.ensemble
with open("./featuresNew.pkl","rb") as f:
	features = pkl.load(f)
print(np.array(features).shape)