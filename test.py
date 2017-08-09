import pymysql
conn = pymysql.connect(host='localhost', user='root', passwd='712342', db='mysql')
cur = conn.cursor()
cur.execute("USE scraping")
cur.execute("select * from pages")
print(cur.fetchone())
cur.close()
conn.close()