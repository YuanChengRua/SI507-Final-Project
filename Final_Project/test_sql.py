import sqlite3

conn = sqlite3.connect('user_temp.db', check_same_thread=False)
cur = conn.cursor()


temp = 'DELETE from user_table1697_Broadway_Street WHERE name =' + ''Lucky Kitchen''
cur.execute(temp)
# cur.execute('REINDEX user_table1697_Broadway_Street')
# a = cur.execute('SELECT name_id FROM user_table1697_Broadway_Street').fetchall()
# b = cur.execute('ALTER TABLE user_table1697_Broadway_Street RENAME TO temp')
# g = cur.execute('SELECT * FROM temp').fetchall()
# print(g)
# conn.commit()
# c = cur.execute('SELECT name FROM (SELECT * FROM user_table1697_Broadway_Street ORDER BY rating DESC, distance) as t LIMIT 1').fetchall()
# print(c)
# print(b)