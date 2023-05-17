"""
The database handler for the program
"""
import sqlite3

conn = sqlite3.connect("./database/wishlist.db")

# Create tables if they don't exist
conn.execute("""
CREATE TABLE IF NOT EXISTS last_price (
    URL TEXT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    PRICE_SYMBOL CHAR(1) NOT NULL,
    PRICE INT NOT NULL
)
""")