from transformers import pipeline, AutoTokenizer
import pandas as pd
import matplotlib.pyplot as plt
import os

# Carregar modelo
tokenizer = AutoTokenizer.from_pretrained("unitary/toxic-bert")
classifier = pipeline("text-classification", model="unitary/toxic-bert", tokenizer=tokenizer, top_k=2, device=0)

# Função de classificação
def classifica_comentario(texto, threshold=0.05):
    if not isinstance(texto, str):
        return "não é texto"
    
    resultados = classifier(texto, truncation=True, max_length=512)
    
    for resultado in resultados[0]:
        if resultado["label"].lower() == "toxic":
            if resultado["score"] >= threshold:
                return "toxic"
            else:
                return "not_toxic"
    
    return "not_toxic"
# Carregar e classificar os comentários
df = pd.read_csv("Comentarios_Filtrados/comentarios_filtrados_resendeevil.csv")
df['classificacao'] = df['comment_text'].apply(classifica_comentario)

df.to_csv("Toxic/toxic_camila_loures.csv", index=False)

# Contagem para o gráfico
contagem = df['classificacao'].value_counts()

# Gráfico de pizza
plt.figure(figsize=(6, 6))
plt.pie(contagem, labels=contagem.index, autopct='%1.1f%%', startangle=140, colors=["#66b3ff", "#ff6666"])
plt.title("Distribuição de Comentários Tóxicos vs Não Tóxicos")
plt.axis('equal')

# Salvar gráfico na pasta Toxic
plt.savefig("Toxic/resendeevil_toxicidade.png")
plt.show()
