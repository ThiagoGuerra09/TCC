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

