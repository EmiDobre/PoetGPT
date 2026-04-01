import pandas as pd

# 📄 Fișierele din directorul curent
csv_files = [
    "ana_blandiana.csv", "arghezi.csv", "bacovia.csv",
    "blaga.csv", "eminescu.csv", "sorescu.csv"
]

# 📦 Concatenare
dfs = []
for file in csv_files:
    df = pd.read_csv(file)
    dfs.append(df)

# 🧩 Unim toate fișierele într-unul singur
df_final = pd.concat(dfs, ignore_index=True)

# 💾 Salvăm ca dataset_generate.csv în directorul curent
df_final.to_csv("dataset_generate.csv", index=False)

print("✅ Combinarea completă a fost salvată în dataset_generate.csv.")
