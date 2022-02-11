import sqlite3

TEMPLATE_PATH = 'templates'
CONNECTION = sqlite3.connect('database.sqlite', check_same_thread=False)
