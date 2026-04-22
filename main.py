from DB_build import import_laws_from_excel

def main():
    excel_path = 'D:\\Python\\02_NTUT_Course\\Advanced_Database_System\\Final_Project_RAGsystem\\Text_Chunking\\chunks.xlsx'
    db_path = 'D:\\Python\\02_NTUT_Course\\Advanced_Database_System\\Final_Project_RAGsystem\\Database\\drone_regulations.db'
    import_laws_from_excel(excel_path, db_path)
    print("資料匯入完成")


if __name__ == "__main__":
    main()