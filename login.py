import requests
from lxml import html

headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
          'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
          }


def login_gitlab():
    session = requests.Session()

    page = session.get('https://gitlab.com/users/sign_in')

    get_token = html.fromstring(page.content)

    token = get_token.xpath('/html/head/meta[@name="csrf-token"]/@content')

    data = {
           'utf8': '\u2713',
           'authenticity_token': token[0],
           'user[login]': 'mamigi@fast-coin.com',
           'user[password]': '4_})fk{g,5"fHrv,'
           }

    response_login = session.post('https://gitlab.com/users/sign_in', headers=headers, data=data)

    return session, response_login
