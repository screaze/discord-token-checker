from requests import get, post
from random import randint
alaala = 0
alaala2 = 0
alaala3 = 0
logo = """
[SYSTEM] Discord Token Checker by Screaze
"""
def checker1(token):
    response = get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})
    return True if response.status_code == 200 else False

def checker2(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if "You need to verify your account in order to perform this action." in str(response.content) or "401: Unauthorized" in str(response.content):
        alaala3 = alaala3+1
        return False
    else:
        return True

def locktokens(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if response.status_code == 401:
        return 'Invalid'
    elif "You need to verify your account in order to perform this action." in str(response.content):
        return 'Phone Lock'
    else:
        return 'Valid'

if __name__ == "__main__":
    try:
        checked = []
        with open('tokens.txt', 'r') as tokens:
            for token in tokens.read().split('\n'):
                if len(token) > 15 and token not in checked and checker2(token) == True:
                    print(f'[LOG] Токен: {token} валидный!')
                    alaala = alaala+1
                    checked.append(token)
                else:
                    print(f'[LOG] Токен: {token} не валидный!')
                    alaala2 = alaala2+1
        if len(checked) > 0:
            save = input(f'[LOG] {len(checked)} Валидных токенов! \n[SYSTEM] Сохранить в текстовый файл? (y/n)').lower()
            if save == 'y':
                name = randint(100000000, 9999999999)
                with open(f'{name}.txt', 'w') as saveFile:
                    saveFile.write('\n'.join(checked))
                print("[LOG] Токены были сохранены в "+name+".txt в директории с софтом!")
        input('[SYSTEM] Нажмите ENTER')
        os.system("clear")
        print("[LOG] Статистика:")
        print("[LOG] Валид:", +alaala)
        print("[LOG] Не валидные:", +alaala2)
        print("[LOG] Заблокированые/Без номера телефона:", +alaala3)
    except:
        input('[LOG] Файл tokens.txt не найден! Нажмите ENTER для закрытия программы!')
        exit()
# End of code
