---
layout: post
title: Find the Outline Properly
description: 
category: program
tags: [image, ML, cv2]
last_modified_at: 2020-05-04T00:00:00+00:00
---

机缘巧合，最近跟着PyImage 的 Adrian的Blog，学习一些图像处理。。。其中我觉得比较有兴趣的一个方面是如何对照片中的图像进行[长宽的测量](https://www.pyimagesearch.com/2016/03/28/measuring-size-of-objects-in-an-image-with-opencv/?__s=yo68x506yucrfbb1gtj5)。

按照Adrian的理念是：

- 将标准的尺寸的物品放在最左边/最右边
    
- 拍照
    
- 将图中的物品的外形都找出来
    
- 用 标准尺寸物品 的 实际长宽 和 图中的 长宽 进行一个比较，得到ratio

- 对其他物品处理以类似的 ratio，以得到其实际长宽

自己的实操预期 及 没有料到的坑：

    - 画一个矩形，然后在四个角上画上 10mm 的正方形

    - 找出矩形四个点，并对其进行 [top-down_view](https://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/)的处理

    - 对四个角上的正方形进行ratio比较，并做出ratio的计算

    - 对放在这个框里的物品，进行长宽计算，并对结果做出error的计算

![正方形0_w_pencil](../assets/img/cv2/square_line.JPG)
坑：铅笔的颜色太浅，不能找出矩形边界

![正方形_w_pen_filled_square](../assets/img/cv2/square_line_2.JPG)
坑：四角上的正方形涂色，但是没有办法找到最外面的四个角，找到的矩形的四个点，是以正方形靠内的四个点组成的，四个calibration的正方形没有被包含进去

![正方形_w_pen_not_filled_square](../assets/img/cv2/square_line_not_fill.JPG)
坑：无法找出矩形的完整边框。。汗。。

预期的坑：

    - 精度不够，因为拍照的位置的关系，可能有些地方会有拉长/ 缩短


