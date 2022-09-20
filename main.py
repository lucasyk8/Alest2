import queue

#abre o txt
with open('casosdeteste.txt', 'r') as file:
    saida = open('saida_T1.txt', 'w')
    copia = file.readlines()
    for i in range(len(copia)):
            #le por linha o txt
            if i%4 == 0: 
                primeira = copia[i].replace('\n','').split()
            elif i%4 == 1:
                segunda = copia[i].replace('\n','').split()
            elif i%4 == 2:
                terceira = copia[i].replace('\n','').split()
            else:     
                #print(primeiraL)
                #print(segundaL)
                #print(terceiraL)
                #ajeita os valores para que sejam listas unicas
                capacidade = [eval(i) for i in primeira] 
                agua = [eval(i) for i in segunda]
                desejada = [eval(i) for i in terceira]
                #print(capacidade)
                #print(agua)
                #print(desejada)

                #se todos estivererm no desejado então não é executado movimentos
                if agua[0] == desejada[0] and agua[1] == desejada[1] and agua[2] == desejada[2]:
                    saida.write(str(capacidade[0])+' '+str(capacidade[1])+' '+str(capacidade[2])+"\n")
                    saida.write(str(agua[0])+' '+str(agua[1])+' '+str(agua[2])+"\n")
                    saida.write(str(desejada[0])+' '+str(desejada[1])+' '+str(desejada[2])+"\n")
                    saida.write("Movimentos: 0"+"\n")
                else: 

                    #verifica se nenhum dos 3 jarros possui tamanho maior que 40, como 
                    #especificado nenhum dos 3 jarros pode ser maior que 40
                    if capacidade[0] > 40 or capacidade[1] > 40 or capacidade[2] > 40:
                        saida.write("jarro so pode ter ate tamanho 40"+"\n")
                    else:

                        #verifica se o estado desejado não é maior que a capacidade se sim é impossivel resolver
                        if desejada[0] > capacidade[0] or desejada[1] > capacidade[1] or desejada[2] > capacidade[2]:
                            saida.write("Impossivel"+"\n")
                        else:

                            #verifica se a soma do que é desejado não é diferente da quantidade de água se sim é impossivel 
                            if sum(desejada) != sum(agua):
                                saida.write("Impossivel"+"\n")
                            else:

                                procurando = True

                                #cria a fila para armazenar agua e número de movimentos
                                moves = queue.Queue()
                                moves.put({
                                    "movimentos": 0,
                                    "jarros": agua
                                })

                                #procura para chegar no estado desejado, gravando o número de movimentos feitos 
                                estadosTestados = set()
                                while procurando:
                                    atual = moves.get()
                                    for i in range(3):
                                        for j in range(3):
                                            #testa se jarros diferentes, então faz uma cópia armazenando jarros e o número de movimentos
                                            if i != j:
                                                jarros = atual["jarros"].copy()
                                                # jarros[i].pour(jarros[j])

                                                #testa se jarros maior que capacidade e se sim executa movimentos e grava em jarros
                                                if jarros[i] + jarros[j] > capacidade[j]:
                                                    jarros[i] = jarros[i] - (capacidade[j] - jarros[j])
                                                    jarros[j] = capacidade[j]
                                                else:
                                                    jarros[j] = jarros[i] + jarros[j]
                                                    jarros[i] = 0
                                                
                                                #testa se está em estados desejados e escreve no txt,então finaliza o programa
                                                if jarros[0] == desejada[0] and jarros[1] == desejada[1] and jarros[2] == desejada[2]:
                                                    procurando = False
                                                    saida.write(str(capacidade[0])+' '+str(capacidade[1])+' '+str(capacidade[2])+"\n")
                                                    saida.write(str(agua[0])+' '+str(agua[1])+' '+str(agua[2])+"\n")
                                                    saida.write(str(desejada[0])+' '+str(desejada[1])+' '+str(desejada[2])+"\n")
                                                    saida.write("Movimentos: "+ str(atual["movimentos"] + 1)+"\n")
                                                    break
                                                #testa se a tentativa testada ja foi testada antes se não adiciona em jarros 
                                                if (str(jarros) not in estadosTestados and  atual["movimentos"] + 1):
                                                    estadosTestados.add(str(jarros))
                                                    #print(atual["movimentos"] + 1, jarros)

                                                    moves.put({
                                                        "movimentos": atual["movimentos"] + 1,
                                                        "jarros": jarros
                                                    })

                                        #print(atual["movimentos"] + 1, moves.qsize())
                                        
                                    #se menor que 0 então é impossivel pois o número de movimentos será negativo
                                    if (moves.qsize() <= 0):
                                        saida.write("Impossivel"+"\n")
                                        procurando = False

saida.close()
file.close()





