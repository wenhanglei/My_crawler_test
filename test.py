import pymysql
conn = pymysql.connect(host='localhost', user='root', passwd='****', db='mysql')
cur = conn.cursor()
cur.execute("USE scraping")
cur.execute("select * from pages")
print(cur.fetchone())
cur.close()
conn.close()