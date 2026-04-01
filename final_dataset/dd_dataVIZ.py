import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Incarcare dataset
df = pd.read_csv("dataset_generate.csv")

# === GRAFIC 1: Distributia poeziilor pe autori ===
author_counts = df['autor'].value_counts()

plt.figure(figsize=(10,6))
sns.barplot(x=author_counts.index, y=author_counts.values)
#plt.title("Distributia poeziilor pe autori")
plt.xlabel("Author")
plt.ylabel("Number of poems")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("poezii_pe_autori.png")
plt.close()

# === GRAFIC 2: Lungimea medie a poeziei per autor ===
df['lungime'] = df['text'].str.len()  # adauga o coloana noua cu lungimea poeziei (caractere)

avg_length = df.groupby('autor')['lungime'].mean().sort_values(ascending=False)

plt.figure(figsize=(10,6))
sns.barplot(x=avg_length.index, y=avg_length.values)
#plt.title("Medium poem length per author")
plt.xlabel("Author")
plt.ylabel("Medium length (characters)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("lungime_medie_autori.png")
plt.close()

# === GRAFIC 3: Distributia lungimii poeziilor (histograma) ===
plt.figure(figsize=(8,6))
sns.histplot(df['lungime'], bins=20, kde=True)
#plt.title("Distribu lungimii poeziilor")
plt.xlabel("Number of characters per poem")
plt.ylabel("Number of poems")
plt.tight_layout()
plt.savefig("distributie_lungime_poezii.png")
plt.close()
