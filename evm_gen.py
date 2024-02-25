from eth_account import Account
import secrets
import threading

# Функція для генерації гаманців
def generate_wallets(number_of_wallets=1, desired_prefix='', desired_suffix=''):
    wallets_generated = 0
    while wallets_generated < number_of_wallets:
        acct = Account.create(secrets.token_hex(32))
        address = acct.address

        # Перевіряємо, чи адреса відповідає заданим умовам з урахуванням регістру
        if address[2:2+len(desired_prefix)] == desired_prefix and \
           address.endswith(desired_suffix):
            with open('wallets.txt', 'a') as f:
                f.write(f"Address: {address}, Private Key: {acct.key.hex()}\n")
            print(f"Address: {address}, Private Key: {acct.key.hex()}")
            wallets_generated += 1
            if number_of_wallets == 1:
                break


# Функція для запуску вибраного режиму роботи
def run_mode(mode):
    if mode == 1:
        number = int(input("Введіть кількість гаманців для генерації: "))
        generate_wallets(number_of_wallets=number)
    elif mode == 2:
        prefix = input("Введіть бажаний префікс: ")
        generate_wallets(desired_prefix=prefix)
    elif mode == 3:
        prefix = input("Введіть бажаний префікс: ")
        suffix = input("Введіть бажаний суфікс: ")
        generate_wallets(desired_prefix=prefix, desired_suffix=suffix)
    else:
        print("Невідомий режим роботи.")

if __name__ == '__main__':
    print("Виберіть режим роботи:")
    print("1 - Генерація вказаної кількості гаманців")
    print("2 - Генерація гаманця з вказаним префіксом")
    print("3 - Генерація гаманця з вказаним префіксом та суфіксом")
    mode = int(input())
    run_mode(mode)
