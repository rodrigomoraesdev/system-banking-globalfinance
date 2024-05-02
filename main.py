import os
import time

# Functions
def to_start():
    print("=" * 100)
    header(-1)
    print("=" * 100)
    print("System: Seja bem-vindo.")
    time.sleep(3)

def header(header):
    pages = ["Menu", "Criar Usuário", "Criar Conta", "Listar Usuário/Conta", "Depósito", "Saque", "Extrato", "Banco=Global=Finance"]
    if header != -1:
        os. system('cls')
    print(pages[header].center(100,"="))

def repeat(option):
    while True:
        again = input("\nSystem: Deseja realizar outra operação?\n[s] sim ou [n] não\n=> ").lower()
        if again in ("sim", "s"):
            return True
        elif again in ("não", "n"):
            exit()
        else:
            header(option)
            print("\nSystem: Por favor, digite 'sim' ou 'não'")
            continue

def menu():
    header(0)
    menu = '''
    1\tCriar Usuário
    2\tCriar Conta
    3\tListar Usuário/Conta
    4\tDepósito 
    5\tSaque
    6\tExtrato
    
    System: Informe o nº da opção desejada:
    ⇒ '''
    return input(menu)

def validation(value):
    if value.startswith("-"):
        print("Operação Inválida".center(100,"|"),f"\nSystem: Favor informe um Número Positivo.")
        return 0
    
    elif value.replace(",", ".").replace(".", "").isdigit():
        value = float(value.replace(".", "").replace(",", "."))
        return value
    else:
        print("Operação Inválida".center(100,"|"),f"\nSystem: Favor informe um Número.")
        return 0

def new_user(users, option):
    header(1)
    cpf = input ("System: Favor informe o CPF do usuário:\n⇒ ").strip().replace(".","").replace("-","")
    user = filter_users(cpf, users)

    if user:
        print("Operação Inválida".center(100,"|"),f"\nSystem: CPF informado já cadastrado.")
        repeat(option)
        return

    name = input("\nSystem: Informe o nome completo:\n⇒ ").strip()
    birth_date = input("\nSystem: Informe a data de nascimento (dd-mm-aaaa):\n⇒ ").strip()
    address = input("\nSystem: Informe o endereço (logradouro, nrº - bairro - cidade/sigla estado):\n⇒ ").strip()

    header(1)
    user_created = {"name":name, "birth_date": birth_date, "cpf": cpf, "address": address}
    print("Operação Concluída".center(100,"-"),f"\nSystem: Usuário criado com sucesso:")
    for i, value in user_created.items():
        print(f"{i.capitalize()}: {value}")

    users.append(user_created)
    repeat(option)

def filter_users(cpf, users):
    filter_user = [user for user in users if user["cpf"] == cpf]
    return filter_user[0] if filter_user else None

def new_account(agency, number_account, users, option):
    header(2)
    cpf = input ("System: Favor informe o CPF do usuário:\n⇒ ").strip().replace(".","").replace("-","")
    user = filter_users(cpf, users)

    if user:
        account_created = {"agency": agency, "number_account": number_account, "user": user}
        print("Operação Concluída".center(100,"-"),f"\nSystem: Conta criada com sucesso:")
        for i, value in account_created.items():
            if i == 'user':
                print(f"{i.capitalize()} - CPF: {value['cpf']}")
            else:
                print(f"{i.capitalize()}: {value}")

        repeat(option)
        return account_created
    
    print("Operação Inválida".center(100,"|"),f"\nSystem: Usuário não encontrado.")
    repeat(option)
    
def list_accounts(accounts, option):
    header(3)
    if not accounts:
        print("System: Nenhuma conta foi registrada.")
    for i in accounts:
        line = f'''
            Agência:\t{i['agency']}
            Conta:\t{i['number_account']}
            Titular:\t{i['user']['name']}
            '''
        print("-" * 100,"\n",line)
    repeat(option)

def deposit(balance, value, option, extract, /):
    if value > 0:    
        balance += value
        print("Operação Concluída".center(100,"-"),f"\nSystem: Valor Depositado: R$ {value:.2f}")
        extract = include_impress(value, extract, option)
    return balance, extract

def withdraw(*, balance, value, option, extract, limit_value_withdraw, limit_qtd_withdraw, qtd_withdraw,):
        exceeded_balance = value > balance
        exceeded_value_limit = value > limit_value_withdraw
        exceeded_qtd_limit = qtd_withdraw >=  limit_qtd_withdraw

        if exceeded_balance:
            print("Operação Inválida".center(100,"|"),"\nSystem: Você não possui saldo suficiente.")

        elif exceeded_value_limit:
            print("Operação Inválida".center(100,"|"),f"\nSystem: O valor informado excede o limite de saque diário de R$ {limit_value_withdraw:.2f}.")
        
        elif exceeded_qtd_limit:
            print("Operação Inválida".center(100,"|"),f"\nSystem: A quantidade excede o limite de saque diário de {limit_qtd_withdraw}x.")

        elif value > 0:
            balance -= value
            qtd_withdraw += 1
            extract = include_impress(value, extract, option)
            print("Operação Concluída".center(100,"-"))
            print(f'Valor Saque: R$ {value:.2f}')

        return balance, extract, qtd_withdraw

def include_impress(value,extract, option):
    if option == 4:
        extract += f"\t    {time.strftime('%d/%m/%y %X')}\t\t\tDepósito\t\t\t R$ {value:.2f}\n"
    if option == 5:
        extract += f"\t    {time.strftime('%d/%m/%y %X')}\t\t\tSaque\t\t\t\t(R$ {value:.2f})\n"
    return extract

def impress(balance, /, *, extract):
        print("-" * 100)
        print("\t\tData/hora\t\t\tOperações\t\t\t   Valor")
        print("-" * 100)
        print("System: Não foram realizadas movimentações." if not extract else extract)
        print("-" * 100)
        print(f"Saldo = R$ {balance:.2f}")

def main():
    LIMIT_QTD_WITHDRAW = 3
    LIMIT_VALUE_WITHDRAW  = 500
    qtd_withdraw = 0

    balance = 0
    extract = ""

    AGENCY = "0001"
    users = []
    accounts = []

    to_start()
    while True:
        option = menu()
        if option.isdigit():
            option = int(option)

            if option == 1:
                new_user(users, option)

            if option == 2:
                number_account = len(accounts) + 1
                account = new_account(AGENCY, number_account, users, option)    

                if account:
                    accounts.append(account)

            if option == 3:
                list_accounts(accounts, option)

            if option == 4:
                header(option)
                value = input("System: Informe o valor do Depósito:\n⇒ ").strip()
                value = validation(value)
                balance, extract = deposit(balance, value, option, extract)
                repeat(option)

            if option == 5:
                header(option)
                value = input("System: Informe o valor do Saque:\n⇒ ").strip()
                value = validation(value)
                balance, extract, qtd_withdraw = withdraw(
                    balance = balance,
                    value = value,
                    option = option,
                    extract = extract,
                    limit_value_withdraw = LIMIT_VALUE_WITHDRAW,
                    limit_qtd_withdraw = LIMIT_QTD_WITHDRAW,
                    qtd_withdraw = qtd_withdraw,
                    )
                repeat(option)

            if option == 6:
                header(option)
                impress(balance, extract=extract)
                repeat(option)

        else:
            print("Operação Inválida".center(100,"|"),f"\nSystem: Favor informe o Número do Serviço.")
            repeat(0)
            continue

main()