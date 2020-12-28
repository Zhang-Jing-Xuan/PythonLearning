import numpy as np
import pandas as pd

data=np.arange(35).reshape(5,7)#[1 2 3 4 5 6 7 8 9]
print(data)
data1=pd.DataFrame(data)
data1=data1.iloc[:, -1]
print(data1)
print("list:\n")
print(list(data1))
# data2=data1.groupby(by=1)
# print(data2)