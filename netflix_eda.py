import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




df = pd.read_csv(r"netflix_titles.csv")
print(df.head())
print(df.info())

type_counts = df['type'].value_counts()
print("\nTür sayıları: ")
print(type_counts)
print(f"\nInsight: Netflix'te toplam {type_counts.get('Movie',0)} film ve {type_counts.get('TV Show',0)} dizi var.")

country_counts = df['country'].value_counts(10)
print("\nEn çok içerik üreten ülkeler: ")
print(country_counts)
top_countries = df['country'].value_counts().head(10)
print(f"\nInsight: En çok içerik üreten ülke {top_countries.index[0]} ve ikinci {top_countries.index[1]}.")

year_counts = df['release_year'].value_counts().sort_index()
print("\nYıllara göre içerik sayısı: ")
print(year_counts)
peak_year = year_counts.idxmax()
print(f"\nInsight: En çok içerik {peak_year} yılında yayınlanmış.")


plt.figure(figsize=(10,6))
sns.countplot(data=df, x='type',palette='Set2')
plt.title("Film ve Dizi Sayısı")
plt.xlabel("Tür")
plt.ylabel("Adet")   
plt.tight_layout()
plt.savefig("imagess/type_count.png")   
plt.show()


plt.figure(figsize=(12,6))
df['release_year'].value_counts().sort_index().plot(kind='bar',color='teal')
plt.title("Yıllara Göre İçerik Sayısı")
plt.xlabel("Yıl")
plt.ylabel("Adet")
plt.tight_layout()
plt.savefig("imagess/yearly_count.png")
plt.show()

top_countries = df['country'].value_counts().head(10)
plt.figure(figsize=(12,7))
sns.barplot(x=top_countries.values, y= top_countries.index,palette='magma')
plt.title("En Çok İçerik Üreten 10 Ülke")
plt.xlabel("İçerik Sayısı")
plt.ylabel("Ülke")
plt.tight_layout()
plt.savefig("imagess/top_countries.png")
plt.show()

