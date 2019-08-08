---
layout: post
title: Pytorch Type Error
description: 
category: program
tags: [image, ML]
last_modified_at: 2019-06-31T00:00:00+00:00
---


在试用pytorch tutorial 的时候，数据是用自己的image读出来的数据，所以试的时候有type error 报错的现象，报错及解决如下：

- __报错1__：

    - RuntimeError: Expected object of scalar type Byte but got scalar type Float for argument #2 'mat2'

- __解决1__：

    - 在xb后面加了.float()。因为输入的数据是 0-255的 int（图像的原因），即使归一化之后，类型还是有问题。

    ```py
    def forward(self, xb):
        return xb.float() @ self.weights + self.bias
    ```

- __报错2__：

    - RuntimeError: Expected object of scalar type Long but got scalar type Int for argument #2 'target'

    

    ```py
    y_train.append(int(p.split('.')[-2].split('_')[1]))
    ```

- __解决1__：

    - 之前的y是int，换成float也不行，他会报错说期待的是Long，但是你给的是Double，所以在读入y数据的时候，直接将type改成了LongTensor

    ```py
    y_train.append(int(p.split('.')[-2].split('_')[1]))
    y_train = y_train.type(torch.LongTensor)  
    ```
