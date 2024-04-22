import os
import time

#Pages
pages = ["Menu", "Depósito", "Saque", "Extrato", "Banco=Global=Finance"]
withdraw_qty_max = 3; withdraw_limit_max = 500; withdraw_qty = 3; withdraw_limit = 500
balance = 0; deposit = 0
extract = ""

# Functions
def display_pages(x):
    os. system('cls')
    print(pages[x].center(100,"="))

def display_extract(a, b, c):
    spaces = (100 - len(a) - len(b) - len(c)) // 6
    print("=" * 100)
    print(f"{' ' * spaces}{a}{' ' * spaces}|{' ' * spaces}{b}{' ' * spaces}|{' ' * spaces}{c}{' ' * spaces}")
    print("=" * 100)
    if extract == "3":
        print("Não foram realizadas movimentações")
    else:
        print(extract)
    print("=" * 100)
    print(f"Saldo disponível: R$ {balance:.2f}")
    print("Fim".center(100,"="))

def include_extract(option):
    global extract
    if option == 1:
        extract += f"{' ' * 9}{time.strftime('%d/%m/%y %X')}{' ' * 9}|{' ' * 13}Depósito{' ' * 13}|{' ' * 10}R$ {deposit:.2f}{' ' * 10}\n"
    if option == 2:
        extract += f"{' ' * 9}{time.strftime('%d/%m/%y %X')}{' ' * 9}|{' ' * 14}Saque{' ' * 15}|{' ' * 9}(R$ {withdraw:.2f}){' ' * 9}\n"

def impress(y, z):
    print(f"\nOperação realizada com sucesso! \n{y}: R$ {z:.2f}")    

def invalid_operation(i):
    print(f"System: Operação inválida, {i}.")
    time.sleep(3)
    option = ""

def repeat(option):
    while True:
        response = input("\nSystem: Deseja realizar outra operação?\n[s] sim ou [n] não\n=> ").lower()
        if response in ("sim", "s"):
            return True
        elif response in ("não", "n"):
            exit()
        else:
            os. system('cls')
            display_pages(option)
            print("\nSystem: Por favor, digite 'sim' ou 'não'")
            continue

#Welcome
print("=" * 100)
print(pages[4].center(100,"="))
print("=" * 100)
print("System: Seja bem-vindo")
time.sleep(5)
while True:
#Menu
    os. system('cls')
    print(pages[0].center(100,"="))
    menu = f'''
    1 Depósito 
    2 Saque
    3 Extrato
    '''
    print(menu)
    option = input("System: Informe o nº da opção desejada:\n=> ").strip()
    if option.replace(",", "").isdigit():
        option = int(option)
        if(option > 0 and option <=3):           
#Deposit
            if option == 1:
                display_pages(option)
                deposit = input("System: Informe o valor do depósito:\n=> ").strip()
                if deposit.replace(",", "").isdigit():
                    deposit = float(deposit.replace(',', '.'))
                    if deposit > 0:
                        balance += deposit
                        include_extract(option)
                        impress("Depósito", deposit)
                        repeat(option)
                    else:
                        print("\nSystem: Operação não realizada! Tente novamente com um número positivo")
                        time.sleep(5)
                else:
                    invalid_operation("permitido apenas valores positivos")
#Withdraw
            if option == 2:
                display_pages(option)
                withdraw = input("System: Informe o valor do saque:\n=> ").strip()
                if withdraw.replace(",", "").isdigit():
                    withdraw = float(withdraw.replace(',', '.'))
                    if withdraw_qty > 0 and withdraw_qty <= withdraw_qty_max:
                        if withdraw <= withdraw_limit :
                            if withdraw <= balance:
                                withdraw_qty -= 1
                                withdraw_limit -= withdraw
                                balance -= withdraw
                                include_extract(option)
                                impress("Saque", withdraw)
                                repeat(option)
                            else:
                                print("\nSystem: Operação não realizada! Saldo Insuficiente")
                                time.sleep(5)
                        else:
                            print(f"\nSystem: Operação não realizada! Você excedeu o Limite Diário de Valor de Saques disponíveis: R$ {withdraw_limit:.2f}")
                            print(f"System: Caso desejar aumentar o limite, contate seu Gerente")
                            time.sleep(10)
                    else:
                        print(f"\nSystem: Operação não realizada! Você excedeu o Limite Diário de Quantidade de Saques: {withdraw_qty_max}")
                        print(f"System: Caso desejar aumentar o limite, contate seu Gerente")
                        time.sleep(10)
                else:
                    invalid_operation("permitido apenas valores positivos")
#Extract
            if option == 3:
                display_pages(option)
                print("System: Segue abaixo o histórico das movimentações:\n")
                display_extract("Data/hora", "Operação", "Valor")
                repeat(option)
        else:
            invalid_operation("informe o número de uma das operações acima")
    else:
        invalid_operation("permitido apenas números positivos")
