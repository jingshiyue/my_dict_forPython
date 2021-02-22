import STPython
import gzip

# {u'111111111111111-489-1': 'INSERT INTO "DJANGO_MIGRATIONS" ("APP", "NAME", "APPLIED") VALUES (:arg0, :arg1, :arg2) RETURNING "DJANGO_MIGRATIONS"."ID" INTO :arg3'}
# {u'111111111111111-489-2': (<django.db.backends.oscar.base.OscarParam object at 0x0000000004C9EF88>, <django.db.backends.oscar.base.OscarParam object at 0x0000000004C9EB88>, <django.db.backends.oscar.base.OscarParam object at 0x0000000004C9EB08>, <django.db.backends.oscar.base.OscarParam object at 0x0000000004C9EC48>)}
# {u'111111111111111-489-3': ['auth', '0001_initial', Oscar_datetime(2021, 1, 28, 13, 40, 56, 789000), <STPython.NUMBER with value None>]}

con=STPython.Connection('sysdba','szoscar55','119.3.152.217:2003/osrdb')
cur=STPython.Cursor(con)

# cur.execute("SELECT TABLE_NAME, 't' FROM USER_TABLES UNION ALL SELECT VIEW_NAME, 'v' FROM USER_VIEWS")
cur.execute('INSERT INTO "MYAPP_PERSON" ("NAME") VALUES (周) RETURNING "MYAPP_PERSON"."ID" INTO %s')

content = cur.fetchone()
# # content = b.read()

print (content)
# # binary_var = cur.var(STPython.BLOB) 
# # data = gzip.decompress(content)
# # print (data)
# cur.close()

import STPython
import gzip
con=STPython.Connection('sysdba','szoscar55','119.3.152.217:2003/osrdb')
cur=STPython.Cursor(con)
import pdb
pdb.set_trace()
# cur.execute('SELECT * FROM "MYAPP_PERSON" ')
cur.execute('INSERT INTO "MYAPP_PERSON" ("NAME") VALUES (成) RETURNING "MYAPP_PERSON"."ID" INTO %s' params[1])
content = cur.fetchall()
print (content)