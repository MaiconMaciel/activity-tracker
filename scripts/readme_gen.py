from datetime import datetime
import pandas as pd

df = pd.read_csv("./logs/log.csv")

ultima = df.iloc[-1]
media = df["horas_totais"].astype("timedelta64[h]").mean()

template = f"""
# 🧠 Productivity Tracker

Monitoramento automático do uso do PC (atualizado em {datetime.now().strftime("%d/%m/%Y %H:%M")}).

## 📈 Últimos dias
| Data | Horas Totais | Sessões |
|------|---------------|---------|
"""

for _, row in df.tail(7).iterrows():
    template += f"| {row['data']} | {row['horas_totais']} | {int(row['sessoes'])} |\n"

template += f"""
## 🕒 Estatísticas gerais
- Média diária: **{media:.1f} horas**
- Último dia: **{ultima['horas_totais']}**
- Total de dias registrados: **{len(df)}**

![Uso diário](activity.png)
![Mapa de calor](activity_heatmap.png)
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(template)
