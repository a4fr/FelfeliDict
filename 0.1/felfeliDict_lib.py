import gzip
import pickle
import time
import sys


def prepair_h8(db='h8.txt'):
	file = open(db, 'r')
	f_dict = {}
	for i in file:
		tmp = i[:-1].split('\t')
		key = tmp[0].strip()
		value = list(tmp[1])
		for i in range(len(value)):
			if value == '(':
				value = ')'
			elif value == ')':
				value = '('
	tmp = ''
	for i in value:
		tmp += i
	value = tmp
	f_dict[key] = value.replace('\\n', '<br/>').strip()
	file.close()
	return f_dict
	
def add_word_to_db(word, definition, db):
	if not(word in db):
		tmp = str(definition)
		db[word] = tmp
	return True

def edit_word_in_db(word, definition, db):
	if word in db:
		db[word] = str(definition)
	return True

def save_db_gzip(db):
	#Converting to bytes & Compressing f_dict
	f_dict_gzip = gzip.compress(pickle.dumps(db))
	file = open('f_dict_gzip', 'wb')
	file.write(f_dict_gzip)
	file.close()

def load_db(db='f_dict_gzip'):
        file = open(db, 'rb')
        if sys.platform == 'linux':
                f_dict = pickle.loads(gzip.decompress(file.read()))
        else:
                f_dict = pickle.loads(gzip.open(db).read())
        return f_dict

def search(keyword, db):
	result = {}
	for key in db:
		if keyword[-1] == '*':
			if key.startswith(keyword[:-1]):
				result[key] = db[key]
		elif keyword[0] == '*':
			if key.endswith(keyword[1:]):
				result[key] = db[key]
		elif keyword in key:
			result[key] = db[key]
	return result





