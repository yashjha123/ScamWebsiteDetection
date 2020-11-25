import pickle as pkl
import numpy as np
from sklearn import tree
import matplotlib.pyplot as plt
use_checkpoint = False
file = "checkpoints/"+"checkpoint0.9896.pkl"
if not use_checkpoint:
	print("Loading sklearn Library...")
	from sklearn.ensemble import RandomForestClassifier
	print("Loaded sklearn Library!")
	print("Loading FeaturesNew...")
	with open("./FeaturesNew.pkl","rb") as f:
		features1 = pkl.load(f)
	print("Loaded FeaturesNew!")
	print("Loading featuresNonMalFinal...")
	with open("./featuresNonMalFinal.pkl","rb") as f:
		features2 = pkl.load(f)
	print("Loaded featuresNonMalFinal!")
	print("Stacking two arrays(train)")
	X_train = np.vstack((features1[:10000],features2[:10000]))
	y_train = [1 for x in range(10000)]+[0 for x in range(10000)]
	print("Stacking two arrays(test)")
	X_test = np.vstack((features1[10000:],features2[10000:]))
	y_test = [1 for x in range(len(features1[10000:]))]+[0 for x in range(len(features2[10000:]))]

	clf = RandomForestClassifier(max_depth=15, random_state=12321)
	print(len(X_train),len(y_train))
	clf.fit(X_train, y_train)
	print("Training Score:- ",clf.score(X_train, y_train))
	print("Test Score:- ",clf.score(X_test, y_test))
	print(len(X_train),len(X_test))
	with open("checkpoints/"+"checkpoint"+str(clf.score(X_train, y_train))+".pkl","wb") as f:
		pkl.dump(clf, f)
else:

	print("Loading Checkpoint...")
	with open(file,"rb") as f:
		clf = pkl.load(f)
	print("Loaded Checkpoint!")

# fig = plt.figure()
# _ = tree.plot_tree(clf.estimators_[0], feature_names=["pagal" for x in range(1177)], filled=True)
# plt.xlim(0,1)
# plt.ylim(0,1)
# # plt.show()
# plt.savefig("tree.png",dpi=fig.dpi,quality=100)
from sklearn.tree import export_graphviz
# Export as dot file
print("No. of estimators_",len(clf.estimators_))
export_graphviz(clf.estimators_[0], out_file='tree.dot', 
                feature_names = ["pagal" for x in range(1177)],
                rounded = True, proportion = False, 
                precision = 2, filled = True)
