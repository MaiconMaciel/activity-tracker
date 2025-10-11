import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# --- Configuração estética global ---
plt.style.use("dark_background")
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.facecolor": "#1E1E1E",
    "axes.edgecolor": "#333333",
    "axes.labelcolor": "#E0E0E0",
    "xtick.color": "#AAAAAA",
    "ytick.color": "#AAAAAA",
    "grid.color": "#333333",
    "figure.facecolor": "#0E0E0E",
})

# --- Ler o log consolidado ---
df = pd.read_csv("./logs/log.csv")

# Converter colunas de tempo
df["horas_totais"] = pd.to_timedelta(df["horas_totais"]).dt.total_seconds() / 3600
df["data"] = pd.to_datetime(df["data"])

# --- Criar o gráfico ---
fig, ax = plt.subplots(figsize=(10, 5), dpi=200)

# linha principal
ax.plot(df["data"], df["horas_totais"], color="#7FB3FF", linewidth=2, label="Horas totais")

# preencher área sob a curva
ax.fill_between(df["data"], df["horas_totais"], color="#7FB3FF", alpha=0.2)

# destacar o último ponto
ax.scatter(df["data"].iloc[-1], df["horas_totais"].iloc[-1],
           color="#FFD166", s=80, zorder=5, label="Último dia")

# Títulos e rótulos
ax.set_title("Tempo total no PC por dia", fontsize=14, color="#FFFFFF", pad=10)
ax.set_ylabel("Horas (h)")
ax.set_xlabel("Data")

# grade e limites
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.grid(True, linestyle="--", linewidth=0.6, alpha=0.4)

# remover bordas superiores e direitas (estilo clean)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# legenda
ax.legend(frameon=False, loc="upper left", fontsize=10, labelcolor="#CCCCCC")

# margem visual
plt.tight_layout()

# salvar imagem em alta resolução
plt.savefig("activity.png", dpi=300, bbox_inches="tight")
plt.close()
