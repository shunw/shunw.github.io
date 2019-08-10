---
layout: post
title: in forward/ NotImplementedError
description: 
category: program
tags: [image, ML]
last_modified_at: 2019-06-31T00:00:00+00:00
---


在写引用model class的时候，发现无法算出prediction。报错如下

- `报错`：

    - in forward raise NotImplementedError

- __解决__：

    - 将forward的两个下划线去掉即可，疑似版本问题

    - 报错时是
    ```py
    def __forward__(self, xb):
        return xb.float() @ self.weights + self.bias
    ```

    - 不报错时是
    ```py
    def forward(self, xb):
        return xb.float() @ self.weights + self.bias
    ```
