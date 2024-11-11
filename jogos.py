import random      
import art 

def main():
    
    
    while True:
        print(art.text2art('GAMES!'))
        game = getGame()
        if game == 1 :
            BlackJack()
        elif game == 2 :
            MagicBall()
        elif game == 3 :
            Pedrapapel()
        else:
            continue
        
        request = input('Você quer continuar jogando? S/N? ').upper()
        if request in ['NAO','N']:
            break

def getGame():
    try:
        opcao = input('Qual jogo você quer jogar? \n 1- Jogo da velha?\n 2- Bola magica\n 3- Pedra papel e tesoura')
        if opcao not in [1,2,3]:
                    raise Exception()
    except (ValueError,Exception):
        print('please Enter a Value 1 or 2')
        
    else : 
        return opcao
    
def Pedrapapel():
    print('Bem vindo ao pedra papel e tesoura')
    player = input('Informe sua jogada escolhendo "pedra, papel e tesoura"').strip().lower()
    bot= random.choice(['pedra','papel','tesoura'])
    
    print(f'Sua jogada foi {player}')
    print(f'a jogada do bot foi {bot}')
    
    if bot == player:
        print('Foi empate!')
    elif player == 'pedra' and bot =='tesoura':
        print('Você ganhou')
    elif player == 'tesoura' and bot =='papel':
        print('Você ganhou')
    elif player == 'papel' and bot =='pedra':
        print('Você ganhou')
    else:
        print('Você perdeu')

def MagicBall():
    resposta = random.randint(1, 9)
    respostas = {
        1: 'It is certain',
        2: 'It is decidedly so',
        3: 'Without a doubt',
        4: 'Yes, definitely',
        5: 'Don’t count on it',
        6: 'My reply is no',
        7: 'Very doubtful',
        8: 'Ask again later',
        9: 'Better not tell you now'
    }
    print(respostas[resposta])
        
def BlackJack():
    