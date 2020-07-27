select city,confirm from  
(select city,confirm from details  # 城市和感染人数拿出来
where update_time=(select update_time from details order by update_time desc limit 1)  # 拿到最新的时间戳
and province not in ("湖北","北京","上海","天津","重庆")  # 不是湖北和直辖市的
# 上面的只查不是湖北和直辖市的
union all  # 作用：将上下两个查询结果拼合成一张表  这里给这张拼合后的表起的别名叫表a
# 下面查的是湖北和直辖市的  # 在sql语句中，使用as可以对字段、表等取别名，像对一些英文的字段取中文名称，使可读性更高。
select province as city,sum(confirm) as confirm from details  # 把直辖市里面所有的区，人数做一个累加作为该直辖市的感染人数
where update_time=(select update_time from details order by update_time desc limit 1)
and province in ("北京"，"上海"， "天津"， "重庆") group by province) as a  # group by province 按省份分组
order by confirm desc limit 5