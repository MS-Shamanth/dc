import gensim
from gensim.models import Word2Vec
import nltk
from nltk.tokenize import word_tokenize
import numpy as np

nltk.download('punkt')
nltk.download('punkt_tab')

corpus = [
    "Natural language processing is a fascinating field.",
    "Word embeddings are a type of word representation.",
    "They allow words to be represented in a continuous vector space.",
    "Word2Vec is one of the most popular algorithms for generating word embeddings.",
    "Neural networks can be used to learn these embeddings."
]

tokenized_corpus = [word_tokenize(sentence.lower()) for sentence in corpus]

model = Word2Vec(
    sentences=tokenized_corpus,
    vector_size=100,
    window=5,
    min_count=1,
    workers=4
)

model.save("word2vec.model")

word = "word"
embedding = model.wv[word]

print(f"Embedding for '{word}':")
print(embedding)

similar_words = model.wv.most_similar("word", topn=5)

print("\nMost similar words to 'word':")

for similar_word, similarity in similar_words:
    print(f"{similar_word}: {similarity:.4f}")

words = ["natural", "language", "processing"]

embeddings = np.array([model.wv[word] for word in words])

print("\nEmbeddings for words:")

for word, embedding in zip(words, embeddings):
    print(f"{word}: {embedding}")
