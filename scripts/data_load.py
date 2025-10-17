

def git_commit_push(commit_message="Atualização automática do tracker"):
    import subprocess

    try:
        # Adiciona todas as alterações
        subprocess.run(["git", "add", "."], check=True)

        # Commit
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Push
        subprocess.run(["git", "push"], check=True)

        print("✅ Commit e push realizados com sucesso!")
    except subprocess.CalledProcessError as e:
        print("❌ Erro ao executar git:", e)

