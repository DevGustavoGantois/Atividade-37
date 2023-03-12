print('==================================ATIVIDADE=========================================')
print("""Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa
vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos
em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols
feitos durante o campo, inclua um sistema de vizualização de detalhes do aproveitamento de cada 
jogador. """)
print('-='*40)
time = list()
jogador  = dict()
partidas = list()
while True:
    jogador.clear
    jogador['Nome'] = int(input('Nome do Jogador:'))
    tot = jogador['Quantas partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou:'))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c}?')))
        jogador['gols'] = partidas[:]
        jogador['total'] = sum(partidas)
        time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
    print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print('-='*40)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<4}')
    print()
print('-='*40)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*40)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'                      => Na partida {i} em {v} gols.')
    print(f'Foi total de {jogador["total"]} gols. ')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador:'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols.']):
            print(f'          No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('                   <<VOLTE SEMPRE>>      ')
print('#'*40)
print('FIM DO PROGRAMA...')

