import pandas as pd
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
EXCEL_FILE = "D:\\Python\\02_NTUT_Course\\Advanced_Database_System\\Final_Project_RAGsystem\\Text_Chunking\\chunks.xlsx"

COLUMNS = [
    "chunk_id",
    "law_name",
    "article_no",
    "content",
    "category"
]


def load_or_create_dataframe():
    if os.path.exists(EXCEL_FILE):
        return pd.read_excel(EXCEL_FILE)
    else:
        return pd.DataFrame(columns=COLUMNS)


def save_to_excel(df):
    df.to_excel(EXCEL_FILE, index=False)
    print(f"✅ 已成功儲存到 {EXCEL_FILE}\n")


def input_chunk():
    print("請輸入一筆新的 chunk（直接 Enter 結束）")

    chunk_id = input("Chunk ID：").strip()
    if chunk_id == "":
        return None

    #law_name = input("法規名稱 (law_name)：").strip()
    law_name = "遙控無人機管理規則"
    article_no = input("條文編號 (article_no)：").strip()

    print("條文全文 (content)：（輸入完成後按 Enter）")
    content = input().strip()

    category = input("主題標籤 (category，可留空)：").strip()

    return {
        "chunk_id": chunk_id,
        "law_name": law_name,
        "article_no": article_no,
        "content": content,
        "category": category
    }


def main():
    print("=== 無人機法規 Chunk 輸入工具 ===\n")

    df = load_or_create_dataframe()

    while True:
        chunk = input_chunk()
        if chunk is None:
            print("輸入結束。")
            break

        df = pd.concat([df, pd.DataFrame([chunk])], ignore_index=True)
        save_to_excel(df)


if __name__ == "__main__":
    main()