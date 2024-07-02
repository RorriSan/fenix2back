import pprint

from modelos import Cliente

#cliente = Cliente('Rodrigo', 'Santos', '1187587458', 'rodrigo.santos@gmail.com', 'rodri8', '1357$')
#cliente.guardar_db()

pp = pprint.PrettyPrinter(indent=4)

datos = Cliente.obtener_todos()
pp.pprint(datos)