import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt


# Carrega CSV já existente
df = pd.read_csv('personalidades_femininas.csv')

# Dicionário de mapeamento de palavras -> categoria (mantido o seu)
mapeamento_categorias = {
    # Racismo
    "macaco": "racismo",
    "macacão": "racismo",
    "macaquinho": "racismo",
    "negro": "racismo",
    "negrinho": "racismo",
    "negrão": "racismo",
    "negra": "racismo",
    "negrinha": "racismo",
    "negrona": "racismo",
    "criolo": "racismo",
    "criolina": "racismo",
    "criolu": "racismo",
    "criola": "racismo",
    "escravo": "racismo",
    "escravinho": "racismo",
    "escravão": "racismo",
    "escrava": "racismo",
    "escrivinha": "racismo",
    "escrivona": "racismo",
    "subhumano": "racismo",
    "sub-humano": "racismo",
    "subhumana": "racismo",
    "sub-raça": "racismo",
    "sub-raças": "racismo",
    "cabelo ruim": "racismo",
    "cabelo ruimzinho": "racismo",
    "cabelo ruimzão": "racismo",
    "tição": "racismo",
    "tizil": "racismo",
    "senzala": "racismo",
    "senzalinha": "racismo",



    # Homofobia
    "viado": "homofobia",
    "viadinho": "homofobia",
    "viadão": "homofobia",
    "viada": "homofobia",
    "viadinha": "homofobia",
    "viadona": "homofobia",
    "sapatão": "homofobia",
    "sapatona": "homofobia",
    "sapatinha": "homofobia",
    "sapatinho": "homofobia",
    "travecão": "homofobia",
    "traveca": "homofobia",
    "travequinha": "homofobia",
    "travequinho": "homofobia",
    "viadagem": "homofobia",
    "bicha": "homofobia",
    "bichinha": "homofobia",
    "bichona": "homofobia",
    "traveco": "homofobia",
    "lésbica": "homofobia",
    "lésbico": "homofobia",
    "lésbicas": "homofobia",
    "lésbicos": "homofobia",
    "gayzinho": "homofobia",
    "gayzona": "homofobia",
    "gayzão": "homofobia",
    "boiola": "homofobia",
    "bioba": "homofobia",
    "biba": "homofobia",
    "bibinha": "homofobia",
    "bibona": "homofobia",
    "froba": "homofobia",
    "frobinha": "homofobia",
    "frobona": "homofobia",
    "baitola": "homofobia",
    "baitolinha": "homofobia",
    "baitolona": "homofobia",


    # Etarismo (preconceito contra idosos/idade)
    "velho": "etarismo",
    "velha": "etarismo",
    "velhaço": "etarismo",
    "velhaça": "etarismo",
    "velhão": "etarismo",
    "velhona": "etarismo",
    "múmia": "etarismo",
    "mumazinha": "etarismo",
    "mumão": "etarismo",
    "calvo": "etarismo",
    "calvinho": "etarismo",
    "calvão": "etarismo",
    "calva": "etarismo",
    "calvinha": "etarismo",
    "calvona": "etarismo",
    "caducado": "etarismo",
    "caducadinho": "etarismo",
    "caducadona": "etarismo",


    # Classismo
    "pobre": "classismo",
    "pobrezinho": "classismo",
    "pobrezinha": "classismo",
    "pobres": "classismo",
    "pobreza": "classismo",
    "mendigo": "classismo",
    "mendiguinho": "classismo",
    "mendigona": "classismo",
    "mendiga": "classismo",
    "periferia": "classismo",
    "periférico": "classismo",
    "miserável": "classismo",
    "miseravélzinho": "classismo",
    "favelado": "classismo",
    "faveladinho": "classismo",
    "faveladona": "classismo",
    "favelada": "classismo",


    # capacitismo
    "idiota": "capacitismo",
    "idiotinha": "capacitismo",
    "idiotão": "capacitismo",
    "burro": "capacitismo",
    "burrinho": "capacitismo",
    "burrão": "capacitismo",
    "burra": "capacitismo",
    "burrinha": "capacitismo",
    "burrona": "capacitismo",
    "estúpido": "capacitismo",
    "estupidinho": "capacitismo",
    "estupidão": "capacitismo",
    "estúpida": "capacitismo",
    "estupidinha": "capacitismo",
    "estupidona": "capacitismo",
    "imbecil": "capacitismo",
    "imbecilzinho": "capacitismo",
    "imbecilão": "capacitismo",
    "retardado": "capacitismo",
    "retardadinho": "capacitismo",
    "retardadão": "capacitismo",
    "retardada": "capacitismo",
    "retardadinha": "capacitismo",
    "retardadona": "capacitismo",
    "deficiente": "capacitismo",
    "deficientinho": "capacitismo",
    "deficientão": "capacitismo",
    "lesado": "capacitismo",
    "lesadinho": "capacitismo",
    "lesadão": "capacitismo",
    "lesada": "capacitismo",
    "lesadinha": "capacitismo",
    "lesadona": "capacitismo",
    "anormal": "capacitismo",
    "anormalzinho": "capacitismo",
    "anormalão": "capacitismo",
    "mongol": "capacitismo",
    "mongolzinho": "capacitismo",
    "mongolão": "capacitismo",
    "mongoloide": "capacitismo",
    "mongoloidinho": "capacitismo",
    "mongoloidão": "capacitismo",
    "paspalho": "capacitismo",
    "paspalhinho": "capacitismo",
    "paspalhão": "capacitismo",
    "paspalha": "capacitismo",
    "paspalhinha": "capacitismo",
    "paspalhona": "capacitismo",
    "aleijado": "capacitismo",
    "aleijada": "capacitismo",
    "aleijadinho": "capacitismo",
    "aleijadinha": "capacitismo",
    "aleijadão": "capacitismo",
    "aleijadona": "capacitismo",
    "defeituoso": "capacitismo",
    "defeituosa": "capacitismo",
    "defeituosinho": "capacitismo",
    "defeituosinha": "capacitismo",
    "defeituosão": "capacitismo",
    "defeituosona": "capacitismo",
    "retardado": "capacitismo",
    "retardada": "capacitismo",
    "retardadinho": "capacitismo",
    "retardadinha": "capacitismo",
    "retardadão": "capacitismo",
    "retardadona": "capacitismo",
    "mongoloide": "capacitismo",
    "mongol": "capacitismo",
    "mongolzinho": "capacitismo",
    "mongolzinha": "capacitismo",
    "mongolão": "capacitismo",
    "mongolona": "capacitismo",
    "deficientezinho": "capacitismo",
    "deficientezinha": "capacitismo",
    "deficientão": "capacitismo",
    "deficientona": "capacitismo",
    "doente mental": "capacitismo",
    "mentalzinho": "capacitismo",
    "mentalzinha": "capacitismo",
    "lesado": "capacitismo",
    "lesada": "capacitismo",
    "lesadinho": "capacitismo",
    "lesadinha": "capacitismo",
    "lesadão": "capacitismo",
    "lesadona": "capacitismo",
    "paralitico": "capacitismo",
    "paralitica": "capacitismo",
    "paraliticuzinho": "capacitismo",
    "paraliticozinha": "capacitismo",
    "paraliticozão": "capacitismo",
    "paraliticozona": "capacitismo",

    #intolerancia religiosa

    "macumbeiro": "intolerância religiosa",
    "macumbeira": "intolerância religiosa",
    "macumbinha": "intolerância religiosa",
    "macumbeirinha": "intolerância religiosa",
    "macumbeirão": "intolerância religiosa",
    "macumbeirona": "intolerância religiosa",
    "endemoniado": "intolerância religiosa",
    "endemoniada": "intolerância religiosa",
    "endemoniadinho": "intolerância religiosa",
    "endemoniadona": "intolerância religiosa",
    "satanista": "intolerância religiosa",
    "adorador do diabo": "intolerância religiosa",
    "filho do capeta": "intolerância religiosa",
    "demoníaco": "intolerância religiosa",
    "demoníaca": "intolerância religiosa",
    "paganismo": "intolerância religiosa",
    "crentelho": "intolerância religiosa",
    "crentinha": "intolerância religiosa",
    "evanjegue": "intolerância religiosa",
    "evangélico idiota": "intolerância religiosa",
    "crente fanático": "intolerância religiosa",
    "seita": "intolerância religiosa",
    "seita doida": "intolerância religiosa",
    "igreja do capeta": "intolerância religiosa",

    # machismo
    "vadia": "machismo",
    "vagabunda": "machismo",
    "puta": "machismo",
    "piranha": "machismo",
    "biscate": "machismo",
    "safada": "machismo",
    "galinha": "machismo",
    "bruaca": "machismo",
    "cachorra": "machismo",
    "rodada": "machismo",
    "marafona": "machismo",
    "interesseira": "machismo",
    "oferecida": "machismo",
    "louca": "machismo",
    "histerica": "machismo",
    "mandona": "machismo",
    "feminazi": "machismo",
    "submissa": "machismo",
    "folgada": "machismo",
    "folgadinha": "machismo",
    "mal comida": "machismo",
    "mal amada": "machismo",
    "sensível demais": "machismo",
    "nojenta": "machismo",
    "emocionada": "machismo",
    "enxerida": "machismo",
    "frágil": "machismo",
    "melindrosa": "machismo",
    "mulher é na cozinha": "machismo",
    "vagaba": "machismo",
    "piriguete": "machismo",
    "rampeira": "machismo",
    "muquirana": "machismo",
    "interessadinha": "machismo",
    "mulherzinha": "machismo",
    "passiva": "machismo",
    "mandada": "machismo",
    "subordinada": "machismo",
    "mandona": "machismo",
    "insuportável": "machismo",
    "mexerica": "machismo",
    "frígida": "machismo",
    "emotiva": "machismo",
    "fofoqueira": "machismo",
    "fresca": "machismo",
    "recatada": "machismo",
    "sem dono": "machismo",
    "encalhada": "machismo",
    "mal amada": "machismo",
    "mal resolvida": "machismo",
    "ficadeira": "machismo",
    "pegadora": "machismo",
    "comida fácil": "machismo",
    "presa fácil": "machismo",

    #xenofobia
    "paraíba": "xenofobia",
    "paraibada": "xenofobia",
    "baianada": "xenofobia",
    "baiano preguiçoso": "xenofobia",
    "nordestino burro": "xenofobia",
    "nordestino ignorante": "xenofobia",
    "nordestino fedido": "xenofobia",
    "estrangeiro burro": "xenofobia",
    "gringo idiota": "xenofobia",
    "imigrante ilegal": "xenofobia",
    "imigrante lixo": "xenofobia",
    "venezuelano nojento": "xenofobia",
    "haitiano fedido": "xenofobia",
    "boliviano ladrão": "xenofobia",
    "chinês imundo": "xenofobia",
    "chinês porco": "xenofobia",
    "muçulmano terrorista": "xenofobia",
    "árabe terrorista": "xenofobia",
    "africano pobre": "xenofobia",
    "argentino metido": "xenofobia",
    "japonês esquisito": "xenofobia",
    "peruano fedorento": "xenofobia",
    "coreano estranho": "xenofobia",
    "latino sujo": "xenofobia",
    "indiano fedorento": "xenofobia",
    "volta pro seu país": "xenofobia",
    "só vem roubar emprego": "xenofobia",
    "não sabe nem falar direito": "xenofobia",
    "fala direito": "xenofobia",
    "aqui não é lugar pra estrangeiro": "xenofobia",
    "estrangeiro só dá trabalho": "xenofobia",
    "nordestino só serve pra votar errado": "xenofobia",
    "cara de estrangeiro": "xenofobia",
    "sotaque ridículo": "xenofobia",
    "gente preguiçosa": "xenofobia",
    "não mistura com esse povo": "xenofobia",


    # gordofobia
   "gordo": "gordofobia",
    "gorducho": "gordofobia",
    "gordão": "gordofobia",
    "gorda": "gordofobia",
    "gorducha": "gordofobia",
    "gordona": "gordofobia",
    "obeso": "gordofobia",
    "obesa": "gordofobia",
    "baleia": "gordofobia",
    "gordice": "gordofobia",
    "barrigão": "gordofobia",
    "flácido": "gordofobia",
    "flácida": "gordofobia",
    "pançudo": "gordofobia",
    "pançuda": "gordofobia",
    "leitão": "gordofobia",
    "leitona": "gordofobia",
    "bolota": "gordofobia",
    "bolotinha": "gordofobia",
    "bolotão": "gordofobia",
    "gordinho": "gordofobia",
    "gordinha": "gordofobia",
    "gordalhão": "gordofobia",
    "gordalhona": "gordofobia",
    "buchuda": "gordofobia",
    "buchudo": "gordofobia",
    "rolha": "gordofobia",
    "rolhão": "gordofobia",
    "rolhinha": "gordofobia",
    "balofo": "gordofobia",
    "balofa": "gordofobia",
    "balofozinho": "gordofobia",
    "balofinha": "gordofobia",
    "balofozão": "gordofobia",
    "balofona": "gordofobia",
    "roliço": "gordofobia",
    "roliça": "gordofobia",
    "rolicinho": "gordofobia",
    "rolicinha": "gordofobia",
    "rolição": "gordofobia",
    "roliçona": "gordofobia",
    "banha": "gordofobia",
    "banhinha": "gordofobia",
    "banhona": "gordofobia"

} # seu mapeamento completo aqui

# 3. Função para detectar categorias
def detectar_categorias(texto):
    categorias = set()
    if pd.isnull(texto):
        return []
    texto = texto.lower()
    for palavra, categoria in mapeamento_categorias.items():
        if re.search(r'\b' + re.escape(palavra) + r'\b', texto):
            categorias.add(categoria)
    return list(categorias)

# 4. Aplica função
df['categorias'] = df['comment_text'].apply(detectar_categorias)

# 5. Contagens
total_comentarios = len(df)
contador = Counter(cat for subcats in df['categorias'] for cat in subcats)
total_filtrados = sum(contador.values())

# 6. Prepara dados da tabela
dados = []
for categoria, quantidade in contador.items():
    porcentagem = f"{(quantidade / total_filtrados) * 100:.1f}%"
    dados.append([categoria.capitalize(), quantidade, porcentagem])

# Ordenar por quantidade (opcional)
dados.sort(key=lambda x: x[1], reverse=True)

# 7. Gera tabela como imagem
fig, ax = plt.subplots(figsize=(8, len(dados) * 0.6 + 2))

plt.suptitle("Comentários analisados personalidades femininas", fontsize=16, fontweight='bold', y=1.05)

plt.text(0.5, 1.0,
         f'Total de Comentários Analisados: {total_comentarios}\nTotal de Comentários Filtrados: {total_filtrados}',
         ha='center', va='top', fontsize=13, fontweight='bold', transform=ax.transAxes)


ax.axis('off')

col_labels = ["Categoria", "Quantidade", "Porcentagem"]
table = ax.table(cellText=dados, colLabels=col_labels, loc='center', cellLoc='center')

table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1, 2)

plt.tight_layout()
plt.savefig("Resultados/tabela_femina.png", dpi=300, bbox_inches='tight')
plt.show()

# Filtrar apenas comentários que possuem pelo menos uma categoria identificada
df_filtrados = df[df['categorias'].apply(lambda x: len(x) > 0)]

# Salvar os comentários filtrados em um CSV
df_filtrados.to_csv("Resultados/comentarios_filtrados_femininos.csv", index=False)

print(f"Total de comentários filtrados salvos: {len(df_filtrados)}")

print("Tabela gerada e salva")