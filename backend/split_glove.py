import gensim.downloader as api
from gensim.models import KeyedVectors
import math

print("Loading original GloVe model...")
glove = api.load("glove-wiki-gigaword-100")

all_words = glove.index_to_key

print(f"Total words : {len(all_words)}")

num_parts = 4

chunk_size = math.ceil(len(all_words) / num_parts)

for part in range(num_parts):

    start = part * chunk_size
    end = min(start + chunk_size, len(all_words))

    words = all_words[start:end]

    kv = KeyedVectors(vector_size=100)

    vectors = [glove[word] for word in words]

    kv.add_vectors(words, vectors)

    filename = f"models/glove_part{part+1}.kv"

    kv.save(filename)

    print(f"Saved {filename}")
    print(f"Words : {len(words)}")

print("\nFinished Successfully!")