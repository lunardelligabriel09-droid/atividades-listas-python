
turma = [
    ['Alice', 8.0, 7.5, 9.0],
    ['Bruno', 6.5, 7.0, 8.0],
    ['Carla', 9.5, 9.0, 9.5],
    ['Diego', 5.0, 6.0, 5.5],
    ['Elena', 7.0, 8.5, 7.5],
]

medias = []

for aluno in turma:
    nome = aluno[0]
    media = sum(aluno[1:]) / 3
    medias.append([nome, media])
    print(f"{nome} - Média: {media:.2f}")

maior_media = medias[0]

for aluno in medias:
    if aluno[1] > maior_media[1]:
        maior_media = aluno

print("Aluno com maior média:", maior_media[0])

aprovados = []
reprovados = []

for aluno in medias:
    if aluno[1] >= 6.0:
        aprovados.append(aluno[0])
    else:
        reprovados.append(aluno[0])

print("Aprovados:", aprovados)
print("Reprovados:", reprovados)

media_geral = sum(aluno[1] for aluno in medias) / len(medias)
print(f"Média geral da turma: {media_geral:.2f}")

turma.append(['Felipe', 8.0, 7.5, 8.5])

ranking = sorted(
    turma,
    key=lambda aluno: sum(aluno[1:]) / 3,
    reverse=True
)

print("Ranking da turma:")
for aluno in ranking:
    media = sum(aluno[1:]) / 3
    print(f"{aluno[0]} - Média: {media:.2f}")