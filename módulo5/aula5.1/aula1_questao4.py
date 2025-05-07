from datetime import datetime
atual= datetime.now()
data= atual.strftime("Data: %d/%m/%Y")
hora= atual.strftime("Hora: %H:%M")
print(data)
print (hora)