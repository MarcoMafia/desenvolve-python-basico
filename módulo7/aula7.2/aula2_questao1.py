data = input("Digite uma data de nascimento (dd/mm/aaaa): ")
lista_data = data.split("/")
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio",
 "Junho", "Julho", "Agosto", "Setembro", "Outubro",
 "Novembro", "Dezembro"]
mes_extenso = meses[int(lista_data[1])-1]
print("Você nasceu em " +lista_data[0] + " de " + mes_extenso + " de " + lista_data[2])