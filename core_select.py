from core import engine

conn = engine.connect()
autor = str(input('Escolha o usuário:'))

usr_mais_commits = "SELECT autor, Count(*) as commits FROM gitlab GROUP BY autor HAVING Count(*) > 1 order by 2 desc limit 1"

commits_mes = "Select count(*) From gitlab where Extract('Month' From to_date(data, 'YYYY/MM/DD')) = Extract('Month' From CURRENT_DATE) and Extract('Year' From to_date(data, 'YYYY/MM/DD')) = Extract('Year' From CURRENT_DATE)"

commits_trimestre = "Select count(*) From gitlab where Extract('Month' From to_date(data, 'YYYY/MM/DD')) >= Extract('Month' From CURRENT_DATE)-3 and Extract('Year' From to_date(data, 'YYYY/MM/DD')) = Extract('Year' From CURRENT_DATE)"

ultimo_commit_usr = f"Select * From gitlab where autor = '{autor}' order by data desc limit 1"

commits_usr = f"Select codigo From gitlab where autor = '{autor}' order by data desc"

print(f"Usuário com mais commits: {conn.execute(usr_mais_commits).fetchall()}")
print(f"Commits do mês: {conn.execute(commits_mes).fetchall()}")
print(f"Commits do trimestre: {conn.execute(commits_trimestre).fetchall()}")
print(f"Ultimo commit do usuário: {conn.execute(ultimo_commit_usr).fetchall()}")
print(f"Lista de commits de usuário: {conn.execute(commits_usr).fetchall()}")
