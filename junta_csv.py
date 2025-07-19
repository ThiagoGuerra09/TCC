import pandas as pd

# Lista dos arquivos CSV
arquivos = [
    "Amostras/comentarios_bispo_bruno.csv",
    "Amostras/comentarios_enaldinho.csv",
    "Amostras/comentarios_felipe_neto.csv",
    "Amostras/comentarios_rezendeevil.csv",
    "Amostras/comentarios_winderson.csv"
]

# Ler e juntar todos em um único DataFrame
df_final = pd.concat([pd.read_csv(arquivo) for arquivo in arquivos], ignore_index=True)

# Salvar em um novo arquivo CSV
df_final.to_csv("personalidades_masculinas.csv", index=False, encoding="utf-8-sig")

print("✅ Arquivo único gerado com sucesso!")
