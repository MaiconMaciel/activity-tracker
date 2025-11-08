# rodar cada script checqando se deu erro ou não
from scripts.data_extract import get_data
from scripts.data_transform import create_log
from scripts.data_vis import create_graphs
from scripts.data_load import git_commit_push


def runActivityTracker():
  try:
    get_data()
  except Exception  as e:
    print(f"Erro na extração de dados: {e}")
  else:
    print("Extração concluida")
    try:
      create_log()
    except Exception as e:
      print(f"Erro no create log/transform: {e}")
    else:
      print("Transform concluido")
      try:
        create_graphs()
      except Exception as e:
        print(f"Erro na visualização: {e}")
      else:
        print("Criação de Graficos concluido")
        try:
          git_commit_push()
        except Exception as e:
          print(f"Erro no Load/Push: {e}")
        else:
          print("Load/Push concluido")

runActivityTracker()