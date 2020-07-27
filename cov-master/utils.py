import time
import pymysql

def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")  # %Y,%m,%d: 年月日  %X: 时分秒  {}: 占位符
    return time_str.format("年","月","日")  # 形如：2020年02月17日 14:19:35

def get_conn():
    """
    :return: 连接，游标
    """
    # 创建连接
    conn = pymysql.connect(host="localhost",
                           user="root",
                           password="123456",
                           db="cov",
                           charset="utf8")
    # 创建游标
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    return conn, cursor

def close_conn(conn, cursor):
    cursor.close()
    conn.close()


def query(sql,*args):
    """
    封装通用查询
    :param sql:
    :param args:
    :return: 返回查询到的结果，((),(),)的形式
    """
    conn, cursor = get_conn()  # 拿到连接，获取到游标
    cursor.execute(sql, args)  # 利用游标执行查询的sql操作  如果sql里面涉及到了多个占位符的话，需要传参args把占位符填上
    res = cursor.fetchall()  # 获取结果  fetchall(): 拿到所有的查询结果  ((),(),)
    close_conn(conn, cursor)  # 关闭连接，游标
    return res  # ((),(),)


def get_c1_data():
    """
    :return: 返回大屏div id="c1" 的数据
    """
    # 因为会更新多次数据，取时间戳最新的那组数据
    sql = "select sum(confirm)," \
          "(select suspect from history order by ds desc limit 1)," \
          "sum(heal)," \
          "sum(dead) " \
          "from details " \
          "where update_time=(select update_time from details order by update_time desc limit 1) "
    res = query(sql)  # 调用前面写的通用查询方法  这个返回结果是一个元组  ((sum(confirm), suspect, sum(heal),sum(dead)),)的形式
    return res[0]  # (sum(confirm), suspect, sum(heal),sum(dead))

def get_c2_data():
    """
    :return:  返回各省数据
    """
    # 因为会更新多次数据，取时间戳最新的那组数据
    sql = "select province,sum(confirm) from details " \
          "where update_time=(select update_time from details " \
          "order by update_time desc limit 1) " \
          "group by province"
    res = query(sql)  # ((),(),)
    return res


def get_l1_data():
	sql = "select ds,confirm,suspect,heal,dead from history"
	res = query(sql)  # 查询出来的数据集((ds,confirm,suspect,heal,dead),(ds,confirm,suspect,heal,dead),...)
	return res


def get_l2_data():

	sql = "select ds,confirm_add,suspect_add from history"
	res = query(sql)
	return res	

def get_r1_data():
    """
    :return:  返回非湖北地区城市确诊人数前5名
    """
    sql = 'SELECT city,confirm FROM ' \
          '(select city,confirm from details  ' \
          'where update_time=(select update_time from details order by update_time desc limit 1) ' \
          'and province not in ("湖北","北京","上海","天津","重庆") ' \
          'union all ' \
          'select province as city,sum(confirm) as confirm from details  ' \
          'where update_time=(select update_time from details order by update_time desc limit 1) ' \
          'and province in ("北京","上海","天津","重庆") group by province) as a ' \
          'ORDER BY confirm DESC LIMIT 5'
    res = query(sql)  # ((city, confirm),(city, confirm),(city, confirm),(city, confirm),(city, confirm))
    return res

def get_r2_data():
    """
    :return:  返回最近的20条热搜
    """
    sql = 'select content from hotsearch order by id desc limit 20'
    res = query(sql)  # 格式 (('民警抗疫一线奋战16天牺牲1037364',), ('四川再派两批医疗队1537382',)
    return res
	
if __name__ == "__main__":
    print(get_r2_data())