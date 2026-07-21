from gensim.models import KeyedVectors


def load_glove():

    print("Loading Part 1...")
    glove = KeyedVectors.load("models/glove_part1.kv")

    for i in range(2, 5):

        print(f"Loading Part {i}...")

        part = KeyedVectors.load(f"models/glove_part{i}.kv")

        glove.add_vectors(
            part.index_to_key,
            part.vectors
        )

    print("Merged Successfully!")

    return glove