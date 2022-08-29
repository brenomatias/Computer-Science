# Muitas vezes a página de onde estamos removendo o conteúdo possui uma limitação de quantas requisições podemos enviar em um curto período de tempo, evitando assim ataques de negação de serviço.


import requests

# exemplos de muitas reqs para uma api

# À partir da décima requisição somos bloqueados de acessar o recurso
# Código de status 429: Too Many Requests
for _ in range(15):
    response = requests.get("https://www.cloudflare.com/rate-limit-test/")
    print(response.status_code)




# Uma boa prática é sempre fazermos uma pausa entre as requisições, ou lote delas, mesmo que o website onde a informação está não faça o bloqueio.

import time


# Coloca uma pausa de 6 segundos a cada requisição
# Obs: este site de exemplo tem um rate limit de 10 requisições por minuto
for _ in range(15):
    response = requests.get("https://www.cloudflare.com/rate-limit-test/")
    print(response)
    time.sleep(6)