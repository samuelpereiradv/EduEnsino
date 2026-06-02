escolha = ''

lista_turmas = [[], []]
materias = ["Lingua Portuguesa", "Matemática", "Geografia", "História"]
quantidade_aulas = 100

lista_turmas[0].append({
    "nome": "Ana",
    "notas": {"1": [10,10,10,10], "2": [], "3": [], "4": []},
    "faltas": {"1": 0, "2": 0, "3": 0, "4": 0}
})


def fim_fun():
    input("Tecle ENTER para continuar!")

def gerar_relatorio():
    print("""
█▀▀ █▀▀ █▀█ ▄▀█ █▀█   █▀█ █▀▀ █░░ ▄▀█ ▀█▀ █▀█ █▀█ █ █▀█
█▄█ ██▄ █▀▄ █▀█ █▀▄   █▀▄ ██▄ █▄▄ █▀█ ░█░ █▄█ █▀▄ █ █▄█""")
    
    print("\nTurmas e alunos:")
    for index, turma in enumerate(lista_turmas, start=1):
        print(f"Turma {index}:")
        if turma:
            for i, aluno in enumerate(turma, start=1):
                print(f"  {i} - {aluno['nome']}")
        else:
            print("  (sem alunos)")

    escolha_turma_aluno = int(input("Digite a turma do aluno: "))
    turma = lista_turmas[escolha_turma_aluno - 1]

    escolha_nome_aluno = int(input("Digite o número do aluno: "))
    aluno = turma[escolha_nome_aluno - 1]

    frequencia = calculo_frequencia(aluno["faltas"])
    media = calculo_notas(aluno["notas"])
    resultado = resultado_final(media,frequencia)

    print(f"""

█▀█ █▀▀ █░░ ▄▀█ ▀█▀ █▀█ █▀█ █ █▀█   █▀▀ █ █▄░█ ▄▀█ █░░
█▀▄ ██▄ █▄▄ █▀█ ░█░ █▄█ █▀▄ █ █▄█   █▀░ █ █░▀█ █▀█ █▄▄          


Nome do aluno: {aluno["nome"]}
Boletim:
{materias[1-1]}: {media[1-1]} | Situação: {'Aprovado' if media[1-1] > 5 else 'Reprovado'}
{materias[2-1]}: {media[2-1]} | Situação: {'Aprovado' if media[2-1] > 5 else 'Reprovado'}
{materias[3-1]}: {media[3-1]} | Situação: {'Aprovado' if media[3-1] > 5 else 'Reprovado'}
{materias[4-1]}: {media[4-1]} | Situação: {'Aprovado' if media[4-1] > 5 else 'Reprovado'}

Frequência: 
{materias[1-1]}: {'Aprovado' if frequencia[1-1]  else 'Reprovado'}
{materias[2-1]}: {'Aprovado' if frequencia[2-1]  else 'Reprovado'}
{materias[3-1]}: {'Aprovado' if frequencia[3-1]  else 'Reprovado'}
{materias[4-1]}: {'Aprovado' if frequencia[4-1]  else 'Reprovado'}

Resultado Final:
{materias[1-1]}: {'Aprovado' if resultado[1-1] else 'Reprovado'}
{materias[2-1]}: {'Aprovado' if resultado[2-1] else 'Reprovado'}
{materias[3-1]}: {'Aprovado' if resultado[3-1] else 'Reprovado'}
{materias[4-1]}: {'Aprovado' if resultado[4-1] else 'Reprovado'}
""")


def resultado_final(media, frequencia):
    resultado = []
    for i in range(len(materias)):
        if media[i] >= 5 and frequencia[i]:
            resultado.append(True)
        else:
            resultado.append(False)
    print(resultado)
    return resultado



def calculo_frequencia(faltas):
    frequencia_minima = quantidade_aulas/4
    frequencia = []
    for faltas in faltas.values():
        if faltas < frequencia_minima:
            frequencia.append(True)
        else:
            frequencia.append(False)

    return frequencia


def calculo_notas(notas):
    materia1 = notas['1']
    materia2 = notas['2']
    materia3 = notas['3']
    materia4 = notas['4']

    boletim = [sum(materia1,)/4 , sum(materia2,)/4, sum(materia3,)/4, sum(materia4,)/4]

    return boletim

def aluno():
    # ---------------- ALUNO ----------------
    print("""
█▀▀ █▀█ █▄░█ ▀█▀ █▀█ █▀█ █░░ █▀▀   ▄▀█ █░░ █░█ █▄░█ █▀█ █▀
█▄▄ █▄█ █░▀█ ░█░ █▀▄ █▄█ █▄▄ ██▄   █▀█ █▄▄ █▄█ █░▀█ █▄█ ▄█""")
    print("""
1 - Vizualizar listas de alunos.
2 - Adicionar aluno.
3 - Excluir aluno
    """)

    escolha_menu_aluno = int(input("Digite o número da sua escolha: "))

    if escolha_menu_aluno == 1:
        for index, turma in enumerate(lista_turmas, start=1):
            nomes = [aluno["nome"] for aluno in turma]
            print(f"Turma {index}: {', '.join(nomes)}")

    elif escolha_menu_aluno == 2:
        for index, turma in enumerate(lista_turmas, start=1):
            nomes = [aluno["nome"] for aluno in turma]
            print(f"Turma {index}: {', '.join(nomes)}")

        escolha_turma = int(input("Digite a turma: "))

        if 1 <= escolha_turma <= len(lista_turmas):
            nome_aluno = input("Digite o nome do aluno: ")

            lista_turmas[escolha_turma - 1].append({
                "nome": nome_aluno,
                "notas": {"1": [], "2": [], "3": [], "4": []},
                "faltas": {"1": 0, "2": 0, "3": 0, "4": 0}
            })

            print(nome_aluno, "foi adicionado na turma", escolha_turma)

    elif escolha_menu_aluno == 3:
        for index, turma in enumerate(lista_turmas, start=1):
            print(f"Turma {index}:")
            for idx, aluno in enumerate(turma, start=1):
                print(idx, ":", aluno["nome"])

        escolha_turma_aluno_deletar = int(input("Turma: "))
        escolha_nome_aluno_deletar = int(input("Aluno: "))

        lista_turmas[escolha_turma_aluno_deletar - 1].pop(escolha_nome_aluno_deletar - 1)
        print("Aluno removido com sucesso!")
    else:
        input("Opção inválida!")

def menu_turmas():
    print("""
█▀▀ █▀█ █▄░█ ▀█▀ █▀█ █▀█ █░░ █▀▀   █▀▄ █▀▀   ▀█▀ █░█ █▀█ █▀▄▀█ ▄▀█ █▀
█▄▄ █▄█ █░▀█ ░█░ █▀▄ █▄█ █▄▄ ██▄   █▄▀ ██▄   ░█░ █▄█ █▀▄ █░▀░█ █▀█ ▄█""")
    print("""
1 - Adicionar Turma
2 - Excluir Turma
        """)

    escolha_turma = int(input("Escolha: "))

    if escolha_turma == 1:
        lista_turmas.append([])
        print("Turma adicionada")

    elif escolha_turma == 2:
        for index in range(len(lista_turmas)):
            print("Turma", index + 1)

        escolha_turma_remover = int(input("Digite a turma: "))
        lista_turmas.pop(escolha_turma_remover - 1)

def notas_faltas():
    # ---------------- NOTAS ----------------
    print("""
█▄░█ █▀█ ▀█▀ ▄▀█ █▀   █▀▀   █▀▀ ▄▀█ █░░ ▀█▀ ▄▀█ █▀
█░▀█ █▄█ ░█░ █▀█ ▄█   ██▄   █▀░ █▀█ █▄▄ ░█░ █▀█ ▄█""")
    for i, materia in enumerate(materias, start=1):
        print(f"{i} - {materia}")

    escolha_materia = str(int(input("Digite a matéria para colocar a nota: ")))

    print("\nTurmas e alunos:")
    for index, turma in enumerate(lista_turmas, start=1):
        print(f"Turma {index}:")
        if turma:
            for i, aluno in enumerate(turma, start=1):
                print(f"  {i} - {aluno['nome']}")
        else:
            print("  (sem alunos)")

    escolha_turma_aluno = int(input("Digite o número da turma: "))
    turma = lista_turmas[escolha_turma_aluno - 1]

    escolha_nome_aluno = int(input("Digite o número do aluno: "))
    aluno = turma[escolha_nome_aluno - 1]

    b1 = int(input("Bimestre 1: "))
    b2 = int(input("Bimestre 2: "))
    b3 = int(input("Bimestre 3: "))
    b4 = int(input("Bimestre 4: "))

    aluno["notas"][escolha_materia] = [b1, b2, b3, b4]

    faltas = int(input(f"Faltas de {aluno['nome']}: "))
    aluno["faltas"][escolha_materia] = faltas
    print(f"\nNotas e faltas adicionadas com sucesso ao aluno(a): {aluno['nome']}")

def disciplinas():
    print("""
█▀▀ █▀█ █▄░█ ▀█▀ █▀█ █▀█ █░░ █▀▀   █▀▄ █▀▀   █▀▄ █ █▀ █▀▀ █ █▀█ █░░ █ █▄░█ ▄▀█ █▀
█▄▄ █▄█ █░▀█ ░█░ █▀▄ █▄█ █▄▄ ██▄   █▄▀ ██▄   █▄▀ █ ▄█ █▄▄ █ █▀▀ █▄▄ █ █░▀█ █▀█ ▄█""")
    print("""
1 - Vizualizar matérias
2 - Modificar matéria
    """)

    menu_materias = int(input("Digite: "))

    if menu_materias == 1:
        for materia in materias:
            print(materia)

    elif menu_materias == 2:
        for i, materia in enumerate(materias, start=1):
            print(i, "-", materia)

        escolha_disciplina = int(input("Número: "))
        nome_disciplina = input("Novo nome: ")

        materias[escolha_disciplina - 1] = nome_disciplina



# Menu de funções
while escolha != 6:
    print("""
███████╗██████╗░██╗░░░██╗  ███████╗███╗░░██╗░██████╗██╗███╗░░██╗░█████╗░
██╔════╝██╔══██╗██║░░░██║  ██╔════╝████╗░██║██╔════╝██║████╗░██║██╔══██╗
█████╗░░██║░░██║██║░░░██║  █████╗░░██╔██╗██║╚█████╗░██║██╔██╗██║██║░░██║
██╔══╝░░██║░░██║██║░░░██║  ██╔══╝░░██║╚████║░╚═══██╗██║██║╚████║██║░░██║
███████╗██████╔╝╚██████╔╝  ███████╗██║░╚███║██████╔╝██║██║░╚███║╚█████╔╝
╚══════╝╚═════╝░░╚═════╝░  ╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚════╝░""")
    escolha = int(input("""Opções:
1 - Aluno
2 - Turma
3 - Notas e Faltas
4 - Disciplinas
5 - Relatório Final
6 - Sair do sistema
Digite: """))
    # ---------------- ALUNOS ----------------
    if escolha == 1:
        aluno()
        fim_fun()
    # ---------------- TURMA ----------------
    elif escolha == 2:
        menu_turmas()
        fim_fun()
    # ---------------- NOTAS E FALTAS ----------------
    elif escolha == 3:
        notas_faltas()
        fim_fun()
    # ---------------- MATÉRIAS ----------------
    elif escolha == 4:
        disciplinas()
        fim_fun()
    # ---------------- RELATÓRIO ----------------
    elif escolha == 5:
        gerar_relatorio()
        fim_fun()
    # ---------------- SAIR ----------------
    elif escolha == 6:
        escolha = 6
        print("Obrigado por usar o sistema!")
        break
    else:
        input("Opção inválida! TECLE ENTER!")
