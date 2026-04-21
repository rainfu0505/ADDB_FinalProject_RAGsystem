import pandas as pd
from sentence_transformers import SentenceTransformer
import json

# 讀取 chunk 資料
INPUT_FILE = "D:\\Python\\02_NTUT_Course\\Advanced_Database_System\\Final_Project_RAGsystem\\Text_Chunking\\chunks.xlsx"
OUTPUT_FILE = "D:\\Python\\02_NTUT_Course\\Advanced_Database_System\\Final_Project_RAGsystem\\Embedding\\chunks_with_embeddings.xlsx"

df = pd.read_excel(INPUT_FILE)

# 載入 embedding 模型
model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

# 對 content 做向量化
print("開始進行知識向量化...")
embeddings = model.encode(df["content"].tolist())

# 將向量轉成可存檔格式（JSON）
df["embedding"] = [json.dumps(vec.tolist()) for vec in embeddings]

# 存回 Excel
df.to_excel(OUTPUT_FILE, index=False)
print(f"✅ 向量化完成，已儲存至 {OUTPUT_FILE}")