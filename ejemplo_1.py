import pandas as pd


data_1 = pd.DataFrame(
    [['Urian', 123], ['Brenda', 321]],
    columns=["Nombre", "Telefono"]
)

data_2 = pd.DataFrame(
    [[15, 21], [41, 11]],
    columns=["Rank", "Subjects"]
)

print(data_1)
print(data_2)

# Agregar el parámetro de index= False para eliminar índice de la salida
# Escribir datos en mi hoja de excel, tambien podemos cambiar el nombre de nuestra hoja aqui en sheet_name
with pd.ExcelWriter('miData_1.xlsx') as writer:
    data_1.to_excel(writer, sheet_name='Hoja N° 1', index=False)
    data_2.to_excel(writer, sheet_name='Hoja N° 2', index=False)
