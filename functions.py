#import de bibliotecas
import random
# declaração de variaveis globais
size = 20
n_agendamento = 0
problema  = "vago"
modelo_carro = "vago"
data = "07/05/2024"
data0 = "07/05/2024"
data1 = "23/05/2024"
data2 = "30/05/2024"
# Função para desenhar um quadrado com o tamanho especificado, para utilizar como foto
def foto(size):
    print("\n\tTire uma foto do problema do carro")
    for i in range(10):
        print("\t\t\t\t\t\t\t\t",'*' * size)
    print("\n\tObrigado!")

# Função para agendar e forncer o codigo de agendamento
def agendamento(tipo_problema):
    inf = input("\n\t Gostaria de agendar com nossos mecanicos?(sim ou não):")
    if inf == "sim":
        ramdom = random.randint(1,100)
        n_agendamento = int(ramdom) 
        print(f"\n\tOK foi agendado! Seu numero de agendamento é {n_agendamento}")
        print(f"\tAgora vá/ou retorne a pagina de agendamento e digite seu numero de\n\t agendamento para informações")
        return n_agendamento
    elif inf == "não":
        print("\tOK, até a proxima!")
    else:
        print("\tDigite sim ou não.")
        agendamento(tipo_problema)
        
# Função para definir o problema e o codigo
def tipo_problema_():
    tipo = input("Escolha 1 - Poblema Motor | 2 - Problema Transmissão | 3 - Falha Elétrica | 4 - Problemas freios: ")
    match tipo:
        case '1':
            foto(20)
            print("\n\t Certo!Segundo a foto tirada o problema é de superaquecimento do carro,\n\t pode ser um problema sério, pois pode danificar o motor e outros \n\tcomponentes importantes do veículo...")
            problema = "Poblema Motor"
            n_agendamento = agendamento(problema)
            return str(n_agendamento), problema
        case '2':
            foto(20)
            print("\n\t Certo!Segundo a foto tirada o problema é de dificuldade de troca de marcha,\n\t será necessário uma troca dos sincronizadores desgastados...")
            problema = "Problema Transmissão"
            n_agendamento = agendamento(problema)
            return str(n_agendamento), problema
        case '3':
            foto(20)
            print("\n\t Certo!Segundo a foto tirada o problema é da bateria do carro\n\t será necesserio troca...")
            problema = "Falha Elétrica"
            n_agendamento = agendamento(problema)
            return str(n_agendamento), problema
        case '4':
            foto(20)
            print("\n\t Certo!Segundo a foto tirada o problema está no desgaste das pastilhas,\n\t será necesserio troca...")
            problema = "Problemas freios"
            n_agendamento = agendamento(problema)
            return str(n_agendamento), problema
        case _:
            print("Escolha entre 1, 2, 3 ou 4")
            tipo_problema_()

# Função para cancelar agendamento
def cancelar_agendamento(n_agendameto):
    confirm = input("\tGostaria de cancelar seu agendamento?(sim ou não):")
    if confirm == "sim":
        print("\tCancelamento realizado com sucesso!")
        print("-" * 88)
        print("\n")
        return 0
    elif confirm == "não":
        print("OK, até!")
        print("-" * 88)
        print("\n")
        return n_agendameto
    else:
        input("Informação inválida ")
        return n_agendameto

# Função para mudar data de agendamento
def mudar_data(data,data1,data2,data0,problema,modelo_carro):
    print(f"\n\tInformações do agendamento:\n\t\t -Data: {data}\n\t\t -Modelo do carro: {modelo_carro}\n\t\t -Problema: {problema} \n\t\t -Mecânica: Seu Zê")
    confirm_data = input("\n\tGostaria de mudar a data?(sim ou não):")
    if confirm_data == "sim":
        print(f"\tOK, temos essas datas disponiveis: \n\t1 -{data1} \n\t2 -{data2}")
        ok = int(input("\tEscolha entre uma das novas datas(1 ou 2) ou digite 0 para manter a data: "))
        match ok:
            case 0:
                mudar_data(data,data1,data2,data0,problema,modelo_carro)
            case 1:
                data = data1
                data1 = data0
                mudar_data(data,data1,data2,data0,problema,modelo_carro)
            case 2:
                data = data2
                data2 = data0
                mudar_data(data,data1,data2,data0,problema,modelo_carro) 
            case _:
                print("\tEscolha entre 0, 1 ou 2")
                mudar_data(data,data1,data2,data0,problema,modelo_carro)
                
    elif confirm_data == "não": 
        print(f"\tOK!")
    else:
        print(f"\tEscreva sim ou não")
        mudar_data(data,data1,data2,data0,problema,modelo_carro)
                    
# Função para Duvidas
def duvidas():
     duv = input("Escolha 1, 2, 3, 4 ou 0 caso não queira tirar nenhuma duvida:")
     match duv:
        case '0':
            print("OK, até!")
            print("-" * 88)
            print("\n")
            return 0
        case '1':
            print("\n\tCerto!Entre na pagina Mecânico Virtual, faça um diagnostico de seu \n\tproblema. Marque uma consulta e grave seu numero de agendameto para poder \n\tver suas informações.")
            confirm = input("\n\tGostaria de tirar mais alguma duvida?(sim ou não): ")
            if confirm == "sim":
                    print("-" * 88)
                    print("\n")
                    return 4
            elif confirm == "não":
                    print("OK, até!")
                    print("-" * 88)
                    print("\n")
                    return 0
            else:
                    input("Informação inválida ")
                    return 0
        case '2':
            print("\n\tCerto!É possivel cancelar seu agendamento na pagina AGENDAMENTO.")
            confirm = input("\n\tGostaria de tirar mais alguma duvida?(sim ou não): ")
            if confirm == "sim":
                    print("-" * 88)
                    print("\n")
                    return 4
            elif confirm == "não":
                    print("OK, até!")
                    print("-" * 88)
                    print("\n")
                    return 0
            else:
                    input("Informação inválida ")
                    return 0
        case '3':
            print("\n\tCerto!Entre na pagina de AGENDAMENTO, coloque seu numero de agendamento \n\te escolha a opção CANCELAR AGENDAMENTO escrevendo cancelar no indicado;")
            confirm = input("\n\tGostaria de tirar mais alguma duvida?(sim ou não): ")
            if confirm == "sim":
                    print("-" * 88)
                    print("\n")
                    return 4
            elif confirm == "não":
                    print("OK, até!")
                    print("-" * 88)
                    print("\n")
                    return 0
            else:
                    input("Informação inválida ")
                    return 0
        case '4':
            print("\n\tCerto!É apenas possivel realizar 1 agendamento por vez e então \n\tvizualizalo na pagina de AGENDAMENTO.")
            confirm = input("\n\tGostaria de tirar mais alguma duvida?(sim ou não): ")
            if confirm == "sim":
                    print("-" * 88)
                    print("\n")
                    return 4
            elif confirm == "não":
                    print("OK, até!")
                    print("-" * 88)
                    print("\n")
                    return 0
            else:
                    input("Informação inválida ")
                    return 0
        case _:
            duvidas()
