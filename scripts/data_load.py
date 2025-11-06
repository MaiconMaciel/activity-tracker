

def git_commit_push(commit_message="Atualização automática do tracker"):
    import subprocess

    try:
        subprocess.run(["git", "add", "."], check=True)

        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        subprocess.run(["git", "push"], check=True)

        print("Commit e push realizados com sucesso!")
    except subprocess.CalledProcessError as e:
        print("Erro ao executar git:", e)

git_commit_push()