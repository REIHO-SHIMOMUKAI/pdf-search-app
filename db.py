import sqlite3

DB_NAME = "app.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS pdfs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            content TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_pdf(filename, content):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO pdfs (filename, content) VALUES (?, ?)",
        (filename, content)
    )

    conn.commit()
    conn.close()


def search_pdf(keyword):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    if keyword:
        cur.execute(
            "SELECT id, filename FROM pdfs WHERE content LIKE ?",
            ('%' + keyword + '%',)
        )
    else:
        cur.execute("SELECT id, filename FROM pdfs")

    rows = cur.fetchall()
    conn.close()
    return rows


def view_pdf(id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT filename, content FROM pdfs WHERE id = ?", (id,))
    row = cur.fetchone()

    conn.close()
    return row


def delete_pdf(id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("DELETE FROM pdfs WHERE id = ?", (id,))

    conn.commit()
    conn.close()