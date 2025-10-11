import subprocess
import pandas as pd
from io import StringIO

# Caminho do CSV
csv_path = "./logs/raw_log.csv"

# Comando PowerShell para pegar eventos 6005/6006 (login/logout)
command = (
    'Get-WinEvent -LogName System '
    '| Where-Object {$_.Id -eq 6005 -or $_.Id -eq 6006} '
    '| Select-Object TimeCreated, Id, LevelDisplayName, Message '
    '| ConvertTo-Csv -NoTypeInformation'
)

# Função para executar comando PowerShell e retornar saída
def get_data(command):
    process = subprocess.run(
        ["powershell", "-command", command],
        capture_output=True,
        text=True
    )
    return process

# Executa comando
process = get_data(command)

# Lê CSV diretamente da saída do PowerShell
df = pd.read_csv(StringIO(process.stdout), encoding="utf-16")

# Remove colunas que não interessam
df.drop(['LevelDisplayName', 'Message'], axis=1, inplace=True)
df['TimeCreated'] = pd.to_datetime(df['TimeCreated'], format='%d/%m/%Y %H:%M:%S', dayfirst=True)
df['TimeCreated_HM'] = df['TimeCreated'].dt.strftime('%H:%M')
df['Date'] = df["TimeCreated"].dt.date

# Salva DataFrame já arrumado
df.to_csv(csv_path, encoding="utf-16", index=False)

# Agora df tem apenas TimeCreated e Id
print(df.head())




#if data != data_no_csv:
#    altera_entrada
#    altera_saida
#    salva a soma?