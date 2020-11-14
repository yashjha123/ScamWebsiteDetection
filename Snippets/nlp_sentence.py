from sklearn.feature_extraction import FeatureHasher
h = FeatureHasher(n_features=10)
D = [{'doggy': 1, 'cat':2, 'elephant':4},{'doggy': 2, 'run': 5}]
f = h.transform(D)
print(f.toarray())

D = [{'doggy': 10, 'cat':2, 'elephant':4},{'doggy': 2, 'run': 5}]
f = h.transform(D)
print(f.toarray())