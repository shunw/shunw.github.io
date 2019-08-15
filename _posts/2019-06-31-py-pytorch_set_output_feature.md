---
layout: post
title: Resnet18 Set Output Feature No
description: 
category: program
tags: [image, ML]
last_modified_at: 2019-06-31T00:00:00+00:00
---


如果没有设置的话，我在使用中发现 output的最终 class有1000个label，但是实际上，我只需要3个class label，这个直接会导致之后计算loss和accuracy有严重误差，解决方法是在设置model的时候，设置他的output class的数量，如下：

- __解决__：

    ```py
    model = models.resnet18(pretrained = False)
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, 3)

    ```

PS： 如果设置pretrained为True，则算法的weights会使用一个已经调试好的一个叫做ImageNet的 classification problem，在这个里面已经有1000个不一样的类别包括 汽车/ 轮船/ 鱼/ 猫/ 狗。这些weights直接存在了这个model里。【参考于：Packt.Deep.Learning.with.PyTorch.2018】