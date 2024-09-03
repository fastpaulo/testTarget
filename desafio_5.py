palavra = input('Digite a palavra que voce quer inverter: ')

def inversao():
 novaValor = ""
 for inverter in palavra.split(" "):
      novaValor += inverter[::-1]
 return novaValor

resultado = inversao()
print("A palavra inveritida fica: ", resultado)