import os
import json

with open("tarefas.json", "r",encoding="utf-8") as arquivo:
    tarefas = json.load(arquivo)

def mostrar_tarefas():
    barra = f'|{60*'-'}|'
    print(barra)
    print("TAREFAS ATUAIS")
    print(barra)
    for i in range(len(tarefas['tarefas'])):
        print(f'|Tarefa {i+1} - {tarefas['tarefas'][i]} ({tarefas['datas']{i}))')
    print(barra)
    input("Aperte enter para continuar.")

def adicionar_tarefas():
    barra = f'|{60* '-'}'
    print(barra)
    tarefa = input("digite o nome da tarefa")
    data = input("digite a data: ")
    tarefas['tarefas'].append(tarefa)
    tarefas[datas].append(data)

    with open("tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)

    print(barra)
    print(f"| Tarefa ({tarefa}) adicionada com sucesso!")
    print(barra)
    input("|Aperte entrar para continuar.")

def mostra_menu()
    while True:



def remover_tarefa():
    barra = f'|{60*'-'}|'
    print(barra)
    print("|REMOVER TAREFA")
    print(barra)
    print("REMOVER TAREFA ")
    print(barra)
    for i in range(len(tarefas['tarefas'])):
        print(f'|tarefa {i - {tarefas['tarefas']} (tarefas['datas'][i]})')
    print (barra)
    thy:
        id_tarefa = int(input('|Digite o numero da tarfa que deseja remover: '))
        if id_tarefa >0:
        tarefa = tarefas ['tarefas'].pop(id_tarefa-1)
        tarefas['datas'].pop(id_tarefa-1)
    else:
        print('|ID invalido!')
    print(f'| tarefa ({tarefa)} removida com sucesso!')

    with open ("tarefas.json","w", encoding="utf-8") as arquivo:
            json.dump(tarefas, arquivo, indent=4 ensure_ascii=false)

       except:
       print("|ERRO! tente novamente.")

    input("|Aperte entrar para continuar.")


def mostrar_menu():
    while True:
        os.system('cls')
        barra = f'| {60* '-'}'
        print(barra)
        print("| GERENCIADOR DE TAREFAS ")
        print(barra)
        print("| 1 - Mostrar tarefas")
        print("| 2 - Adicionar tarefas")
        print("| 3 - Remover tarefa")
        print("| 4 - Sair")
        print(barra)
        opc = input("|informe a opcao desejada: ")

        if opc == '1':
            os.system('cls')
            mostrar_tarefas()

        elif opc == '2':
            os.system('cls')
            adicionar_tarefas()

        elif opc == '3':
            os.system('cls')
            remover_tarefa()

        elif opc == '4':
            print("saindo...")
            break 

        else:
            print("ERRO! Escolha uma opçao valida.")
            input("Aperte enter para continuar.")



mostrar_menu()