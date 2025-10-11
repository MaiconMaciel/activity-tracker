import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import seaborn as sns
from matplotlib.patches import Rectangle

plt.style.use("dark_background")
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.facecolor": "#0e0e0e",
    "figure.facecolor": "#000000",
    "axes.labelcolor": "#E0E0E0",
    "xtick.color": "#AAAAAA",
    "ytick.color": "#AAAAAA",
    "grid.color": "#222222",
})

df = pd.read_csv("./logs/log.csv")

df["horas_totais"] = pd.to_timedelta(df["horas_totais"]).dt.total_seconds() / 3600
df["data"] = pd.to_datetime(df["data"])

media_global = df["horas_totais"].mean()

# heatmap
df["semana"] = df["data"].dt.isocalendar().week
df["dia_semana"] = df["data"].dt.day_name()

dias_ordem = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
df["dia_semana"] = pd.Categorical(df["dia_semana"], categories=dias_ordem, ordered=True)

pivot = df.pivot_table(index="dia_semana", columns="semana", values="horas_totais", aggfunc="mean", observed=False)

plt.figure(figsize=(10, 4), dpi=200)
sns.heatmap(pivot, cmap="rocket_r", linewidths=0.4, cbar_kws={'label': 'Horas'})
plt.title("Mapa de calor - Horas por dia da semana", fontsize=13, color="white", pad=10)
plt.xlabel("Semana do ano")
plt.ylabel("Dia da semana")
plt.text(pivot.shape[1]-0.5, -0.8, f"Média Global: {media_global:.2f}h", color="white", fontsize=9, ha="right")
plt.tight_layout()
plt.savefig("./graphs/activity_heatmap.png", dpi=300, bbox_inches="tight")
plt.close()

# barras
fig, ax = plt.subplots(figsize=(10, 5), dpi=200)

ax.bar(
    df["data"], df["horas_totais"],
    color="#4e1d4b",
    edgecolor="#2e003a",
    linewidth=0.1,
    alpha=0.9
)

ax.axhline(media_global, color="#e43841", linestyle="--", linewidth=1.5, label=f"Média Global ({media_global:.2f}h)")

ax.set_xticks(df["data"])
ax.set_xticklabels(df["data"].dt.strftime("%d/%m"), rotation=90, ha="center", fontsize=8)

ax.set_title("Activity Tracker - 30 dias", fontsize=13, color="white", pad=10)
ax.set_ylabel("Horas (h)")
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.grid(True, linestyle="-", linewidth=0.5, alpha=0.75)
ax.legend(frameon=False, loc="upper left", fontsize=9, labelcolor="#CCCCCC")

plt.tight_layout()
plt.savefig("./graphs/activity_last30.png", dpi=300, bbox_inches="tight")
plt.close()
