import pandas as pd
import re

# 1. Carregar o CSV original
df = pd.read_csv("TCC/Amostras/comentarios_enaldinho.csv")

# 2. Lista de palavras ofensivas (você pode adicionar mais depois)
palavras_ofensivas = [
    "idiota", "burro", "otário", "nojento", "estúpido", "imbecil", 
    "desgraçado", "babaca", "vagabundo", "corno", "traidor", "gordo", "viado", 
    "sapatão", "doente", "gorducho", "travecão", "macaco", "negro", 
    "cabelo ruim", "arrombado", "covarde", "vaca", "chifrudo", 
    "bunda mole", "burra", "piranha", "puta", "puta velha", "negrinho", "criolo", 
    "escravo", "favelado", "favelada", "subhumano", 
    "sub-raça", "africano", "gordão", "obeso", "baleia de carga", 
    "gordice", "furdunço", "barriga de chope", "flácido", "pançudo", "viadinho", 
    "bicha", "traveco", "puto", "viado lixo", "arrombado", "drag queen", 
    "lésbica", "gayzinho", "viadagem", "transfóbico", 
    "pobre", "mendigo", "periferia", 
    "lixo humano", "marginal", "vagabunda", "rapariga", "prostituta", "miserável", 
    "esquisito",  "bicho velho", "velhaço", "múmia", "demente", 
     "calvo"

]

# 3. Função para detectar presença de palavras ofensivas no comentário
def detectar_cyberbullying(texto):
    if pd.isnull(texto):
        return 0  # Comentário vazio, não classifica como cyberbullying
    
    # Criar expressão regular para capturar palavras inteiras, ignorando maiúsculas/minúsculas
    regex = r'\b(?:' + '|'.join(re.escape(palavra) for palavra in palavras_ofensivas) + r')\b'
    
    # Transformar para minúsculo para fazer comparação sem diferenciar maiúsculas/minúsculas
    texto = texto.lower()
    
    # Verificar se a expressão regular encontra uma das palavras ofensivas
    if re.search(regex, texto):
        return 1  # Se encontrar uma palavra ofensiva, marca como cyberbullying
    
    return 0  # Se nenhuma palavra ofensiva encontrada

# 4. Aplicar a função a todos os comentários
df['cyberbullying'] = df['comment_text'].apply(detectar_cyberbullying)

# 5. Filtrar apenas comentários classificados como cyberbullying
df_cyberbullying = df[df['cyberbullying'] == 1]

# 6. Salvar os comentários ofensivos em um novo CSV
df_cyberbullying.to_csv('TCC/Comentarios_Filtrados/comentarios_cyberbullying_enaldinho.csv', index=False)

print("Detecção concluída. Comentários ofensivos salvos.")