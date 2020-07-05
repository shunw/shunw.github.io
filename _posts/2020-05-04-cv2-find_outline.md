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
    
    - 完成 

- 找出四个角上的定位点

    - done

    - 填过的坑：一直找不到左下角的定位点，是因为edge上有broken，所以用find contour找不到这个square

- 对四个角上的正方形进行ratio比较，并做出ratio的计算

- 对放在这个框里的物品，进行长宽计算，并对结果做出error的计算

## 图1：(failed)

![正方形0_w_pencil](/assets/img/cv2/square_line.JPG)

- 铅笔的颜色太浅，不能找出矩形边界

    - 用水笔加深

## 图2：

![正方形_w_pen_filled_square](/assets/img/cv2/square_line_2.JPG)

- 状态： 

    - 成功分解出矩形框

    - 准备测量定位正方形

- mark: 
    
    - 整张纸的情况下

        - 按照cv2.contourArea进行排序，index 2 为外圈矩形

        - 三个正方形定位角的index 依次为 2, 3, 4

    - 四个定位方块的情况下

        - 可以找到左上，右上，右下的定位正方形，但是找不到左下的定位正方形

- 现有问题：

    - 找不到左下的定位正方形

        - 因为edge 有broken，需要自己填上


## 图3：

![正方形_w_pen_not_filled_square](/assets/img/cv2/square_line_not_fill.JPG)

- 状态：

    - 成功分解出矩形框

    - 准备测量定位正方形

- mark: 

    - 按照cv2.contourArea进行排序，index 2 为外圈矩形
    

    


## 预期的坑：

- 精度不够，因为拍照的位置的关系，可能有些地方会有拉长/ 缩短

## Wendy 的个人心得：

- 找出edge初期步骤：

    - 处理成gray，之后进行 GaussianBlur

        - 在找定位涂黑的正方形的时候，mediaBlur的效果比GaussianBlur好

    - 进行Canny 处理，注意设置妥当的threshold❗️

    - Adrian没有进行 edge dilate的处理，但是我发现，如果用我自己拍的图，为了找出妥当的边框，这一步不能少，也不排除是因为我拍的照片不够好

        - 因为是找正方形，所以其中应该使用 cv2.MORPH_RECT

    ```py
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    edged = cv2.dilate(edged, kernel)
    ```

- 找出 contour， 可以有的debug 手段
    
    - 加上 put Text， 对每一个contour进行标识，或者一个一个的找contour，实测挺好用 👍

        - 一个一个确认的步骤，详见 open_cv_6_17_measure.py

        - 因为conts返回值是list，所以要对list进行处理，多个conts的，比 单个conts的会多一层

- 去掉重复/ 相似的 contour 

    - 详见 open_cv_6_17_measure.py

    - 对area进行排序
    
    - cv2.boundingRect 得到 x, y, weight, height
    
    - 对前后的x, y, w, h进行比较
    
    - 设置threshold，如果x, y, w, h的前后比较值 大于 .97，则舍弃该contour

- 找四边形

    - 还是需要 Adrian介绍的模块，详见[链接](https://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/)，代码41行 - 51行

- 用find contour 找四边形，可能会因为有line broken直接导致找不到这形状

- 找出四个角上的calibration色块 （和边界很接近）

    - 因为和边界很接近，用cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)[1]

    - 要注意调整 100 - 255这个threshold，在色块的浓度和边线上 进行balance

- 四个和四边的line接壤的定位色块，右下↘️和左下↙️无法找到对应的contour

    - 怀疑：原因是有毛刺

    - 用canny 的效果比用threshold(gray, 100, 255, cv2.THRESH_BINARY)[1]的效果好，能找出右下的框

    - 失败尝试：

        - 用[solution](https://stackoverflow.com/questions/46486078/opencv-how-to-find-rectangle-contour-of-a-rectangle-with-round-corner) 将图像黑白reverse，但是酱紫就无法基本无法找出边框

![毛刺图](/assets/img/cv2/square_attached_lines.png)

- ❓有时因为线粗细不匀，四边形会被认为是n边形，如何处理？

## milestone1: 

终于作出这个图了，激动的过来纪念一下。

![矩形_outline_top_down_view](/assets/img/cv2/rec_outline_top_down_not_fill.png)


## Reference: 

- [about contour algorithm](https://theailearner.com/2019/08/31/contour-tracing/)

    - [refer to this article](http://www.imageprocessingplace.com/downloads_V3/root_downloads/tutorials/contour_tracing_Abeer_George_Ghuneim/index.html)