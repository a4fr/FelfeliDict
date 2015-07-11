#! python3

from bottle import Bottle, run, app, template, route, get, post, request, static_file
import felfeliDict_lib as felfeliDict
import time
import os


app = '/dict'

#Dictionary DataBase	
start = time.time()
f_dict = felfeliDict.load_db()
print('* DataBase loaded in', format(time.time()-start, '.2f'))


###############################################################################
@route('/static/<filename>')
def server_static(filename):
	return static_file(filename, root='template/')

@route('/static/img/<filename>')
def server_static(filename):
	return static_file(filename, root='template/img')
	
	
###############################################################################
def split_words(words_str):
	if words_str=='':
		return []
	word_tmp = words_str.split('-')
	words = []
	for i in word_tmp:
		if i.strip() != '':
			words.append(i.strip())
	return words

def translate(words):
	result = []
	
	#store with order of words
	for word in words:
		for item in felfeliDict.search(word, f_dict).items():
			result.append(item)
			
	#show definition of last word in first
	result.reverse()
	return result

###############################################################################
@get(app)
def form():
	output = {}
	return template('template/doc', words=output, text='')
	
@route(app+'/help')
def help():
	return template('template/help')

@post(app)
def from_post():
	words_from_get = request.forms.get('words')
	output = translate(split_words(words_from_get))
	return template('template/doc', words=output, text=words_from_get)

@route(app+'/<path>')
def translate_url(path):
	output = translate(split_words(path))
	return template('template/doc', words=output, text=path)


###############################################################################
port = 2020
host = 'localhost'
run(host=host, port=port, debug=True, reloader=True)

#os.system('gnome-open http://{host}:{port}{app}'.format(host=host, port=port, app=app))


