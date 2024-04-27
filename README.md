# Astrology-Bot: Fine-tuned LLaMA-2-7B for Horoscope Chat and Tarot Reading enhanced with RAG

# Motivation

Scientific testing has found no evidence to support the premises or purported effects outlined in astrological traditions. The continued belief in astrology despite its lack of credibility is seen as a demonstration of low scientific literacy, although some continue to believe in it even though they are scientifically literate. Let's make fun of it!.

![stargazing-cover-image](https://github.com/nogibjj/astrology-bot/assets/112578026/b01cce31-4680-4f1c-b7c3-0a5430f1a407)



# Repo Overview
```
Astrology-Bot/
│
├── data/                                 
│   ├── horoscope.csv 
│   ├── tarot.csv
│   ├── horoscope_webscraping.ipynb
│   └── tarot_webscraping.ipynb            
│
├── interface/                            
│   ├── get_response.py                   
│   ├── inference.py                      
│   └── UI.py                             
│
├── model/                                
│   ├── embedding_model.py                
│   └── inference_model.py               
│
└── RAG/
    ├── chunk_data.py                     
    ├── index_data.py                     
    ├── main.py                           
    └── utils.py                          


```
# Dataset

## Horoscope Reading

Scrape the plain text from Astrology.com with [Astrology.com](https://www.astrology.com/horoscope/daily.html) on daily basis. 

For each of the zodiac sign(`aries`, `taurus`, `gemini`, `cancer`, `leo`, `virgo`, `libra`, `scorpio`, `sagittarius`, `capricorn`, `aquarius`, `pisces`), I scraped `love`, `daily` and `work`.

## Tarot

Scrape the plain text of the meaning of each tarot card in different position from [biddytarot.com]([https://biddytarot.com/tarot-card-meanings/]). 

# Pipeline 
![pipeline](https://github.com/nogibjj/astrology-bot/assets/112578026/14580f20-4e4e-49b6-a437-a74b78d9517c)

1. **Chunking**: The cleaned text data is chunked through sliding window with 200 words as window size and 50 as sliding step size.
2. **Embed Text**: The text is embedded with BGE-Large model which is selected through [MTEB LeaderBoard](https://huggingface.co/spaces/mteb/leaderboard).
3. **Index Embedding**: The embeddings are indexed into [Pinecone](https://www.pinecone.io/). The retriver utilizes cosine similarity to retrieve relavant embeddings from the database.
4. **Prompting**: The query will be embedded with the same encoder. Then the retrieved text will be added into the prompt.
5. **Inference**: ``LLaMA-2-7B`` model is utilized to generate results. Due to the autoregressive nature, the generated text is post-processed and only the first answer is extracted as the final decision.

## Results
As shown in the results, the generated context information is more readable and makes more sense after fine-tuning and RAG implementation.
![1714098454821](https://github.com/nogibjj/astrology-bot/assets/112578026/86beb412-998f-4856-930f-8f12a9b112d6) ![IMG65](https://github.com/nogibjj/astrology-bot/assets/112578026/c97d3abe-db34-41f1-bbed-8ba633bfc1b5)


