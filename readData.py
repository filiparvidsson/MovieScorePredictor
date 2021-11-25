import pandas as pd

cols = ["tconst", "averageRating"]
titleAndRating = pd.read_csv('title.ratings.tsv', delimiter='\t', usecols=cols)

cols = ["tconst", "titleType", "primaryTitle"]
titleTypeAndName = pd.read_csv('title.ratings.tsv', delimiter='\t', usecols=cols)

#ratings = pd.read_csv('title.ratings.tsv', delimiter='\t', index_col="tconst")
print(title) 
