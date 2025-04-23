import prompt


def greetings():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def main():
    greetings()


if __name__ == '__main__':
    main()