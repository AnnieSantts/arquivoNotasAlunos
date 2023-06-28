import csv

def calcular_medias_turmas():
    arquivo = open('alunos.csv', 'r')
    next(arquivo)
    escritor = csv.reader(arquivo, delimiter=',', lineterminator='\n')
    arq = list(escritor)

    turmas = {}
    medias_turmas = []

    for linha in arq:
        turma = linha[5]
        notas = linha[1:4]
        notas = map(int, notas)
        soma_notas = sum(notas)
        media = soma_notas / 3

        if turma in turmas:
            turmas[turma].append(media)
        else:
            turmas[turma] = [media]

    arquivo.close()

    for turma, medias in turmas.items():
        media_turma = sum(medias) / len(medias)
        media_turma = round(media_turma, 1)  # Arredonda para 1 casa decimal
        medias_turmas.append((turma, media_turma))

    return medias_turmas

def media_alunos_aprovados():
    arquivo = open('alunos.csv', 'r')
    next(arquivo)
    escritor = csv.reader(arquivo, delimiter=',', lineterminator='\n')
    arq = list(escritor)
    aprovados = []
    reprovados = []
    medias = []

    for linha in arq:
        aluno = linha[0]
        notas = linha[1:4]
        notas = map(int, notas)
        soma_notas = sum(notas)
        media = soma_notas / 3
        media = round(media, 1)  # Arredonda para 1 casa decimal

        if media >= 7:
            aprovados.append(aluno)
        else:
            reprovados.append(aluno)
        medias.append(media)

    arquivo.close()
    return medias, aprovados, reprovados

medias_alunos, alunos_aprovados, alunos_reprovados = media_alunos_aprovados()
medias_turmas = calcular_medias_turmas()

print("Médias dos alunos:", medias_alunos)
print("Alunos aprovados:", alunos_aprovados)
print("Alunos reprovados:", alunos_reprovados)

maior_media_turma = max(medias_turmas, key=lambda x: x[1])
menor_media_turma = min(medias_turmas, key=lambda x: x[1])

print("Médias das turmas:")
for turma, media in medias_turmas:
    print(f"Turma {turma}: {media:.1f}")  # Exibe com 1 casa decimal

print("Turma com maior média:", maior_media_turma[0], "- Média:", maior_media_turma[1])
print("Turma com menor média:", menor_media_turma[0], "- Média:", menor_media_turma[1])
