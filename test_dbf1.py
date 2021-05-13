from dbfpy import dbf
db = dbf.Dbf("test1.dbf")
for rec in db:
    print (rec)
    id = rec["id"]
    name = rec["name"]
db.close