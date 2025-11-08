import pandas as pd
import datetime

def git_commit_push(commit_message="Atualização automática do tracker"):
    import subprocess

    try:
        subprocess.run(["git", "add", "."], check=True)

        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        subprocess.run(["git", "push"], check=True)     

    except subprocess.CalledProcessError as e:
        print("Erro git:", e)

    else:
        #log de push - com data e hora ? só pra ter sla
        df = pd.read_csv("./logs/git.csv")

        date = datetime.now(ZoneInfo="America/Sao_Paulo")
        push = True 

        df.append({
            "data": date,
            "push": push
        })

        print("Commit e push sucesso!") 

git_commit_push()