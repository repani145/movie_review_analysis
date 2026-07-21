import gensim.downloader as api

print("Downloading GloVe...")

glove = api.load("glove-wiki-gigaword-100")

print("Saving...")

glove.save("models/glove.kv")

print("Done!")