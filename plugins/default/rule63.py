import untangle
try:
	try:
		r34text = ' '.join(answ_text)
		r34text = r34text.replace(' ','+')
		blacklist = '-fur+-scat*+-darling_in_the_franxx+-furry+-dragon+-guro+-animal_penis+-animal+-wolf+-fox+-webm+-my_little_pony+-monster*+-3d+-animal*+-ant+-insects+-mammal+-horse+-blotch+-deer+-real*+-shit+-everlasting_summer+-copro*+-wtf+'
		parse = untangle.parse('http://rule63.xxx/index.php?page=dapi&s=post&q=index&limit=100&tags='+blacklist+str(r34text))
		randnum = random.randint(0,len(parse.posts.post))
		mess = 'Дрочевня подкатила<br>('+str(randnum)+'/'+str(len(parse.posts.post))+')<br>----------<br>Остальные теги: '+parse.posts.post[randnum]['tags']
		parse = parse.posts.post[randnum]['file_url']
		pic = requests.get(parse).content
		open('img/rule64/'+str(userid)+'.jpg','wb').write(pic)
		sendpic('img/rule64/'+str(userid)+'.jpg',mess,toho)
	except UnicodeEncodeError:
		apisay('Ничего не найдено :(',toho)
except AttributeError:
	apisay('Ничего не найдено :(',toho)
