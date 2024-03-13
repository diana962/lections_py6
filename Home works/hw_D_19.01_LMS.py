# Задание 1

# Вы решили сделать проверку при входе, и пускать на сайт только «своих» ребят. Для этого Вам необходимо составить список никнеймов, которые будут иметь доступ.

# Необходимо, что при запуске кода, программа запрашивала никнейм, и либо пускать на сайт (выведется сообщение «Ты – свой. Приветствую, любезный {НИК_ПОСЕТИТЕЛЯ}!»), либо нет (в этом случае будет такой текст: «Тут ничего нет. Еще есть вопросы?»).

# Используйте цикл While, для того чтобы программа вновь и вновь запрашивала никнейм пользователя, до тех по пока не ввести «правильный» никнейм.

# dict = {
#     'sara': '123',
#     'kim': '345',
#     'kasim': '678'
# } 

# while True:
#     user = input('Enter a nickname: ')
#     if user not in dict:
#         print('Тут ничего нет. Еще есть вопросы?')
#         break
#     for user in dict:
#         passport = input('Enter a password: ')  # --> строка; числа должны быть в '' dict
#         if passport == dict[user]:
#             print(f'Ты – свой. Приветствую, любезный {user}!')
#             break
#         else:
#             print("Неверно введен парлоль")


# Задание 2

 

# Создать программу имитирующий чат:

# Чат должен работать со следующими фразами:

# "Кто ты?" -  "Я программа"

# "Что делаешь?" - "Работаю"

# "Как дела” - "Хорошо"

# "Как это работает?” - "Как-то так"

# "Где ты?” - "У тебя на компе"

# Написать чат-бота, который будет ждать от пользователя ввод вопроса из вышеописанных фраз и давать на него соответствующий ответ.  Ввод данных будет осуществляться вечно, до тех пор, пока пользователь не введет букву "q". Сообщить, если введен вопрос, которого нет в списке.

# dict = {
#     'Кто ты?' : 'Я программа',
#     'Что делаешь?' : 'Работаю',
#     'Как дела' : 'Хорошо',
#     'Как это работает?' : 'Как-то так',
#     'Где ты?' : 'У тебя на компе'
# }
# while True:
#     user = input('Ask me or if you want to stop "q": ')
#     if user == 'q':
#         break
#     elif user in dict.keys(): # elif user in dict:
#         print(dict[user])
#     else:
#         print('No Answer.')

# Задание3

# Напишите программу, которая будет суммировать все числа, введенные пользователем, игнорируя при этом нечисловой ввод. Выводите на экран текущую сумму чисел после каждого очередного ввода. Ввод пользователем значения, не являющегося числовым, должен приводить к появлению соответствующего предупреждения, после чего пользователю должно быть предложено ввести следующее число. Выход из программы будет осуществляться путем пропуска ввода. 
# Удостоверьтесь, что ваша программа корректно обрабатывает целочисленные значения и числа с плавающей запятой.

# count = 0
# while True:
#     user = input('Enter a num or if you want to stop "q": ')
#     if user == 'q':
#         break
#     for i in user:
#         if i.isalpha():
#             print('Not number. ')
#             break
#         else:
#             num = float(user)
#             count += num
#             print(count)
#             break