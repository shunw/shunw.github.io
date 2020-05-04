---
layout: post
title: Find the Outline Properly
description: 
category: program
tags: [image, ML, cv2]
last_modified_at: 2020-05-04T00:00:00+00:00
---

机缘巧合，最近跟着PyImage 的 Adrian的Blog，学习一些图像处理。。。其中我觉得比较有兴趣的一个方面是如何对照片中的图像进行[长宽的测量](https://www.pyimagesearch.com/2016/03/28/measuring-size-of-objects-in-an-image-with-opencv/?__s=yo68x506yucrfbb1gtj5)。

## 按照Adrian的理念是：

- 将标准的尺寸的物品放在最左边/最右边
    
- 拍照
    
- 将图中的物品的外形都找出来
    
- 用 标准尺寸物品 的 实际长宽 和 图中的 长宽 进行一个比较，得到ratio

- 对其他物品处理以类似的 ratio，以得到其实际长宽

## 自己的实操预期 及 没有料到的坑：

- 画一个矩形，然后在四个角上画上 10mm 的正方形
    
    - 完成，虽然不够完美

- 找出矩形四个点，并对其进行 [top-down_view](https://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/)的处理
    
    - 正在处理坑 👈

- 对四个角上的正方形进行ratio比较，并做出ratio的计算

- 对放在这个框里的物品，进行长宽计算，并对结果做出error的计算

## 坑1：

![正方形0_w_pencil](/assets/img/cv2/square_line.JPG)

- 铅笔的颜色太浅，不能找出矩形边界

    - 用水笔加深

## 坑2：

![正方形_w_pen_filled_square](/assets/img/cv2/square_line_2.JPG)

- 四角上的正方形涂色，但是没有办法找到最外面的四个角，找到的矩形的四个点，是以正方形靠内的四个点组成的，四个calibration的正方形没有被包含进去

    - 又画了其他的图

    - 可以继续研究下 👈


## 坑3：

![正方形_w_pen_not_filled_square](/assets/img/cv2/square_line_not_fill.JPG)

- 无法找出矩形的完整边框。。汗。。
    
    - 检查edged 图像，调整threshold

- 找出了差不多的框，可能是计算的area，有少许不同；另外导致这个问题的原因可能是因为框有的地方比较粗，所以因为是不同的框

    - 对area进行排序
    
    - cv2.boundingRect 得到 x, y, weight, height
    
    - 对前后的x, y, w, h进行比较
    
    - 设置threshold，如果x, y, w, h的前后比较值 大于 .97，则舍弃该contour

## milestone1: 

终于作出这个图了，激动的过来纪念以下。

![矩形_outline_top_down_view](/assets/img/cv2/rec_outline_top_down.JPG)

## 预期的坑：

- 精度不够，因为拍照的位置的关系，可能有些地方会有拉长/ 缩短

## Wendy 的个人心得：

- 以下步骤对找出妥当的edge必不可少

    - 处理成gray，之后进行 GaussianBlur

    - 进行Canny 处理，注意设置妥当的threshold❗️

    - Adrian没有进行 edge dilate的处理，但是我发现，如果用我自己拍的图，为了找出妥当的边框，这一步不能少，也不排除是因为我拍的照片不够好

        ```py
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

        edged = cv2.dilate(edged, kernel)
        ```

    - 有时找出来的框有问题，那就加上 put Text， 对每一个contour进行标识，或者一个一个的放contour，进行debug，实测挺好用 👍

    - Adrian介绍的，计算周长，以此查看是否是四边形，这个模块没有用上，可以相见[链接](https://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/)，他的41行 - 51行这里