question = {
    'Pergunta 1': {
            'pergunta': 'Qual item arremessável é necessario para cegar um monstro ? ',
        'respostas': {
            'a': 'Lampejo.',
            'b': 'Lampejo inseto.',
            'c': 'Mosclarão.',
        },
        'resposta_certa': 'a',
    },
    'Pergunta 2': {
        'pergunta': 'Quais itens usamos para a criação de  poção maxima ? ',
        'respostas': {
            'a': 'Mandrágora e Armaguinseto.',
            'b': 'Mandrágora e Poção de vida.',
            'c': 'Mandrágora e Mega Nutrientes.',
        },
        'resposta_certa': 'c',
    },
}
print('=*'* 50 + '=*')

correct_answer = 0

for question, dados_question in question.items():
    print(f'{question}: {dados_question["pergunta"]}')

    print('Respostas: ')
    for respostas, dados_respostas in dados_question['respostas'].items():
        print(f'{respostas}: {dados_respostas}')

    print('=*' * 50 + '=*')

    resposta_usuario = input('Informe sua Resposta: ')

    if resposta_usuario == dados_question['resposta_certa']:
        print('Parabens Caçador, Resposta Válida')

        correct_answer += 1

    else:
        print('Infelizmente você é caçador de ranque baixo, treine mais e volte aqui')
    print('=*' * 50 + '=*')

    quantidade_perguntas = len(question)
    porcentagem_acertos = correct_answer / quantidade_perguntas * 100
    print(f'Você acertou {correct_answer} respostas.')
    print(f'Sua porcetagem de acerto foi {porcentagem_acertos}%.')

    print('=*'* 50 + '=*')
