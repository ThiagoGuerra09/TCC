import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt
# 1. Carregar o CSV filtrado
df = pd.read_csv('TCC/Comentarios_Filtrados/comentarios_filtrados_resendeevil.csv')

mapeamento_categorias = {
    # Racismo
    "macaco": "racismo",
    "negro": "racismo",
    "negra": "racismo",
    "negrinho": "racismo",
    "negrinha": "racismo",
    "criolo": "racismo",
    "criola": "racismo",
    "escravo": "racismo",
    "escrava": "racismo",
    "subhumano": "racismo",
    "sub-raça": "racismo",
    "africano": "racismo",
    "africana": "racismo",
    "cabelo ruim": "racismo",

    # Homofobia
    "viado": "homofobia",
    "viada": "homofobia",
    "sapatão": "homofobia",
    "sapatona": "homofobia",
    "travecão": "homofobia",
    "traveca": "homofobia",
    "viadinho": "homofobia",
    "viadinha": "homofobia",
    "bicha": "homofobia",
    "bichão": "homofobia",
    "traveco": "homofobia",
    "drag queen": "homofobia",
    "lésbica": "homofobia",
    "lésbico": "homofobia",
    "gayzinho": "homofobia",
    "viadagem": "homofobia",
    "transfóbico": "homofobia",

    # Etarismo (preconceito contra idosos/idade)
    "bicho velho": "etarismo",
    "bicho velha": "etarismo",
    "velhaço": "etarismo",
    "velhaça": "etarismo",
    "múmia": "etarismo",
    "múmia velha": "etarismo",
    "demente": "etarismo",
    "calvo": "etarismo",
    "calva": "etarismo",

    # Ofensa direta (xingamentos ou insultos pessoais)
  # Ofensa Moral
    "otário": "ofensa moral",
    "otária": "ofensa moral",
    "nojento": "ofensa moral",
    "nojenta": "ofensa moral",
    "desgraçado": "ofensa moral",
    "desgraçada": "ofensa moral",
    "corno": "ofensa moral",
    "corna": "ofensa moral",
    "traidor": "ofensa moral",
    "traidora": "ofensa moral",
    "arrombado": "ofensa moral",
    "arrombada": "ofensa moral",
    "covarde": "ofensa moral",
    "lixo humano": "ofensa moral",
    "marginal": "ofensa moral",
    "esquisito": "ofensa moral",
    "esquisita": "ofensa moral",
    "furdunço": "ofensa moral",
    "babaca": "ofensa moral",

    # Ofensa gerais
    "vagabundo": "ofensa",
    "vagabunda": "ofensa",
    "doente": "ofensa",
    "vaca": "ofensa",
    "chifrudo": "ofensa",
    "chifruda": "ofensa",
    "bunda mole": "ofensa",

    # Ofensa Sexual
    "piranha": "ofensa sexual",
    "puta": "ofensa sexual",
    "puta velha": "ofensa sexual",
    "vagabunda": "ofensa sexual",
    "rapariga": "ofensa sexual",
    "prostituta": "ofensa sexual",

    # Classismo
    "pobre": "classismo",
    "pobreza": "classismo",
    "mendigo": "classismo",
    "mendiga": "classismo",
    "periferia": "classismo",
    "miserável": "classismo",
    "favelado": "classismo",
    "favelada": "classismo",

    # Palavras relacionadas a capacidade cognitiva
    "idiota": "insulto cognitivo",
    "burro": "insulto cognitivo",
    "burra": "insulto cognitivo",
    "estúpido": "insulto cognitivo",
    "estúpida": "insulto cognitivo",
    "imbecil": "insulto cognitivo",

    # Palavrões em geral (ofensas ligadas ao corpo/físico)
    "gordo": "gordofobia",
    "gorda": "gordofobia",
    "gorducho": "gordofobia",
    "gorducha": "gordofobia",
    "gordão": "gordofobia",
    "gordona": "gordofobia",
    "obeso": "gordofobia",
    "obesa": "gordofobia",
    "baleia de carga": "gordofobia",
    "gordice": "gordofobia",
    "barriga de chope": "gordofobia",
    "flácido": "gordofobia",
    "pançudo": "gordofobia"
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

# 4. Aplicar função
df['categorias'] = df['comment_text'].apply(detectar_categorias)

# 5. Contagem
todas_categorias = []
for cats in df['categorias']:
    todas_categorias.extend(cats)

contador = Counter(todas_categorias)

# 6. Porcentagem
total_comentarios = len(df)
porcentagem_categorias = {cat: (count / total_comentarios) * 100 for cat, count in contador.items()}

# 7. Cores padronizadas por categoria
cores = {
    'racismo': 'saddlebrown',
    'homofobia': 'orchid',
    'etarismo': 'slategray',
    'ofensa moral': 'darkcyan',
    'ofensa': 'crimson',
    'ofensa sexual': 'deeppink',
    'classismo': 'darkorange',
    'insulto cognitivo': 'royalblue',
    'gordofobia': 'darkgreen'
}

# 8. Preparar dados para gráfico
labels = list(porcentagem_categorias.keys())
sizes = list(porcentagem_categorias.values())
colors = [cores[label] for label in labels]

# 9. Gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
plt.axis('equal')
plt.title('Distribuição de Categorias de Ofensas - Resendeevil')

# 10. Salvar e exibir
plt.savefig('TCC/Resultados/resendeevil.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nGráfico salvo")
