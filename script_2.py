from gensim.models import Word2Vec

# Sample sentences representing a corpus over time
sentences = [
    ['gene', 'discovery', 'in', 'the', 'early', '20th', 'century'],
    ['gene', 'regulation', 'mechanisms', 'identified', 'in', 'the', '1960s'],
    ['genetic', 'engineering', 'advances', 'in', 'the', '1990s'],
    ['gene', 'editing', 'with', 'CRISPR', 'technology', 'in', 'the', '2010s']
]

# Train a Word2Vec model
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

# Get vector for 'gene' at different times
gene_vector_20th_century = model.wv['gene']

# Find most similar words to 'gene'
similar_words = model.wv.most_similar('gene')
print(similar_words)
