import sqlite3
import pandas as pd

def create_laws_table(conn: sqlite3.Connection) -> None:

    """Build database table"""

    conn.execute("""
    CREATE TABLE IF NOT EXISTS Drone_regulations (
        chunk_id INTEGER PRIMARY KEY,
        law_name TEXT,
        article_no TEXT,
        content TEXT,
        category TEXT
    )
    """)
    conn.commit()

def import_laws_from_excel(excel_path: str, db_path: str) -> None:

    """Import excel data into database"""

    df = pd.read_excel(excel_path)
    df = df.where(pd.notnull(df), None)

    conn = sqlite3.connect(db_path)

    try:
        #建立資料表，並刪除先前的資料
        create_laws_table(conn)
        conn.execute("DELETE FROM Drone_regulations")

        insert_sql = """
        INSERT INTO Drone_regulations (chunk_id, law_name, article_no, content, category)
        VALUES (?, ?, ?, ?, ?)
        """
        #資料丟進資料表
        conn.executemany(
            insert_sql,
            df.itertuples(index=False, name=None)
        )
        conn.commit()
    finally:
        conn.close()