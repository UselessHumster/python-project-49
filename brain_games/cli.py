import prompt

def greetings(game_rule: str = ''):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game_rule)
    return name