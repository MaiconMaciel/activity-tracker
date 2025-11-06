import subprocess
import pandas as pd
from io import StringIO


def get_data():

    csv_path = "/opt/airflow/logs/raw_log.csv"

    command = (
        'Get-WinEvent -LogName System '
        '| Where-Object {$_.Id -eq 6005 -or $_.Id -eq 6006} '
        '| Select-Object TimeCreated, Id, LevelDisplayName, Message '
        '| ConvertTo-Csv -NoTypeInformation'
    )

    process = subprocess.run(
        ["powershell", "-command", command],
        capture_output=True,
        text=True
    )

    df = pd.read_csv(StringIO(process.stdout), encoding="utf-16")

    df.drop(['LevelDisplayName', 'Message'], axis=1, inplace=True)
    df['TimeCreated'] = pd.to_datetime(df['TimeCreated'], format='%d/%m/%Y %H:%M:%S', dayfirst=True)
    df['TimeCreated_HM'] = df['TimeCreated'].dt.strftime('%H:%M')
    df['Date'] = df["TimeCreated"].dt.date

    df.to_csv(csv_path, encoding="utf-16", index=False)
    print("Extract concluido")
