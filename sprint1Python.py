import random
pagina = 0
size = 20
n_agendamento = 0
problema  = "vago"
modelo_carro = "vago"
# Função para desenhar um quadrado com o tamanho especificado, para utilizar como foto
def foto(size):
    print("\n\tTire uma foto do problema do carro")
    for i in range(10):
        print("\n\t\t\t\t\t\t\t\t",'*' * size)
    print("\n\tObrigado!")

def agendamento(tipo_problema):
    inf = input("\n\t Gostaria de agendar com nossos mecanicos?(sim ou não):")
    if inf == "sim":
        ramdom = random.randint(1,100)
        n_agendamento = ramdom 
        print(f"\n\tOK foi agendado! Seu numero de agendamento é {n_agendamento}")
        print(f"\tAgora vá/ou retorne a pagina de agendamento e digite seu numero de\n\t agendamento para informações")
    elif inf == "não":
        print("\tOK, até a proxima!")
    else:
        print("\tDigite sim ou não.")
        agendamento(tipo_problema)
        
def tipo_problema_():
    tipo = input("Escolha 1 - Poblema Motor | 2 - Problema Transmissão | 3 - Falha Elétrica | 4 - Problemas freios: ")
    match tipo:
        case '1':
            print
            foto(20)
            print("\n\t Certo!Segundo a foto tirada o problema é de superaquecimento do carro,\n\t pode ser um problema sério, pois pode danificar o motor e outros \n\tcomponentes importantes do veículo...")
            problema = "Poblema Motor"
            agendamento(problema)
        case '2':
            print
            foto(20)
            print("\n\t Certo!Segundo a foto tirada o problema é de dificuldade de troca de marcha,\n\t será necessário uma troca dos sincronizadores desgastados...")
            problema = "Problema Transmissão"
            agendamento(problema)
        case '3':
            print
            foto(20)
            print("\n\t Certo!Segundo a foto tirada o problema da bateria do carro\n\t será necesserio troca...")
            problema = "Falha Elétrica"
            agendamento(problema)
        case '4':
            print
            foto(20)
            print("\n\t Certo!Segundo a foto tirada o problema está no desgaste das pastilhas,\n\t será necesserio troca...")
            problema = "Problemas freios"
            agendamento(problema)
        case _:
            print("Escolha entre 1, 2, 3 ou 4")
            tipo_problema_()


while pagina == 0:
    print("\n")
    print("-" * 88)
    print("|*Logo*  HOME  MV  AGENDAR  SOBRE NÒS     (Digíte sua pergunta...   ) *INCONE PERGUNTA*|")
    print("-" * 88)
    print("\n")
    print("\t","-" * 65)
    print("\t PROJETO")
    print("\t  O projeto “Mecânico Virtual” é uma solução criada com \n\t  o intuito de facilitar a comunicação entre cliente e profissional, \n\t  como também tornar todo o processo mais simples, \n\t  com ambas as partes tendo suas necessidades atendidas o tempo todo.")
    print("\n")
    print ("Gostaria de entrar em uma das outras paginas?")
    opcao = int(input("Escolha 1 - MECÂNICO VIRTUAL | 2 - AGENDAR | 3 - SOBRE NÓS | 4 - FAZER PERGUNTA | 5 - ENCERRAR SESSÃO: "))
    
    match opcao:
        case 1:
           pagina = 1
           while pagina == 1: 
               print("-" * 88)
               print("\n")
               print("-" * 88)
               print("|*Logo*  HOME  MV  AGENDAR  SOBRE NÒS     (Digíte sua pergunta...   ) *INCONE PERGUNTA*|")
               print("-" * 88)
               print("\n")
               print("\t","-" * 65)
               print("\t\t\t MECÂNICO VIRTUAL")
               print("\n\tOlá, sou seu mecânico virtual.")
               modelo_carro = input("\n\tDigite o modelo de seu carro: ")
               print("\n\t Aqui estão alguns problemas em que posso te ajudar: ")
               print("\n\t 1 - Problemas de Motor: \n\t\t - Falhas de ignição, superaquecimento, problemas com a \n\t\tbateria ou falhas no sistema de injeção de combustível.")
               print("\n\t 2 - Problemas de Transmissão: \n\t\t - Dificuldades para engatar as marchas ou ruídos \n\t\testranhos durante as mudanças.")
               print("\n\t 3 - Falhas no Sistema Elétrico: \n\t\t - Falhas na bateria, alternador ou arranque.\n\t\tProblemas com sistemas de iluminação, sensores, \n\t\tsistemas de som e outros componentes eletrônicos.")
               print("\n\t 4 - Problemas no Sistema de Freios: \n\t\t - Desgaste nas pastilhas ou discos de freio,\n\t\t vazamentos no sistema hidráulico, ou falhas \n\t\t no sistema de assistência de frenagem.")
               print("\n")
               tipo_problema_()
               pagina = 0
                        
        case 2: 
           pagina = 2
           while pagina == 2: 
               print("-" * 88)
               print("\n")
               print("-" * 88)
               print("|*Logo*  HOME  MV  AGENDAR  SOBRE NÒS     (Digíte sua pergunta...   ) *INCONE PERGUNTA*|")
               print("-" * 88)
               print("\n")
               print("\t","-" * 65)
               print("\t\t\t AGENDAMENTO")
               n = int(input("\n\t Olá, qual seu numero de agendamento? (se não tiver um, digite 0)"))
               if n == 0:
                    print("\n\tVá até a pagina de Mecânico virtual para fazermos um diagnostico \n\tdo seu problema:")
                    pagina = 0
               elif n == n_agendamento:
                   data = "07/05/2024"
                   print(f"\n\tInformações do agendamento:\n\t\t -Data: {data}\n\t\t -Modelo do carro: {modelo_carro}\n\t\t -Problema:{problema} \n\t\t -Mecânica: Seu Zê")
               else:
                   print("\n\tTipo de infomação não aceitavel!") 
                   pagina = 0
               data = input("Gostaria de mudar a data?(sim ou não)")
               if data == "sim":
                   data1 = "23/05/2024"
                   data2 = "30/05/2024"
                   
                    
                    
                   
                   

        case 5:
            print("Encerrando...")
            break
        

        case _:

            print("\n")
            print("Opção invalida!")
            print("Escolha um das opções: 1 ou 2 ou 3.")