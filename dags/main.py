# Adicionar um cálculo de média semanal/mensal.

# Gerar um ranking de “dias mais produtivos”.

# Enviar notificações (ex: via Telegram) com o resumo diário.

# Integrar com APIs de sistema (Windows/macOS/Linux) pra medir tempo real de sessão.

from aiflow import DAG

from scripts.data_extract import get_data
from scripts.data_transform import create_log
from scripts.data_vis import create_graphs
from scripts.data_load import git_commit_push

# test a f*cking commit