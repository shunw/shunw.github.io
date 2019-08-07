---
layout: post
title: Pytorch Trial
description: 
category: program
tags: [image, ML]
last_modified_at: 2019-06-31T00:00:00+00:00
---


在试用pytorch tutorial 的时候，数据是用自己的image读出来的数据，所以试的时候有type error 报错的现象，解决如下：

- RuntimeError: Expected object of scalar type Byte but got scalar type Float for argument #2 'mat2'

    - error as below: 
```py
def forward(self, xb):
    return xb.float() @ self.weights + self.bias
```

- RuntimeError: Expected object of scalar type Long but got scalar type Int for argument #2 'target'

    - error as below:

```py
y_train.append(int(p.split('.')[-2].split('_')[1]))
```

    - Solution: 

```py
y_train.append(int(p.split('.')[-2].split('_')[1]))
y_train = y_train.type(torch.LongTensor)  
```
