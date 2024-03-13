import random
all_numbers = [f'{letter}{number}' for letter in 'BINGO' for number in range(1, 76)]
random.shuffle(all_numbers)
print(all_numbers)

new_lsit = [x for x in range(1,76)] #--> начинает создавать карту
card_generate = []
for x in 'BINGO':
    random.shuffle(new_lsit)
    card_generate.append([f'{x}{i}' for i in new_lsit[0:5]])
for row in card_generate:
    print(row) #--> cоздал карту

atempant = []
check = True
for _ in range(1000):
    counter = 0
    while check:
        counter += 1

        delete_num = random.choice(all_numbers)
        all_numbers.remove(delete_num)

        for row in card_generate:
            if delete_num in row:  
                row[row.index(delete_num)] = 'X' #--> он стваит Х на индексе/месте в row.
    
        for row in card_generate:
            if len(set(row)) == 1:
                atempant.append(counter)
                
                check = False

        for col in range(0, 5):
            if len(set(row[col] for row in card_generate)) == 1:
                
                atempant.append(counter)
                check = False

                                    
        if len(set(card_generate[i][i] for i in range(5))) == 1 or len(set(card_generate[i][4-i] for i in range(5))) == 1:
           
            atempant.append(counter)
            check = False

    print('-----------------------------------------------------------')
    for row in card_generate:
        print(row)

print(atempant)

for row in card_generate:
    print(row)