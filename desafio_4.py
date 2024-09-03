
sp = 67.836
rj = 36.678
mg = 29.229
es = 27.165
outros = 19.849
valorTotal=180.756


resultado = (100*outros)/valorTotal
opcao = -1
while opcao != 0:
 opcao = int(input("[1] SP \n[2] RJ \n[3] MG \n[4] ES \n[5] Outros \n[0] Sair \n: "))
 if opcao == 1:
  resultado = (100*sp)/valorTotal
  print("o percentual de representação do estado SP:  {:.0f}%".format(resultado) )
 elif opcao == 2:
  resultado = (100*rj)/valorTotal
  print("o percentual de representação do estado RJ:  {:.0f}%".format(resultado) )
 elif opcao == 3:
  resultado = (100*mg)/valorTotal
  print("o percentual de representação do estado MG:  {:.0f}%".format(resultado) )
 elif opcao == 4:
  resultado = (100*es)/valorTotal
  print("o percentual de representação do estado ES:  {:.0f}%".format(resultado) )
 elif opcao == 5:
  resultado = (100*outros)/valorTotal
  print("o percentual de representação para outros estados:  {:.0f}%".format(resultado) )
 elif opcao == 0:
  break
