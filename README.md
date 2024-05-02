# Sistema: Banking Global Finance

<div>
<img src="./img/home.png" alt="Imagem 1" width="48%">
<img src="./img/menu.png" alt="Imagem 1" width="48%">
</div>
<div align="center">
<img src="./img/users.png" alt="Imagem 1" width="48%">
<img src="./img/accounts.png" alt="Imagem 2" width="48%">
</div>
<div align="center">
<img src="./img/list.png" alt="Imagem 3" width="48%">
<img src="./img/deposit.png" alt="Imagem 1" width="48%">
</div>
<div align="center">
<img src="./img/withdrawal.png" alt="Imagem 2" width="48%">
<img src="./img/extract.png" alt="Imagem 3" width="48%">
</div>

## 👨🏻‍💻 Abrir Projeto:

🖥️Acesso<br>
Para ter acesso ao código, você irá precisar:

Python: Ter o Python instalado. Você pode baixar a versão mais recente do Python no site oficial [python.org](https://www.python.org/downloads/).<br>
Editor de Código: Ter um ambiente de desenvolvimento integrado (IDE). Recomendo o [VsCode](https://code.visualstudio.com/download).<br>

Abra o arquivo: "main.py" no seu editor de Código (VsCode) e terá acesso completo ao código.<br>
Para executá-lo clique na opção: `Run Python File` na parte superior direita do VsCode.<br>
Ele irá abrir o terminal no qual poderá interagir com o sistema.

<img src="./img/execute.png" alt="Imagem 1" width=auto>

## 📝 Introdução

Essa é a versão 2.0 que criei do Sistema Bancário criado para a empresa Global Finance, realizar suas operações financeiras.

## 💡 Sobre

Fui contratado pelo Banco Global Finance para desenvolvimento de seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. <br>
Para essa segunda versão, além de otimizar as 3 operações iniciais: Saque, Depósito e Visualizar Extrato, através de funções, também desenvolvi novas funcionalidades, como: Criar Usuário, Criar Conta e Listar Usuário/Conta.<br>
Isso tudo, respeitando todas as regras do negócio:

📇 Criar Usuário:<br>
Essa nova funcionalidade permite criar usuários em uma lista, com os seguintes dados: "Nome, Data de Nascimento, CPF (apenas números) e Endereço".<br>
O endereço segue o formato: "Logradouro, nr - Bairro - Cidade/Sigla Estado".<br>
Uma validação impede o cadastro de dois ou mais usuários com o mesmo CPF.<br>

💳 Criar Conta:<br>
Essa nova funcionalidade permite criar contas, cada uma composta por: "Agência, Número da Conta e Usuário".<br>
A Agência é fixa: "0001", e o Número da Conta é sequencial, começando em 1. Isso permite que um usuário tenha mais de uma conta.<br>
Se não houver contas cadastradas, uma mensagem informa ao usuário o motivo.<br>

🗒️ Listar Usuário/Conta:<br>
Desenvolvi essa função para facilitar a consulta das contas criadas, exibindo detalhes como Agência, Conta e Titular.<br>

📨 Depósito:<br>
Apenas valores positivos são aceitos para depósito. Se o valor for diferente, o sistema informa que a operação é inválida.<br>
Todos os depósitos são registrados e exibidos no Extrato.<br>

💸 Saque:<br>
O sistema permite até 3 saques diários, com um limite máximo total de R$ 500,00 por saque. Se esse limite for ultrapassado, o sistema informa o motivo.<br>
Se o usuário não tiver saldo suficiente, uma mensagem avisa sobre a impossibilidade de realizar o saque.<br>

📜Extrato:<br>
Essa operação lista todos os depósitos e saques, mostrando também o saldo atual da conta.<br>
Se não houver movimentações, é exibida a mensagem padrão: "Não foram realizadas movimentações".<br>
Os valores são exibidos no formato R$ xxx.xx, por exemplo: R$ 1500.45.<br>

## 📚 Conhecimentos

Para estudo e aplicação do projeto, foi utilizado os conteúdos:

- [Python AI Backend Developer](https://web.dio.me/track/coding-future-vivo-python-ai-backend-developer)

## 🤖 Tecnologias

<div style="display: flex">
  <img alt="Python" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" />
</div>

---

- `Python`: O Python é a linguagem de programação utilizada para tornar real nosso Sistema Bancário, definindo as regras, cálculos e funções necessárias para automatizar e executar o projeto, respeitando as regras do negócio.

---

**Desenvolvido por [Rodrigo Moraes](https://github.com/rodrigomoraesdev)**
