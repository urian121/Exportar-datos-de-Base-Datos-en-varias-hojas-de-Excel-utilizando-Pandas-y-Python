import pandas as pd
import mysql.connector
import openpyxl


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


def listaUsers():
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as mycursor:
                querySQL = "SELECT * FROM registros"
                mycursor.execute(querySQL,)
                resumen_consignaciones_diarias = mycursor.fetchall()
                return resumen_consignaciones_diarias
    except Exception as e:
        print(f"Ocurrió un error leyendo la consignación: {e}")
        return {}


def hojaUsuarios(lista_usuarios, wb):
    hoja = wb.create_sheet(title="Usuarios")
    hoja.append(('id', 'nombre', 'profesion', 'status'))
    for usuario in lista_usuarios:
        hoja.append((usuario['id'], usuario['nombre'],
                    usuario['profesion'], usuario['status']))


def resumenConsignacionesRecibidas():
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as mycursor:
                querySQL = "SELECT * FROM personas"
                mycursor.execute(querySQL,)
                resumen_consignaciones_diarias = mycursor.fetchall()

                wb = openpyxl.Workbook()

                hoja = wb.active
                hoja.title = "Consignaciones"
                # Crea la fila del encabezado con los títulos
                hoja.append(('id', 'Nombre', 'Sexo', 'email'))
                for consignacion in resumen_consignaciones_diarias:
                    # Agrega una tupla con los valores de la consignación
                    hoja.append((consignacion['id_persona'], consignacion['nombre'],
                                consignacion['sexo'], consignacion['email']))

                # Crea una hoja de Excel para los usuarios
                lista_usuarios = listaUsers()
                hojaUsuarios(lista_usuarios, wb)

                # Guarda el archivo Excel
                wb.save('resumen_consignaciones_diarias.xlsx')

    except Exception as e:
        print(f"Ocurrió un error leyendo la consignación: {e}")
        return {}


if __name__ == '__main__':
    resumenConsignacionesRecibidas()
