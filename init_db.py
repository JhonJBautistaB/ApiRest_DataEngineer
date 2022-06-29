from controller import init_tb_db


""" Modulo que permite inicializar la BD para la prueba de concepto con Pandas """
# instancia de creación
try:
    initiald_tb = init_tb_db()
except Exception as ex:
    print("Se ha generado un error al inicializar las tablas")