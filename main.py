import pandas as pd
from sqlalchemy import create_engine


dados = pd.read_csv("diabetes.csv")

caminho_banco_dados = "C:\\Users\\Giovanni\\PycharmProjects\\Projeto 1 Analise de Danos com Python\\pacientes.db"
engine = create_engine(f'sqlite:///{caminho_banco_dados}', echo=False)
dados.to_sql('pacientes', con=engine, if_exists='replace', index=False)

# Executar consultas SQL para filtrar pacientes com mais de 50 anos e calcular o índice de massa corporal (IMC)
consulta_sql = """SELECT *,
           CASE
               WHEN age > 50 AND BMI >= 30 THEN 'obeso'
               ELSE 'normal'
           END AS status_obesidade
    FROM pacientes
    WHERE age > 50"""""


dados_transformados = pd.read_sql_query(consulta_sql, engine)

print(dados_transformados.head())

dados_transformados.to_csv('dados_transformados.csv', index=False)
