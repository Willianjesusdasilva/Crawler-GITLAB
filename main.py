# -*- coding: utf-8 -*-
from datetime import datetime
from login import login_gitlab, html
from core import engine, metadata
from core_reset import truncate_db

metadata.create_all()
truncate_db()

Session, response_rep = login_gitlab()

limit = 70
offset = 0


while True:
    link = f'https://gitlab.com/autowarefoundation/autoware.ai/autoware/commits/master?limit={limit}&offset={offset}'
    print(link)
    response_rep = Session.get(link)

    idProcesso = html.fromstring(response_rep.text)

    list_msg = idProcesso.xpath("//*[contains(@class, 'commit-row-message item-title')]|//*[contains(@title, 'put litter in its place symbol')]")
    list_user = idProcesso.xpath("//*[contains(@class, 'commit-author-link')]")
    list_cmt = idProcesso.xpath("//*[contains(@class, 'label label-monospace monospace')]")
    list_dat = idProcesso.xpath("//*[contains(@class, 'js-timeago')]")

    if len(list_msg) != 0:
        i = 0
        for i in range(len(list_user)):
            form_user = str(list_user[i].text.replace("'", ""))
            form_desc = str(list_msg[i].text.replace("'", ""))
            form_dat = str(datetime.strptime(list_dat[i].text, '%b %d, %Y'))
            form_cmt = str(list_cmt[i].text.replace('\n', ''))

            conn = engine.connect()

            conn.execute(f"insert into gitlab (autor,descricao,codigo,data) values ('{str(form_user)}', '{str(form_desc)}', '{str(form_cmt)}', '{str(form_dat)}');")
        offset += limit
    else:
        break
