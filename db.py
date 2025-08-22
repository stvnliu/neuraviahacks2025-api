import sqlite3

def init(path: str):
    conn = sqlite3.connect(path)
    init_tables = [
        
    ]