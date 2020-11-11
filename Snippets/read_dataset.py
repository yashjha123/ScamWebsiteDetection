import scipy.io
import pickle as pkl

print("Loading Dataset...")

mat = scipy.io.loadmat('../Dataset/url.mat')
print(mat)
print("Dataset Loaded!")

print("Saving .pkl file!")

with open("../Dataset/url.pkl","wb") as f:
	pkl.dump(mat, f)

print(".pkl file saved")
print(mat)
print("Code Executed Completely!")