# Projeto 1 - DataBase

## Meu primeiro projeto utilizando Python (biblioteca Pandas) e SQL.
## O desafio proposto era o seguinte:

## "Temos em mãos um arquivo com dados de pacientes que desenvolveram ou não diabetes. Precisamos gerar uma amostra de dados com os pacientes com mais de 50 anos e para cada um deles indicar em uma nova coluna se o paciente está normal (índice de massa corpórea menor que 30) ou obeso (índice de massa corpórea maior ou igual a 30). Então devemos gerar um novo arquivo CSV e encaminhar para o Cientista de Dados. Vamos resolver esse problema com Banco de Dados, Python e SQL. Os dados serão inicialmente carregados com Linguagem Python. Faremos então uma cópia dos dados para um banco de dados e usaremos Linguagem SQL para as transformações necessárias. Por fim, copiaremos os dados transformados de volta para um dataframe do Pandas para salvar o resultado em formato CSV."

## O primeiro passou foi importar as bibliotecas utilizadas no projeto:
''' import pandas as pd
from sqlalchemy import create_engine
'''

## Em seguida ler o dataframe original utilizando o pandas:
''' dados = pd.read_csv("diabetes.csv") '''

## Após a leitura eu indiquei o caminho e criei o banco de dados, transferindo o arquivo CSV para ele:
'''caminho_banco_dados = "C:\\Users\\Giovanni\\PycharmProjects\\Projeto 1 Analise de Danos com Python\\pacientes.db"
engine = create_engine(f'sqlite:///{caminho_banco_dados}', echo=False)
dados.to_sql('pacientes', con=engine, if_exists='replace', index=False)'''

## Então realizei a consulta e transformação no banco de dados de acordo com o que foi pedido no enunciado do desafio, criando uma nova coluna com o status do paciente (se é obeso ou não) e depois separando apenas os pacientes com mais de 50 anos:
'''consulta_sql = """SELECT *,
           CASE
               WHEN age > 50 AND BMI >= 30 THEN 'obeso'
               ELSE 'normal'
           END AS status_obesidade
      FROM pacientes
      WHERE age > 50"""""

   dados_transformados = pd.read_sql_query(consulta_sql, engine)
    '''

## E por fim criei um novo arquivo CSV com os dados transformados:
''' dados_transformados.to_csv('dados_transformados.csv', index=False) '''


Certifique-se de que o arquivo "dados_pacientes.csv" esteja no mesmo diretório ou forneça o caminho completo para o arquivo no código Python.

O arquivo "dados_transformados.csv" será gerado com os resultados da análise.

## Requisitos do sistema

- Python 3.x
- Pandas
- SQLAlchemy

## Contribuições

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, correções de bugs ou novos recursos, sinta-se à vontade para abrir um problema (issue) ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
