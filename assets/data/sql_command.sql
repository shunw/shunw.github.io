-- ****************
-- UPDATE COL INFO
-- ****************

-- update category_lkup set color='#ef908b' where category_name = 'machine_learning';

-- ****************
-- DELETE ONE COL
-- ****************
-- alter table main_time rename to tmp_main_time;
-- create table main_time(item_id int, start datetime, end datetime, comment varchar2);
-- insert into main_time(item_id, start, end, comment);
-- select item_id, start, end, comment;
-- from tmp_main_time;
-- drop table tmp_main_time;

-- ****************
-- COL INFO
-- ****************
-- pragma table_info(item_lkup);

-- ****************
-- TABLE NAME
-- ****************
-- select name from sqlite_master where type = 'table';

-- ****************
-- INSERT DATA
-- ****************
insert into main_time
(item_id, start, end, comment)
values
(6, '2019-02-17 8:29:00.000', '2019-02-17 9:09:00.000', ''),
(6, '2019-02-17 9:21:00.000', '2019-02-17 10:45:00.000', ''),
(1, '2019-02-17 10:45:00.000', '2019-02-17 11:00:00.000', 'test others');
