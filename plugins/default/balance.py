if len(augdb.read('system/users.db','balance','id="'+str(userid)+'"')) == 0:
	augdb.write('system/users.db','balance',[(userid,100)])
	apisay('Я заметила что вы первый раз воспользовались услугами кбкоинов. Для вас создан кошелёк  с балансом 100 кбкоинов',toho)
else:
	balance = augdb.read('system/users.db','balance','id='+str(userid))[0][1]
	apisay('Ваш баланс составляет '+str(balance)+' кбкоинов',toho)