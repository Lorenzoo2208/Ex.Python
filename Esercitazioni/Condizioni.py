#Esercitazione Condizioni

numero = 7
tentativo = int(input("indovina il numero ( tra 1 e 10):"))
if tentativo == numero:
    print("hai indovinato il numero.")
elif tentativo > numero:
    print("il numero è troppo alto.")
else:
    print("il numero è troppo basso.")    



