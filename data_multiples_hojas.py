import pandas as pd
import mysql.connector
import openpyxl


# Funcion para establecer conexión con BD MySQL y Python
def connectionBD():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="demo",
            raise_on_warnings=True
        )
        if connection.is_connected():
            return connection

    except mysql.connector.Error as error:
        print(f"No se pudo conectar: {error}")


# Función que retorna la lista de usurios de una Tabla en BD
def listaRegistros():
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as mycursor:
                querySQL = "SELECT * FROM registros"
                mycursor.execute(querySQL,)
                lista_registros = mycursor.fetchall()
                return lista_registros
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return {}


# Función que genera la 2 hoja del Excel para la tabla de Registros
def hojaRegistros(listaRegistrosBD, wb):
    hoja = wb.create_sheet(title="Registros")
    hoja.append(('Id', 'Nombre', 'Profesion', 'Estatus'))
    for registro in listaRegistrosBD:
        hoja.append((registro['id'], registro['nombre'],
                    registro['profesion'], registro['status']))


# Función que retorna la lista de personas de una Tabla en mi BD
def listaPersonas():
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as mycursor:
                querySQL = "SELECT * FROM personas"
                mycursor.execute(querySQL,)
                lista_personas = mycursor.fetchall()

                wb = openpyxl.Workbook()

                hoja = wb.active
                hoja.title = "Consignaciones"
                # Crea la fila del encabezado con los títulos
                hoja.append(('Id', 'Nombre', 'Sexo', 'Email'))
                for persona in lista_personas:
                    # Agrega una tupla con los valores de la persona
                    hoja.append((persona['id_persona'], persona['nombre'],
                                persona['sexo'], persona['email']))

                # Crea una hoja de Excel para los Registros
                lista_registrosBD = listaRegistros()
                hojaRegistros(lista_registrosBD, wb)

                # Guarda el archivo Excel
                wb.save('miData_2.xlsx')

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return {}


if __name__ == '__main__':
    listaPersonas()
