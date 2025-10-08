# PROJECT SCRAPING YOUTUBE COMMENT (VERSI LOKAL)

#Import library
from youtube_comment_downloader import YoutubeCommentDownloader
import pandas as pd
import re
import os

#Tentukan folder penyimpanan lokal
project_path = r"C:\Users\A S U S\OneDrive\Documents\TUGASSS\Scrappingdata"
os.makedirs(project_path, exist_ok=True)

print("✅ Folder project siap digunakan!")
print(f"📁 Lokasi penyimpanan: {project_path}")

#SCRAPING KOMENTAR YOUTUBE

#Gunakan link video kamu
video_url = "https://youtu.be/6VkezACZL24?si=52WNaDw7I8OywHvV"

# nisialisasi downloader
downloader = YoutubeCommentDownloader()

#Gunakan sort_by=0 → urutkan komentar dari yang paling atas
comments = downloader.get_comments_from_url(video_url, sort_by=0)

#Simpan hasil scraping ke list
data = []
for comment in comments:
    data.append({
        "user": comment["author"],
        "comment": comment["text"]
    })

#Ubah ke DataFrame
df = pd.DataFrame(data)

#Simpan hasil scraping ke CSV
scraping_file = os.path.join(project_path, "scraping.csv")
df.to_csv(scraping_file, index=False, encoding='utf-8-sig')

print(f"\n✅ File hasil scraping tersimpan di: {scraping_file}")
print(f"📄 Jumlah komentar yang diambil: {len(df)}")

#CASE FOLDING (Preprocessing)

#Baca file hasil scraping
df = pd.read_csv(scraping_file)

#Ubah semua huruf jadi kecil dan hilangkan tanda baca
df["clean_comment"] = df["comment"].str.lower()
df["clean_comment"] = df["clean_comment"].apply(
    lambda x: re.sub(r"[^a-zA-Z0-9\s]", "", str(x))
)

#Menyimpan hasil bersih ke file baru
casefold_file = os.path.join(project_path, "case_folding.csv")
df.to_csv(casefold_file, index=False, encoding='utf-8-sig')

print(f"✅ Hasil case folding tersimpan di: {casefold_file}")

#Tampilkan 5 komentar pertama
print("\n📝 Contoh hasil case folding:")
print(df.head())
