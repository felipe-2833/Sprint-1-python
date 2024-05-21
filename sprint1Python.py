#Import das funções
from functions import *
#variaveis globais
pagina = 0
size = 20
n_agendamento = 0
problema  = "vago"
modelo_carro = "vago" 
data = "07/05/2024"
data0 = "07/05/2024"
data1 = "23/05/2024"
data2 = "30/05/2024"              

#PAGINA PRINCIPAL/ HOME
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
    opcao = input("Escolha 1 - MECÂNICO VIRTUAL | 2 - AGENDAR | 3 - SOBRE NÓS | 4 - FAZER PERGUNTA | 5 - ENCERRAR SESSÃO: ")
    
    match opcao:
        #MECÂNICO VIRTUAL 
        case "1":
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
               n_agendamento, problema = tipo_problema_()
               pagina = 0
        
        #AGENDAR                
        case "2": 
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
               n = input("\n\t Olá, qual seu numero de agendamento? (se não tiver um, digite 0):")
               if n == "0":
                    print("\n\tVá até a pagina de Mecânico virtual para fazermos um diagnostico \n\tdo seu problema:")
                    pagina = 0
               elif n == n_agendamento:
                    data = mudar_data(data,data1,data2,data0,problema,modelo_carro)
                    
                    n_agendamento = cancelar_agendamento(n_agendamento)
                    pagina = 0        
               else:
                   print("\n\tTipo de infomação não aceitavel!") 
                   pagina = 0
        
        #SOBRE NÓS
        case "3":
            pagina = 3
            while pagina == 3: 
               print("-" * 88)
               print("\n")
               print("-" * 88)
               print("|*Logo*  HOME  MV  AGENDAR  SOBRE NÒS     (Digíte sua pergunta...   ) *INCONE PERGUNTA*|")
               print("-" * 88)
               print("\n")
               print("\t","-" * 65)
               print("\t\t\t SOBRE NÓS")
               print("\n\t|*LOGO*  ANDRÉ GERALDI MARCOLONGO      RM555285|")
               print("\n\t|*LOGO*  SAMIR HAGE NETO               RM555285|")
               print("\n\t|*LOGO*  FELIPE LEVY STEPHENS FIDELIX  RM556426|")
               confirm = input("\nVoltar para HOME?(Escreva sim para voltar): ")
               if confirm == "sim":
                    print("-" * 88)
                    print("\n")
                    pagina = 0
               else:
                    input("Informação inválida ")
                    pagina = 3
        
        #FAZER PERGUNTA
        case "4":
            pagina = 4
            while pagina == 4: 
               print("-" * 88)
               print("\n")
               print("-" * 88)
               print("|*Logo*  HOME  MV  AGENDAR  SOBRE NÒS     (Digíte sua pergunta...   ) *INCONE PERGUNTA*|")
               print("-" * 88)
               print("\n")
               print("\t","-" * 65)
               print("\t\t\t DUVIDAS")
               print("\n\tOlá sou seu assistente virtual, como posso te ajudar?")
               print("\n\t Aqui estão alguns problemas em que posso te ajudar: ")
               print("\n\t 1 - Como agendar um serviço?: ")
               print("\n\t 2 - Quais são as políticas de cancelamento e reembolso?: ")
               print("\n\t 3 - Como faço para alterar ou cancelar um agendamento existente?: ")
               print("\n\t 4 - Como posso visualizar ou gerenciar meus agendamentos futuros?: ")
               print("\n")
               pagina = duvidas()
               
        #ENCERRAR SESSÃO      
        case "5":
            print("Encerrando...")
            break
    
        #Caso opção errada    
        case _:

            print("\n")
            print("Opção invalida!")
            print("Escolha um das opções: 1, 2, 3, 4 ou 5.")
            print("-" * 88)
            continue