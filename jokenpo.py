import random

def escolha_usuario():
    opcoes = {'1': 'pedra', '2': 'papel', '3': 'tesoura'}
    while True:
        print('\nEscolha:')
        print('1) Pedra\n2) Papel\n3) Tesoura\n0) Sair')
        esc = input('Digite o número da sua escolha: ').strip()
        if esc == '0':
            return None
        if esc in opcoes:
            return opcoes[esc]
        print('Entrada inválida. Tente novamente.')

def escolha_computador():
    return random.choice(['pedra', 'papel', 'tesoura'])

def verifica_vencedor(u, c):
    if u == c:
        return 'empate'
    wins = {('pedra','tesoura'), ('tesoura','papel'), ('papel','pedra')}
    return 'usuario' if (u, c) in wins else 'computador'

def main():
    print('*** Jokenpô - Pedra, Papel e Tesoura ***')
    placar_u = placar_c = 0
    while True:
        u = escolha_usuario()
        if u is None:
            print('Saindo...')
            break
        c = escolha_computador()
        print(f'Você: {u}  x  Computador: {c}')
        resultado = verifica_vencedor(u, c)
        if resultado == 'empate':
            print('Empate!')
        elif resultado == 'usuario':
            print('Você ganhou esta rodada!')
            placar_u += 1
        else:
            print('Computador ganhou esta rodada!')
            placar_c += 1
        print(f'Placar -> Você: {placar_u}  Computador: {placar_c}')

if __name__ == '__main__':
    main()
