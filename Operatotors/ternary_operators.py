# # sentence = input('Enter a sentence: ')
# # ternary operator enthaelt ein String, der if-else Konstruktion hat.
# # Ternary operators(тернарный оператор) - это конструкция которая по своему действию аналогична конструкции if else, но при этом записывается в одну строку

# # res = 'Yes, it\'s a question.' if sentence[-1] == '?' else 'Normal one.'
# # print(res)

# # num = int(input('Enter a number:'))
# # print('even num' if num % 2 == 0 else 'odd number')

# ls = [55, 65, 75, 89, 100, 15, 6]
# user = input('max or min: ').lower().strip()
# print(max(ls) if user == 'max' else min(ls) if user == 'min' else 'Invalid.')

# #-----------------------------------------------------------------------------------------------------------------------------------
# flag = True
# symbols = '0123456789' + '.' + '-'

# while flag: 
#     num1 = input ('Enter a number: ') #123wq
#     is_corrent = True
#     for x in num1:
#         if x not in symbols:
#             print('You entered a letter.')
#             is_corrent = False
#             break
#     if not is_corrent:
#         continue
    
#     num2 = input ('Enter a number: ') #123wq
#     is_corrent = True
#     for x in num2:
#         if x not in symbols:
#             print('You entered a letter.')
#             id_corrent = False
#             break
#     if not is_corrent:
#         continue

#     num1 = float(num1) if '.' in num1 else int(num1)
#     num2 = float(num2) if '.' in num2 else int(num2)

#     # print(num1, type(num1))
#     # print(num2, type(num2))
#     operator = input('Enter operstion(+, -, *, /: )').strip()

#     if operator == "+":
#         print(f'{num1 + num2}')
#     if operator == "-":
#         print(f'{num1 - num2}')
#     if operator == "*":
#         print(f'{num1 * num2}')
#     if operator == "/":
#         print(f'{num1 / num2}' if num2 != 0 else 'На ноль делить нельзя!') 

#     choice = input('Continue? Yes/No: ')
#     if choice.lower().strip() !='yes':
#         flag = False
#         print('Bye bye')





