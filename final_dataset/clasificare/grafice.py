import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Încarcă datasetul final pentru clasificare
df = pd.read_csv("dataset_clasificare_train.csv", encoding="utf-8")

# === GRAFIC 1: Distribuția strofelor pe autori ===
stanza_counts = df['autor'].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=stanza_counts.index, y=stanza_counts.values)
#plt.xlabel("Author")
#plt.ylabel("Number of stanzas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("stanzas_per_author.png")
plt.close()

# === GRAFIC 2: Lungimea medie a strofelor per autor (în caractere) ===
df['lungime'] = df['text'].astype(str).str.len()
avg_length = df.groupby('autor')['lungime'].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=avg_length.index, y=avg_length.values)
#plt.xlabel("Author")
#plt.ylabel("Average stanza length (characters)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("avg_stanza_length.png")
plt.close()
