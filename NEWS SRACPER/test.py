from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

tokenized_news = [tokenizer(news, padding="max_length", truncation=True, return_tensors="pt") for news in news_headlines]
