import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt


# 1. Carregar o CSV filtrado
df = pd.read_csv('TCC/Comentarios_Filtrados/comentarios_cyberbullying_resendeevil.csv')



# 2. Definir o mapeamento de palavras para categorias (mapeamento_categorias que montamos acima)
mapeamento_categorias = {
    # Racismo
    "macaco": "racismo",
    "negro": "racismo",
    "negrinho": "racismo",
    "criolo": "racismo",
    "escravo": "racismo",
    "favelado": "racismo",
    "favelada": "racismo",
    "subhumano": "racismo",
    "sub-raça": "racismo",
    "africano": "racismo",

    # Homofobia
    "viado": "homofobia",
    "sapatão": "homofobia",
    "travecão": "homofobia",
    "viadinho": "homofobia",
    "bicha": "homofobia",
    "traveco": "homofobia",
    "viado lixo": "homofobia",
    "drag queen": "homofobia",
    "lésbica": "homofobia",
    "gayzinho": "homofobia",
    "viadagem": "homofobia",
    "transfóbico": "homofobia",

    # Etarismo (preconceito contra idosos/idade)
    "bicho velho": "etarismo",
    "velhaço": "etarismo",
    "múmia": "etarismo",
    "demente": "etarismo",
    "calvo": "etarismo",

    # Ofensa direta (xingamentos ou insultos pessoais)
    "idiota": "ofensa",
    "burro": "ofensa",
    "otário": "ofensa",
    "nojento": "ofensa",
    "estúpido": "ofensa",
    "imbecil": "ofensa",
    "desgraçado": "ofensa",
    "babaca": "ofensa",
    "vagabundo": "ofensa",
    "corno": "ofensa",
    "traidor": "ofensa",
    "doente": "ofensa",
    "arrombado": "ofensa",
    "covarde": "ofensa",
    "vaca": "ofensa",
    "chifrudo": "ofensa",
    "bunda mole": "ofensa",
    "burra": "ofensa",
    "piranha": "ofensa",
    "puta": "ofensa",
    "puta velha": "ofensa",
    "cabelo ruim": "ofensa",
    "puto": "ofensa",
    "pobre": "ofensa",
    "mendigo": "ofensa",
    "periferia": "ofensa",
    "lixo humano": "ofensa",
    "marginal": "ofensa",
    "vagabunda": "ofensa",
    "rapariga": "ofensa",
    "prostituta": "ofensa",
    "miserável": "ofensa",
    "esquisito": "ofensa",
    "furdunço": "ofensa",

    # Palavrões em geral (ofensas ligadas ao corpo/físico)
    "gordo": "palavrões em geral",
    "gorducho": "palavrões em geral",
    "gordão": "palavrões em geral",
    "obeso": "palavrões em geral",
    "baleia de carga": "palavrões em geral",
    "gordice": "palavrões em geral",
    "barriga de chope": "palavrões em geral",
    "flácido": "palavrões em geral",
    "pançudo": "palavrões em geral"


}

# 3. Função para detectar categoria(s) no comentário
def detectar_categorias(texto):
    categorias_encontradas = set()
    if pd.isnull(texto):
        return []
    texto = texto.lower()
    for palavra, categoria in mapeamento_categorias.items():
        if re.search(r'\b' + re.escape(palavra) + r'\b', texto):
            categorias_encontradas.add(categoria)
    return list(categorias_encontradas)

# 4. Aplicar a função para cada comentário
df['categorias'] = df['comment_text'].apply(detectar_categorias)

# 5. Contar quantas vezes cada categoria apareceu
todas_categorias = []
for cats in df['categorias']:
    todas_categorias.extend(cats)

contador = Counter(todas_categorias)

# 6. Calcular porcentagem
total_comentarios = len(df)
porcentagem_categorias = {cat: (count / total_comentarios) * 100 for cat, count in contador.items()}

# 7. Gerar gráfico de pizza
labels = list(porcentagem_categorias.keys())
sizes = list(porcentagem_categorias.values())

# Gerar o gráfico
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Gráfico redondo
plt.title('Distribuição de Categorias de Cyberbullying Resendeevil')

# 8. Salvar o gráfico como PNG
plt.savefig('TCC/Resultados/resendeevil.png', dpi=300, bbox_inches='tight')

# Mostrar também na tela
plt.show()

print("\nGráfico salvo em: Resultados/grafico_categorias_cyberbullying.png")