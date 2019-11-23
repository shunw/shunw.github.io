---
layout: post
title: 网球数据分析日记
description: 
category: data
tags: [daily]
last_modified_at: 2019-11-05T00:00:00+00:00
---


### 问题1：

预测参赛的人中，所有人中谁夺冠的概率。

### 假设：

【失败】选手在最近一段时间，tourney里连续赢球的百分比，会影响下一个tourney里F round里赢球的概率。--- 么以看出相关

【选取假设】设计数据，查看哪些是相关

### 数据处理步骤（理想中，可能之后会有更新）：

- 将需要的数据用dataframe的形式表达出来；

    - y: final_winner --- the probability to be tourney final winner. 

    - x: player_name, tourney_level, surface, player_age, player_ht, player_hand, player_rank_point(this need to deal with NULL data), **recent_period_win_percent** (maybe 1 year's avg of the win_percent * tourney_level)

        - 用pandas df.rolling来处理，时间长度可以自己设置。


- 将category的数据用one-hot-encoding的方式处理;

    - 用pandas get_dummies来处理

- 降维;

    - 【失败】用PCA 处理，后来发现col是330（因为one hot encoding的关系），前四个因子累加起来的百分比刚超过5%。

- 线性数据处理

    - EDA/ use pairplot to check the data relationship.

        - 没有出来有明显的相关x因素和y结果之间

        - player_age/ player_ht has 0 data.

- 将数据分成training dataset 和 test dataset; 并验证是否各个y label平均分配; 

- 将数据 X_train 进行归一化处理,且应用到 X_test 上

- 之后用sklearn里的现成的包

- 接着计算accuracy

### 相关table

- player_wl_tourney (main_dataset_deal_with)

|player_name | tourney_id|tourney_name |surface |draw_size|tourney_level|tourney date| final_winner | round_total | winner_max_round |win_percent| player_hand|player_age|player_ht|player_rank_points|wt_win_percent|
|--- | --- | ---| ---| --- | --- |--- |--- |--- | --- |--- |  --- |--- | --- |--- | --- |  
|roger xxx | idxxx|xxx master| hard |32|A|2019-01-01| 1 | 4 | 4 |100| R|20|189|2190|win% * level weight|


- player_info: 运动员的信息，参加的所有的tourney的一些情况，以 名字 和 tourney id 为 key

|player_name | tourney_id| tourney_name |surface | draw_size | tourney_level|level_weight|tourney_date |player_hand|player_age|player_ht|player_rank_points|
|--- | --- | ---| ---| --- | --- |--- |---| --- | --- |--- |--- |
|roger xxx | xxx | xx master| hard| 32 | A|1|2019-01-01 |R|20|189|2190|

- tourney_r_info: 每次tourney的round，及其排位

|round | round_count | t_id| 
|--- | --- | ---| 
|RR | 4 | which is tourney_id| 

- tourney_r_total: 每次tourney的round总数

|tourney_id | round_total|
|--- | --- | 
|xxx | 5 |


- win_info: 运动员获胜的最后的场次

|winner_name | winner_max_round | tourney_id| 
|--- | --- | ---| 
|roger xxx | 4 | xxx| 

- lose_info: 运动员输的场次

|loser_name | loser_count |tourney_id| 
|--- | --- | ---| 
|roger xxx | 1 | xxx| 


- final_win_info: 决胜局胜利的运动员和场次

|final_winner_name | tourney_id| 
|--- | --- | 
|roger xx | xxx | 

### 问题2：

赢得赛事的概率，是否和左右手持拍有关 
    
- 是否可以应用到假设检验

    - 如何分配数据


### 假设：


<hr>

### obstacle

- category input to numerical data

    - nominal input: try the one-hot-encoding first

### trial steps

- change the category input into numerical data

- use classification algorithm with scikit-learn

- back to use PCA or other tool to check if any improvement can be gained. 

<hr>

### col 内容理解

刚刚理解了一把列的内容，所以先把自己学习到的一些术语放在这里，以备不时之需。（好复杂）

- level: 

    - C (1): ATP 挑战赛
    - A (2): ATP 系列赛
    - M (3): Master 大师杯赛
    - G (4): Grand Slam 大满贯
    - F (5): Final (世界排名前8的比赛)

- winner_entry: 

    - WC: wild card
    - Q: 资格赛
    - LL: lucly loser
    - PR: protected ranking
    - SE: special exempt

- winner rank: 当时世界排名，每周更新

- winner_rank_point: 当时世界排名积分，每周更新

- winner/ loser_entry: 当时比赛里的种子排名

- df: double fault 双误

- svpt: save point 比赛里总得分（赢一个球为一分）

- 1st in: 一发进球

- 1st won: 一发赢球

- 2nd won: 二发赢球

- svgm: 保发局数（他发球，且他赢了的那一局）

- bpsaved: break point saved 自己保住了自己发球局的破发点

- bpfaced: 自己拿到了多少对方破发点

- round: 当时比赛的场次，比如 16强，8强，1/4赛，半决赛，决赛等