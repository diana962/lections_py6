# Одним из первых в истории примеров шифрования считаются закодиро-
# ванные послания Юлия Цезаря. Римскому полководцу необходимо было
# посылать письменные приказы своим генералам, но он не желал, чтобы
# в случае чего их прочитали недруги. В результате он стал шифровать свои
# послания довольно простым методом, который впоследствии стали на-
# зывать кодом Цезаря.
# Идея шифрования была совершенно тривиальной и заключалась в цик­
# лическом сдвиге букв на три позиции. В итоге буква A превращалась в D,
# B – в E, C – в F и т. д. Последние три буквы алфавита переносились на на-
# чало. Таким образом, буква X становилась A, Y – B, а Z – C. Цифры и другие
# символы не подвергались шифрованию.
# Напишите программу, реализующую код Цезаря. Позвольте пользова-
# телю ввести фразу и количество символов для сдвига, после чего выведите
# результирующее сообщение. Убедитесь в том, что ваша программа шиф-
# рует как строчные, так и прописные буквы. Также должна быть возмож-
# ность указывать отрицательный сдвиг, чтобы можно было использовать
# вашу программу для расшифровки фраз.

# alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# symbols = '!@#$%^&*()_-+=<>?/, .'

# user = 'a, z'.upper()
# ls = []
# for i in user:
#     if i in symbols:
#         ls.append(i)
#     for x in alphabet:
#         if i == x and i != 'X' and i != 'Y' and i != 'Z':
#             index = alphabet.index(i) + 3
#             ls.append(alphabet[index])
#     else:
#         if i == 'X':
#             ls.append('A')
#         if i == 'Y':
#             ls.append('B')
#         if i == 'Z':
#             ls.append('C')
# print(''.join(ls))

# def caesar_cipher(message, shift):
#     result = ""
#     for char in message:
#         if char.isalpha(): 
#             start = ord('A') if char.isupper() else ord('a')
#             result += chr((ord(char) - start + shift) % 26 + start)
#         else:
#             result += char
#     return result


# phrase = input("Введите фразу для расшифровки: ")
# shift = int(input("Введите количество символов для сдвига: "))

# encrypted_message = caesar_cipher(phrase, shift)
# print(encrypted_message)

# def caesar_cipher(message, shift):
#     result = ""
#     for char in message:
#         if char.isalpha(): 
#             start = ord('A') if char.isupper() else ord('a')
#             result += chr((ord(char) - start + shift) % 26 + start)
#         else:
#             result += char
#     return result


# phrase = input("Введите фразу для расшифровки: ")
# shift = int(input("Введите количество символов для сдвига: "))

# encrypted_message = caesar_cipher(phrase, shift)
# print(encrypted_message)



