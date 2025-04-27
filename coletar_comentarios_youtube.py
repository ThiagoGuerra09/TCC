import requests
import pandas as pd
from tqdm import tqdm

# Sua chave de API do YouTube Data
API_KEY = ""

# IDs ou URLs dos vídeos de desafio do Enaldinho
video_ids = [
    "CaWh022KuX4",
   "m5UpGISwdVk",
   "7roRz1T_5qY",
   "puplAelQdKs",
   "nTcRHtcaE10"
]

# Função para extrair comentários de um vídeo
def get_comments(video_id, api_key):
    comments = []
    next_page_token = None

    while True:
        url = f"https://www.googleapis.com/youtube/v3/commentThreads"
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
            comment = item["snippet"]["topLevelComment"]["snippet"]
            comments.append({
                "video_id": video_id,
                "author": comment["authorDisplayName"],
                "comment_text": comment["textDisplay"],
                "like_count": comment["likeCount"],
                "published_at": comment["publishedAt"]
            })

        next_page_token = response_data.get("nextPageToken")
        if not next_page_token:
            break

    return comments

# Coletar comentários de todos os vídeos
all_comments = []
for video_id in tqdm(video_ids, desc="Coletando comentários"):
    try:
        comments = get_comments(video_id, API_KEY)
        all_comments.extend(comments)
    except Exception as e:
        print(f"Erro ao coletar comentários do vídeo {video_id}: {e}")

# Converter para DataFrame
df_comments = pd.DataFrame(all_comments)

# Salvar em CSV
df_comments.to_csv("TCC/Amostras/comentarios_resendeevil.csv", index=False)
print("Comentários salvos")
