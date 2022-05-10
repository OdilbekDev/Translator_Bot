import sqlite3

#bu kod vazifasi userni tanlagan tilini bazaga saqlab qolish
#bazada user id lar ham saqlanadi agar stat send funksiyalarini qoʻshmoqchi boʻlsangiz iloji bor!

db = sqlite3.connect("userlanguages.db")
dbc = db.cursor()
dbc.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    chat_lang
)""")
db.commit()
