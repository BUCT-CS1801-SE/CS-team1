
-- insert into museum values ('1','name', '文物', '一级', '1', '北京市')


-- select * from museum;
-- delete from museum where idmuseum = 1;
-- insert into museum values('1','故宫博物院','文物','一级','0','东城区景山前街4号');

-- select * from museum where museumName = '故宫博物院';

-- update museum set telephone='010-85007938,010-85007421,010-85007058',
-- collectionInfo='清明上河图',
-- openTime='全年 周一 不开放;4月1日-10月31日 周二至周日 08:30-17:00;11月1日-次年3月31日 周二至周日 08:30-16:30;法定节假日周一不闭馆' 
-- where museumName='故宫博物院';

-- alter table collect modify column introduce text

-- select museumName, collectionInfo from museum;

-- alter table museum add url VARCHAR(255) after museumName;

update museum set url='https://www.dpm.org.cn/' where museumName='故宫博物院';

select * from museum