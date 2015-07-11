from felfeliDict_lib import *

db = load_db()
print(edit_word_in_db('word', 'یک دیکشنری خیلی ساده و باحال برای گیک ها<br/>اولین نسخه آن در آبان ۹۳، توسط <b>علی نجفی</b> توسعه داده شد', db))
save_db_gzip(db)
