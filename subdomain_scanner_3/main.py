import requests

# домен для поиска поддоменов
domain = "susu.ru"

# читать все поддомены
file = open("subdomains.txt")
# прочитать весь контент
content = file.read()
# разделить на новые строки
subdomains = content.splitlines()

# список обнаруженных поддоменов
discovered_subdomains = []
for subdomain in subdomains:
    # создать URL
    url = f"http://{subdomain}.{domain}"
    try:
        # если возникает ОШИБКА, значит, субдомен не существует
        requests.get(url)
    except requests.ConnectionError:
        # если поддомена не существует, ничего не выводить
        pass
    else:
        print(f"[+] Обнаружен поддомен: {url}")
        # добавляем обнаруженный поддомен в наш список
        discovered_subdomains.append(url)

# сохраняем обнаруженные поддомены в файл
with open("discovered_subdomains.txt", "w") as f:
    for subdomain in discovered_subdomains:
        print(subdomain, file=f)
