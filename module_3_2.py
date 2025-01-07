# Задача 'Рассылка писем'

def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if '@' not in recipient and sender or not recipient.endswith(('.com', '.ru', '.net')) or not sender.endswith(('.com', '.ru', '.net')):
        print(f'Невозможно отправить письмо с адреса {recipient} на адрес {sender}')
    elif recipient==sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {recipient} на адрес {sender}')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.teacher@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')