from transformers import pipeline, AutoTokenizer
import pandas as pd
import matplotlib.pyplot as plt

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
df = pd.read_csv("Resultados/comentarios_filtrados_masculinos.csv")
df['classificacao'] = df['comment_text'].apply(classifica_comentario)

df.to_csv("Toxic/toxicidade_masculina.csv", index=False)

# Contagem para o gráfico
contagem = df['classificacao'].value_counts()

# Gráfico de pizza com textos em negrito e título com espaçamento maior
plt.figure(figsize=(6, 6))
wedges, texts, autotexts = plt.pie(
    contagem,
    labels=contagem.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=["#66b3ff", "#ff6666"],
    textprops={'fontweight': 'bold'}  # Negrito nos textos
)

plt.title("Distribuição de Tóxicidade Personalidades Masculinas", fontweight='bold', pad=20)  # Título em negrito e espaçamento maior
plt.axis('equal')

# Salvar gráfico na pasta Toxic
plt.savefig("Toxic/personalidades_masculinas_toxicidade.png")
plt.show()
