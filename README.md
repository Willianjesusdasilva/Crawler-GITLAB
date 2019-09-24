# Gitlab Commit Crawler

Gitlab Commit Crawler é uma ferramenta para extração de commits realizados no Gitlab.

## Instalação

Para instalar as dependências do projeto é necessária a utilização do instalador de pacotes do python (pip) com o seguinte comando:

```bash
pip install -r requirements.txt
```

## Utilização

Para a utilização do projeto existem dois arquivos importantes, sendo eles:

#### main.py
Arquivo que recolhe por meio de requisições e filtra os dados da página, trata os mesmos e faz sua inserção no banco de dados.
#### core_select.py
Recolhe os registros do banco de dados e apresenta na tela(último commit, usuário com mais commits e etc...)

## Tecnologias
#### Python 3.6
-Sqlalchemy
-Requests
-Lxml
-Datetime

#### PostgreSQL
O banco postgres utilizado nesta aplicação é disponibilizado pelo ElephantSQL.

(Para facilitar a utilização do banco, optei por utilizar um serviço web, uma vez que não tive êxito na utilização do docker)