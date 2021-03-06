---
layout: default
title: ML_study
---

### 目的

- 记录一下我在学习过程中的困惑，收获，主要是在machine learning这个方向上，也包括一些图片处理. 


### 心得

#### 关于图片处理

- 加上kernel，如何显示图片

#### 关于 pytorch 学习

- [Type_Error]({{ site.baseurl }}{% link _posts/2019-06-31-py-pytorch_type_error.md %})

- [in forward/ raise NotImplementedError]({{ site.baseurl }}{% link _posts/2019-06-31-py-pytorch_forward.md %})

- [set Resnet18 output feature#]({{ site.baseurl }}{% link _posts/2019-06-31-py-pytorch_set_output_feature.md %})

### 进行中

#### 可以做到

- 从Video里按照frame截图

#### 目前困扰

- 无法正确判断明亮的物体的个数，会把0个误判成1个，也会把2个误判成0 - 1 个，准备用pytorch解决

- 但是pytorch的准确率不高，如下是书上(Packt Deep Learning with PyTorch)的建议:

    - with transfer learning

        - 可能对我自己的图像识别帮助不大
    
    - try playing with different dropout values

    - change dropout value

    - add more data

        - 略有提高，
    
    - do data augmentation like: randomly flipping the horizontally/ rotate the image by a small angle 

        - 没有提高，反而有下降，继续观察之

    - try dropout 

    - try different activation function, like tanh (need to check the if the intial weights are optimal for it or not) for the hidden layer and the softmax for the final layer

- manning_grokking: Page 195 add sigmoid derivative training accuracy rises while test accuracy down a little. 

#### 试着探索

- 是否有可能用pytorch解决这个问题？

- 别人的blog里可以明确判断object（如人）是如何做到的?

- 探索下如何降低loss 提高acc in Mnist / Cats and Dogs； 且对比下书上的案例

- 看下youtube的视频，是否有按照视频练习的可能。

- 是否可以将model 极其参数存下来/ 将cnn的training 参数存下来 后续用

- 计算tanh/ softmax的derivative




