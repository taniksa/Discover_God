from gensim.models import Word2Vec

# Sample sentences
sentences = [
    ['the', 'cat', 'sat', 'on', 'the', 'mat'],
    ['the', 'dog', 'sat', 'on', 'the', 'log'],
    ['the', 'cat', 'chased', 'the', 'mouse'],
    ['the', 'dog', 'barked', 'at', 'the', 'mailman']
]

# Train a Word2Vec model
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

# Get vector for 'cat'
cat_vector = model.wv['cat']

# Find most similar words to 'cat'
similar_words = model.wv.most_similar('cat')
print(similar_words)
