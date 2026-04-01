import pandas as pd

df = pd.read_csv("dataset_generate.csv")
print(df.head())  # vezi structura
print("Număr total poezii:", len(df))

# Distributoe poezii per autor
import matplotlib.pyplot as plt


# Similaritate intre poezii random:
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import seaborn as sns

sample_texts = df["text"].sample(20, random_state=42)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(sample_texts)
sim_matrix = cosine_similarity(X)

plt.figure(figsize=(8, 6))
sns.heatmap(sim_matrix, cmap="viridis")
#plt.title("Similaritate între poezii (TF-IDF cosine)")
plt.show()