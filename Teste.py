import os
import pandas as pd
import json

# Definindo o caminho para o arquivo JSON
file_json = 'C:\\Users\\samue\\Desktop\\CACTUS\\arquivojson.json'

# Abrindo e carregando o arquivo JSON em um dicionário
with open(file_json, 'r') as arquivo:
    data_string = json.load(arquivo)

# convertendo em DataFrame
data = data_string['dice777']['game_results']
df = pd.DataFrame.from_dict(data, orient='index')
df.reset_index(inplace=True)

# Salvando o DataFrame em um arquivo xlsx
df.to_excel('C:\\Users\\samue\\Desktop\\CACTUS\\Arquivo_Extraido.xlsx', index=False)

# Contando a quantidade de valores True e False na coluna 'success'
count = df['success'].value_counts()
quantidade_true = count.get(True, 0)
quantidade_falso = count.get(False, 0)

# Imprimindo as quantidades de valores True e False e a contagem total
print("Quantidade de True:", quantidade_true)
print("Quantidade de False:", quantidade_falso)
print("Contagem total de 'success':", count)

# Contando a quantidade de valores '200' e '400' na coluna 'status_code'
count_status_code = df['status_code'].value_counts()
Qtd_200 = count_status_code.get(200, 0)
Qtd_400 = count_status_code.get(400, 0)

# Imprimindo a quantidade de valores '200' e '400'
print("Quantidade de '200' na coluna 'status_code':", Qtd_200)
print("Quantidade de '400' na coluna 'status_code':", Qtd_400)

# Filtrando todos os registros em que a coluna 'status_code' é igual a 400
registro_400 = df[df['status_code'] == 400]
print("Registros com 'status_code' igual a 400:")
print(registro_400)
