# 📚 EduEnsino

Sistema de gerenciamento escolar desenvolvido em Python para auxiliar no controle de alunos, turmas, notas, faltas e emissão de relatórios acadêmicos.

## 🎯 Objetivo

O EduEnsino foi criado com o objetivo de simular um sistema escolar simples, permitindo o cadastro e gerenciamento de informações acadêmicas de alunos de forma prática e organizada através do terminal.

## ✨ Funcionalidades

### 👨‍🎓 Gerenciamento de Alunos

* Visualizar alunos cadastrados.
* Adicionar novos alunos às turmas.
* Remover alunos existentes.

### 🏫 Gerenciamento de Turmas

* Criar novas turmas.
* Excluir turmas existentes.

### 📝 Controle de Notas e Faltas

* Registrar notas por disciplina.
* Registrar faltas dos alunos.
* Atualizar informações acadêmicas.

### 📖 Gerenciamento de Disciplinas

* Visualizar disciplinas cadastradas.
* Alterar nomes das disciplinas.

### 📊 Relatórios

* Cálculo automático das médias.
* Verificação de frequência.
* Determinação de aprovação ou reprovação.
* Geração de relatório final do aluno.

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* Estruturas de dados (`listas` e `dicionários`)
* Funções
* Modularização básica
* Interface via terminal (CLI)

---

## 📂 Estrutura dos Dados

Cada aluno é armazenado no seguinte formato:

```python
{
    "nome": "Ana",
    "notas": {
        "1": [10, 10, 10, 10],
        "2": [],
        "3": [],
        "4": []
    },
    "faltas": {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0
    }
}
```

---

## 🚀 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/EduEnsino.git
```

2. Acesse a pasta do projeto:

```bash
cd EduEnsino
```

3. Execute o arquivo principal:

```bash
python EduEnsino.py
```

---

## 📚 Conceitos Aplicados

Durante o desenvolvimento deste projeto foram utilizados conceitos importantes de programação:

* Variáveis
* Estruturas condicionais (`if`, `elif`, `else`)
* Estruturas de repetição (`for`, `while`)
* Funções
* Listas
* Dicionários
* Manipulação de dados
* Organização de código
* Cálculos estatísticos básicos

---

## 🔮 Melhorias Futuras

* Persistência de dados em arquivos JSON.
* Banco de dados SQLite.
* Interface gráfica.
* Login de usuários.
* Exportação de relatórios em PDF.
* Sistema de múltiplos professores.
* Histórico acadêmico completo.

---

## 👨‍💻 Autor

Desenvolvido por **Samuel Pereira** como projeto de aprendizado em Python.

---

## 📄 Licença

Este projeto é de uso educacional e livre para estudos, modificações e melhorias.
