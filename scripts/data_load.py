import pandas as pd
from datetime import datetime
import os

def git_commit_push(commit_message="Atualização automática do tracker"):
    import subprocess

    try:
        print('Oi')
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)     

    except subprocess.CalledProcessError as e:
        print("Erro git:", e)

    else:
        # log simples se push ocorrer sem problemas
        path = "./logs/git.csv"
        if not os.path.exists(path) or os.path.getsize(path) == 0:
            df = pd.DataFrame(columns=["data", "push"])
        else:
            df = pd.read_csv(path)
            date = datetime.now()
            push = 1 
            df = pd.concat([df, pd.DataFrame([{
                "data": date,
                "push": push
                }])], ignore_index=True)
            df.to_csv(path, index=False)


        print("Loaded")