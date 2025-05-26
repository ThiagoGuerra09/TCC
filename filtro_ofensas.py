import pandas as pd
import re

# 1. Carregar o CSV original
df = pd.read_csv("TCC/Amostras/comentarios_camila_loures.csv")

# 2. Lista de palavras ofensivas (você pode adicionar mais depois)
palavras_ofensivas = [
   "macaco", "negro", "negra", "negrinho", "negrinha", "criolo", "criola", "escravo", "escrava", "subhumano", "sub-raça", "africano", "africana", "cabelo ruim",
"viado", "viada", "sapatão", "sapatona", "travecão", "traveca", "viadinho", "viadinha", "bicha", "bichão", "traveco", "drag queen", "lésbica", "lésbico", "gayzinho", "viadagem", "transfóbico",
"bicho velho", "bicho velha", "velhaço", "velhaça", "múmia", "múmia velha", "demente", "calvo", "calva",
"otário", "otária", "nojento", "nojenta", "desgraçado", "desgraçada", "corno", "corna", "traidor", "traidora", "arrombado", "arrombada", "covarde", "lixo humano", "marginal", "esquisito", "esquisita", "furdunço", "babaca",
"vagabundo", "vagabunda", "doente", "vaca", "chifrudo", "chifruda", "bunda mole",
"piranha", "puta", "puta velha", "vagabunda", "rapariga", "prostituta",
"pobre", "pobreza", "mendigo", "mendiga", "periferia", "miserável", "favelado", "favelada",
"idiota", "burro", "burra", "estúpido", "estúpida", "imbecil",
"gordo", "gorda", "gorducho", "gorducha", "gordão", "gordona", "obeso", "obesa", "baleia de carga", "gordice", "barriga de chope", "flácido", "pançudo"


]

# 3. Função para detectar presença de palavras ofensivas no comentário
def detectar_cyberbullying(texto):
    if pd.isnull(texto):
        return 0  
    
    # Criar expressão regular para capturar palavras inteiras, ignorando maiúsculas/minúsculas
    regex = r'\b(?:' + '|'.join(re.escape(palavra) for palavra in palavras_ofensivas) + r')\b'
    
    # Transformar para minúsculo para fazer comparação sem diferenciar maiúsculas/minúsculas
    texto = texto.lower()
    
    # Verificar se a expressão regular encontra uma das palavras ofensivas
    if re.search(regex, texto):
        return 1  # Se encontrar uma palavra ofensiva, marca
    
    return 0  # Se nenhuma palavra ofensiva encontrada

# 4. Aplicar a função a todos os comentários
df['cyberbullying'] = df['comment_text'].apply(detectar_cyberbullying)

# 5. Filtrar apenas comentários classificados
df_cyberbullying = df[df['cyberbullying'] == 1]

# 6. Salvar os comentários ofensivos em um novo CSV
df_cyberbullying.to_csv('TCC/Comentarios_Filtrados/comentarios_cyberbullying_camila_loures.csv', index=False)

print("Detecção concluída. Comentários ofensivos salvos.")