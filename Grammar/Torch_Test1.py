import torch
from touch.autograd import Variable
import numpy as np


np_data=np.arange(6).reshape((2,3))
torch_data=torch.from_numpy(np_data)
tensor2array=torch_data.numpy()
print(
    '\nnnumpy',np_data,
    '\ntouch',torch_data,
    '\ntensor2array',tensor2array,
)

data=[-1,-2,1,2]
tensor=torch.FloatTensor(data)
print(
    '\nabs',
    '\nnumpy:',np.abs(data),
    '\ntorch:',torch.abs(tensor)
)

data=[[1,2],[3,4]]
tensor=torch.FloatTensor(data)
print(
    '\nnumpy:',np.matmul(data,data),
    '\ntorch:',torch.mm(tensor,tensor),
)