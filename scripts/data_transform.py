# transform data



def create_log():
  import pandas as pd

  df = pd.read_csv("logs/raw_log.csv", encoding="utf-16")
  grouped = df.groupby('Date')
  group_size = grouped.size()
  dia = []
  
  for date, group in grouped:
      
      grouped = group.sort_values('TimeCreated', ascending=True)
      # group é todas as linhas agrupadas de um dia
      #print(f'group={group}')
      #entrada e saida do grafico
      entrada_final = group.loc[group['Id']==6005, 'TimeCreated'].min()
      saida_final   = group.loc[group['Id']==6006, 'TimeCreated'].max()

      #lista com horarios do dia
      lista = []
      for index, line in group.iterrows():
         lista.append(line["TimeCreated"])
      lista.sort()

      #calcular tempo
      tempo_total_dia = pd.Timedelta(0)
      for i in range(0, len(lista)-1, 2):
        entrada = pd.Timestamp(lista[i])
        saida = pd.Timestamp(lista[i+1])
        tempo_total_dia += saida - entrada

        
        #print(f'total dia "{date}": {tempo_total_dia}')

      dia.append({
        "data": date,
        "entrada": entrada_final if pd.notna(entrada_final) else False,
        "saída": saida_final if pd.notna(saida_final) else False,
        "sessoes": len(lista) // 2,
        "horas_totais": tempo_total_dia
      })

  df_log = pd.DataFrame(dia)

  df_log.to_csv("logs/log.csv",  index=False, encoding="utf-8")
  