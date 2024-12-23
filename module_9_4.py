from random import choice

#Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda c1, c2: c1 == c2, first, second)))

#Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for data in data_set:
                file.write(str(data) + '\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#Метод __call__
class MysticBall:
    def __init__(self, *words):
        self.words = list(words)
    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Nope', 'Most assuredly', "Can't really say",
                        'That s for you to decide', "No, you won't",
                        "Turn right at the stop sign",
                        "Yes, her name is Lynn", "There is for you, Neal")
print(first_ball())
print(first_ball())
print(first_ball())