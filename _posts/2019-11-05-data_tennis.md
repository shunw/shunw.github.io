---
layout: post
title: 网球数据分析
description: 
category: data
tags: [daily]
last_modified_at: 2019-11-05T00:00:00+00:00
---


刚刚理解了一把列的内容，所以先把自己学习到的一些术语放在这里，以备不时之需。（好复杂）

- level: 

    - C: ATP 挑战赛
    - A: ATP 系列赛
    - M: Master 大师杯赛
    - G: Grand Slam 大满贯
    - F: Final (世界排名前8的比赛)

- winner_entry: 

    - WC: wild card
    - Q: 资格赛
    - LL: lucly loser
    - PR: protected ranking
    - SE: special exempt

- winner rank: 当时世界排名，每周更新

- winner_rank_point: 当时世界排名积分，每周更新

- winner/ loser_entry: 当时比赛理的种子排名

- df: double fault 双误

- svpt: save point 比赛里总得分（赢一个球为一分）

- 1st in: 一发进球

- 1st won: 一发赢球

- 2nd won: 二发赢球

- svgm: 保发局数（他发球，且他赢了）

- bpsaved: break point saved 自己保住了自己发球局的破发点

- bpfaced: 自己拿到了多少对方破发点

- round: 当时比赛的场次，比如 16强，8强，1/4赛，半决赛，决赛等

<hr>

### 问题：

预测参赛的人中，所有人中谁夺冠的概率。

### 假设：

选手在最近一段时间，tourney里连续赢球的百分比，会影响下一个tourney里F round里赢球的概率。

### 步骤：

- 随便选取一段赛事，然后将所有的人员抓取出来

- 按照每个人看此人最近一段时间（设置这段时间为可变化的参数）赢得比赛的概率？/看最近一段时间和比赛是否有关联。

    - 选一个人，然后看他一段时间内的夺冠的概率

|winner_name/ winner_id | tourney_name |final_winner? (1/0) | tourney total round # to person | win round # |lose round # | tourney date| surface |
|--- | --- | ---| ---| --- | --- |--- |--- |
|roger xxx | xxx master| 1 | 4 | 4 |0 | 2019-01-01| hard |

### 相关table

- player_info: 运动员的信息，参加的所有的tourney的一些情况，以 名字 和 tourney id 为 key

|player name | tourney_id| tourney_name |surface | draw_size | tourney_date |
|--- | --- | ---| ---| --- | --- |


- win_info: 运动员获胜的场次

|winner name | tourney_id| winner_count |
|--- | --- | ---| 

- lose_info: 运动员输的场次

|loser name | tourney_id| winner_count |
|--- | --- | ---| 


- final_winner_info: 决胜局胜利的运动员和场次

|final_winner_name | tourney_id| 
|--- | --- | 

