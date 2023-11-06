from mysql.connector import (connection)
db_conexao = connection.MySQLConnection(host="localhost", user="root", password="", database="entrevistas")

def inserir_valores(nome, telefone, email, bio, entrevista, pratico, teorico, softSkills):
    cursor = db_conexao.cursor()
    cursor.execute(f"INSERT INTO entrevistados VALUES (0,'{nome}', '{telefone}', '{email}', '{bio}', {entrevista}, {pratico}, {teorico},{softSkills})")
    db_conexao.commit()
    db_conexao.close()