import requests

if name== 'main':
    url = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
        content = response.text
        file = open('resultado.txt', 'w')
        file.write(content)
        file.close()