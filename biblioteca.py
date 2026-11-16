from db import DB

db = DB()

def consultar_llibres():
    sql = "SELECT * FROM Llibre"
    return db.execute_query(sql)


def consultar_llibres_disponibles():
    sql = "SELECT * FROM Llibre WHERE disponible = 1"
    return db.execute_query(sql)