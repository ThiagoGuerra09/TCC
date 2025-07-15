import requests
import pandas as pd
from tqdm import tqdm
import re
import nltk
import string
from unidecode import unidecode
import os

# Baixar stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('portuguese'))

# Função de pré-processamento de texto
def clean_text(text):
    text = text.lower()
    text = unidecode(text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = re.sub(rf"[{re.escape(string.punctuation)}]", '', text)
    text = re.sub(r'\d+', '', text)
    words = text.split()
    filtered = [w for w in words if w not in stop_words]
    return ' '.join(filtered)

# Sua chave de API
API_KEY = "AIzaSyDEtRq1qdXdJEeAubuWBPJPXsXX-nk8hQo"

# Lista de vídeos
video_ids = [
"ExH89R0aWfk",
"qsUqWfB-ydI",
"aUGseCX7I6k",
"vQrCdIDdeuk",
"JtAi4Sj8jCA",
"qUXljiTyJbg",
"ybkfssrjHUk",
"nuyGsYRoCTI",
"aKeXWNg2J64",
"JvsjliIZtTQ" 
]

# Coleta de comentários
def get_comments(video_id, api_key):
    comments = []
    next_page_token = None

    while True:
        url = "https://www.googleapis.com/youtube/v3/commentThreads"
        params = {
            'part': 'snippet',
            'videoId': video_id,
            'pageToken': next_page_token,
            'maxResults': 100,
            'key': api_key
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        for item in response_data.get("items", []):
            snippet = item["snippet"]["topLevelComment"]["snippet"]
            raw_text = snippet["textDisplay"]
            clean = clean_text(raw_text)

            comments.append({
                "video_id": video_id,
                "author": snippet["authorDisplayName"],
                "comment_text": clean,  # <-- campo limpo aqui
                "like_count": snippet["likeCount"],
                "published_at": snippet["publishedAt"]
            })

        next_page_token = response_data.get("nextPageToken")
        if not next_page_token:
            break

    return comments

# Coletar todos os comentários
all_comments = []
for video_id in tqdm(video_ids, desc="Coletando comentários"):
    try:
        comments = get_comments(video_id, API_KEY)
        all_comments.extend(comments)
    except Exception as e:
        print(f"Erro ao coletar do vídeo {video_id}: {e}")

# Criar DataFrame
df_comments = pd.DataFrame(all_comments)

# Salvar CSV com todos os campos
df_comments.to_csv("TCC/Amostras/comentarios_crescendo_luluca.csv", index=False)
print("Comentários limpos salvos com sucesso!")
