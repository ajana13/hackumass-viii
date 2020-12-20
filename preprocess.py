import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# helper function, list difference
# https://stackoverflow.com/questions/6486450/python-compute-list-difference
diff = lambda l1,l2: [x for x in l1 if x not in l2]

# hardcoded input of training data
data = pd.read_csv("data/copy.csv")
df = pd.DataFrame(data)

### text columns ###
obj_df = df.select_dtypes(include=['object']).copy()
text_cols = list(obj_df.columns.values)

df = df.dropna(axis=1, thresh=121)

# df.apply(lambda x: np.where(x.isnull(), x.dropna().sample(len(x), replace=True), x))

### continuous columns ###
all_cols = list(df.columns.values)
cont_cols = diff(all_cols, text_cols)

print("shape: ", df.shape)

df.to_csv("data/full_constant_0.csv", index=False)