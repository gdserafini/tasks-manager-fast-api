# Task Manager API

API - Gerenciador de Tarefas desenvolvido em Python com FastAPI utilizando banco de dados PostgreSQL. <br>
Projeto baseado no curso de FastAPI: https://fastapidozero.dunossauro.com/

## Como configurar e rodar o projeto
### Requisitos
* Docker

### Ambiente com .env
Caso não exista, é necessário criar o arquivo .env na raiz do projeto com as seguintes variáveis:
>DATABASE_URL<br>
>SECRET_KEY<br>
>ALGORITHM<br>
>ACCESS_TOKEN_EXPIRE_MINUTES<br>
>PASSWORD_TEST<br>
>POSTGRES_USER<br>
>POSTGRES_DB<br>
>POSTGRES_PASSWORD<br>

Com o Docker devidamente instalado execute:
> docker compose up --build

Assim é possível acessar a API e sua documentação em _http://localhost:8000/docs_

## Rodando testes com TestContainers
### Requisitos
* Python >= 3.12

Conforme script de configuração da aplicação em tests.sh, execute o comando na pasta root da aplicação:
> source tests.sh

Então execute o comando:
> task test