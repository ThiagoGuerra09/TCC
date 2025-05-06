# TCC Thiago Guerra Werkhaizer Felipe

# Análise de Comentários de grandes influenciadores no YouTube para Identificação de Cyberbullying

Este projeto visa realizar uma análise de dados nos comentários de vídeos do YouTube do Enaldinho, com o objetivo de identificar potenciais casos de cyberbullying. Utilizando a API do YouTube, os comentários são extraídos e armazenados para posterior análise.

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação utilizada para o desenvolvimento do projeto.
- **Google API Client**: Biblioteca para interação com a API do YouTube, utilizada para coletar os comentários.
- **Pandas**: Biblioteca de manipulação de dados para armazenar e processar os comentários extraídos.
- **tqdm**: Biblioteca para exibição de barras de progresso durante a coleta dos dados.

## Pré-requisitos

Antes de rodar o código, é necessário:
1. Ter uma chave de API do YouTube, que pode ser obtida [aqui](https://console.developers.google.com/).
2. Instalar as bibliotecas necessárias utilizando o comando:

   ```bash
   pip install google-api-python-client pandas tqdm


## Videos usados nas amostras

## comentarios_resendeevil.csv
      "CaWh022KuX4",
      "m5UpGISwdVk",
      "7roRz1T_5qY",
      "puplAelQdKs",
      "nTcRHtcaE10",
      "CaWh022KuX4",
      "m5UpGISwdVk",
      "7roRz1T_5qY",
      "puplAelQdKs",
      "9TbzIKWtvOc", 
      "s_OMCz5MXnU", 
      "Pp6FwS8iFms",
        "o_MhqpL0DVQ",
          "DJNZza61z1U",
            "Kjp3pXMZfF8",
              "SZqT-ctRSec",
                "NDCkMcNJFt0",
                  "bKY_IGIBMQY",
                    "_sHMAG-eKg8",
                    "v=tTHWSgzM8yc"
## comentarios_camila_loures.csv
      "Bykdn5SrtM0",
      "5uSPSVNEQ6s",
      "TYWrS9lbHVo",
      "m3GpdXFufU4",
      "gRO4G1Gpf0s",
      "ounRlEoxIb8", "VZNqfLWxvcQ", "DkbsuIPgrtc", "Ofv8NhlIN-A", "B7uM4y301uU", "WsmGpNduvNY", "ORSQrg93eFg", "NT6bCf-r9JY", "C8vI-nO7s6s", "9TbzIKWtvOc"

## comentarios_enaldinho.csv
     "mrKRmApg3I0", "h7hzx8RzzJM", "BOQW2fVqHRI", "ZqoH8AjRMvc", "9UiHhvvZ7VI", "VlPLOEmycbw", "gAX7mW3KFTQ", "ZzOXtngrGeM", "UEYmhlOE3i0",
      "aMF3dfR6Yc4",
    "2eu6efo-gBs",
    "x--vfRhaP0Q",
    "NaQJYavi0kI",
    "sM42cxbM9Ao",
    "v=2byAsju7UD0"

   

## Palavras ofensivas no filtro

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
