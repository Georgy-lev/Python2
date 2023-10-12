import pandas as pd
from random import shuffle

lst = ['robot'] * 10
lst += ['human'] * 10
shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)


data['tmp'] = 1
data.set_index([data.index, 'whoAmI'], inplace=True)
data = data.unstack(level=-1, fill_value=0).astype(int)
data.columns = data.columns.droplevel()
data.columns.name = None
print(data)