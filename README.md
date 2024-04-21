# Documentação do Sistema Bancário - Versão 1

## Visão Geral
Este documento descreve as operações implementadas no novo sistema bancário desenvolvido para um grande banco, que escolheu modernizar suas operações utilizando a linguagem de programação Python. A versão inicial do sistema inclui três operações básicas: depósito, saque e extrato.

### Funcionalidades
- **Depósito**
- **Saque**
- **Extrato**

## Detalhes das Operações

### 1. Operação de Depósito
- **Descrição**: Permite ao usuário depositar valores positivos em sua conta bancária.
- **Requisitos**:
  - Aceita somente valores positivos.
  - Não requer identificação de agência ou número de conta bancária, pois é uma operação para um único usuário.
  - Os depósitos são armazenados em uma variável e exibidos na operação de extrato.

### 2. Operação de Saque
- **Descrição**: Permite ao usuário realizar até três saques diários, com um limite de R$ 500,00 por saque.
- **Requisitos**:
  - O usuário não pode sacar mais do que o saldo disponível em conta.
  - Se o saldo não for suficiente, o sistema exibirá uma mensagem informando a impossibilidade de realizar o saque.
  - Os saques são registrados e exibidos no extrato.

### 3. Operação de Extrato
- **Descrição**: Exibe todas as transações realizadas (depósitos e saques) e o saldo atual da conta.
- **Formatação**:
  - Todos os valores monetários são exibidos no formato `R$ XXXX,XX`.
  - Exemplo: `1500.45` será exibido como `R$ 1500,45`.

## Conclusão
Este sistema inicial atende às necessidades básicas do banco de modernizar suas operações com uma solução simples e eficaz. As funcionalidades implementadas são fundamentais para a operação bancária diária de um usuário, fornecendo uma base sólida para futuras expansões do sistema.
