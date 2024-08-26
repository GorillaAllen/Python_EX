import random as rd
pool_list = [i for i in range(1,14)]

def output_char(num):
    if num ==   1:
        return 'A'
    if num ==   11:
        return 'J'
    if num ==   12:
        return 'Q'
    if num ==   13:
        return 'K'
    return str(num)

ans = rd.choice(pool_list)
print(ans)
counter = 0
legit_pool = ['a', 'A', 'j', 'J', 'q','Q', 'k', "K",2,3,4,5,6,7,8,9,10]

while True:
    guess = input("開始猜:")
    if guess not in legit_pool:
        # print(legit_pool)
        print('輸入錯誤,請重來')
        continue
    if guess == 'A' or guess == 'a': guess = 1
    if guess == 'J' or guess == 'j': guess = 11
    if guess == 'Q' or guess == 'q': guess = 12
    if guess == 'K' or guess == 'K': guess = 13
    guess = int(guess)
    # print(guess)
    counter += 1

    if guess == ans:
        print("BINGO!你猜了%d次"%counter)
        break
    elif guess > ans:
        temp_list = pool_list.copy()
        for i in range(0, len(pool_list)):
            if pool_list[i] >= guess:
                temp_list.remove(pool_list[i])
        pool_list = temp_list        
        print("錯. 太大了. 介於%s跟%s之間" %(output_char(min(pool_list)), output_char(max(pool_list))))
    else:
        temp_list = pool_list.copy()
        for i in range(0, len(pool_list)):
            if pool_list[i] <= guess:
                temp_list.remove(pool_list[i])
        pool_list = temp_list    
        print("錯. 太小了. 介於%s跟%s之間" %(output_char(min(pool_list)), output_char(max(pool_list))))

