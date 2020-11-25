import pickle as pkl
import numpy as np
# from sklearn.ensemble
with open("./featuresNonMalFinal.pkl","rb") as f:
	features = pkl.load(f)
print(np.array(features).shape)