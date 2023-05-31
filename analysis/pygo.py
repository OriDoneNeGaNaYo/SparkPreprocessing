import pymysql

hostname = "127.0.0.1"
username = "root"
go_db = "bus"
password = "busdb"
port = "3308"


conn = pymysql.connect(
    host=hostname,
    user=username,
    db=go_db,
    password=password,
    port=int(port)
)


if conn is None:
    print(" None ")
else:
    print(" Great! ")