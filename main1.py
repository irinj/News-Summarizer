import tkinter as tk
from textblob import TextBlob
from newspaper import Article
import nltk
import logging

# Download the necessary NLTK data for Newspaper3k
nltk.download('punkt')

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def summarize():
    url = utext.get('1.0', "end").strip()
    logging.info(f"URL: {url}")
    
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        
        title.config(state='normal')
        author.config(state='normal')
        publication.config(state='normal')
        summary.config(state='normal')
        sentiment.config(state='normal')
        
        title.delete('1.0', "end")
        title.insert('1.0', article.title if article.title else "N/A")
        
        author.delete('1.0', "end")
        author.insert('1.0', ', '.join(article.authors) if article.authors else "N/A")
        
        publication_date = article.publish_date if article.publish_date else "N/A"
        if publication_date != "N/A":
            publication_date = publication_date.strftime('%Y-%m-%d')
        publication.delete('1.0', "end")
        publication.insert('1.0', publication_date)
        
        summary.delete('1.0', "end")
        summary.insert('1.0', article.summary if article.summary else "Summary not available.")
        
        analysis = TextBlob(article.text)
        sentiment.delete('1.0', "end")
        sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')
        
        title.config(state='disabled')
        author.config(state='disabled')
        publication.config(state='disabled')
        summary.config(state='disabled')
        sentiment.config(state='disabled')
    
    except Exception as e:
        logging.error(f"Error: {e}")
        title.config(state='normal')
        author.config(state='normal')
        publication.config(state='normal')
        summary.config(state='normal')
        sentiment.config(state='normal')
        
        title.delete('1.0', "end")
        author.delete('1.0', "end")
        publication.delete('1.0', "end")
        summary.delete('1.0', "end")
        sentiment.delete('1.0', "end")
        
        title.insert('1.0', "Error")
        author.insert('1.0', "Error")
        publication.insert('1.0', "Error")
        summary.insert('1.0', "Could not retrieve article. Please check the URL and try again.")
        sentiment.insert('1.0', "Error")
        
        title.config(state='disabled')
        author.config(state='disabled')
        publication.config(state='disabled')
        summary.config(state='disabled')
        sentiment.config(state='disabled')

root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')

tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

plabel = tk.Label(root, text="Publication Date")
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

selabel = tk.Label(root, text="Sentiment Analysis")
selabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

ulabel = tk.Label(root, text="URL")
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

root.mainloop()
