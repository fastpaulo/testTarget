value = input("Digite um valor: ")

def fibonacci():
    sequence = [0, 1]
    while len(sequence) < 200:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

result = fibonacci()
print(result)
if int(value) in result:
    print("Esse numero faz parte da sequencia Fibonacci")
else:
      print("Esse numero não faz parte da sequencia Fibonacci")