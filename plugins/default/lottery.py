if len(augdb.read('system/users.db','balance','id="'+str(userid)+'"')) == 0:
	augdb.write('system/users.db','balance',[(userid,100)])
	apisay('Я заметила что вы первый раз воспользовались услугами кбкоинов. Для вас создан кошелёк  с балансом 100 кбкоинов',toho)
else:
	balance[userid] = augdb.read('system/users.db','balance','id='+str(userid))[0][1]
	if balance[userid] < 5:
		apisay('Я заметила что вы проебали все баблишка, поэтому даю тебе кредит в 5 кбкоинов.\nТеперь твой баланс составляет '+str(balance[userid]+5)+' кбкоинов',toho)
		augdb.replace('system/users.db','balance','id='+str(userid),'money='+str(balance[userid]+5))
	if answ_text[0].isdigit():
		if int(answ_text[0]) <= balance[userid]:
			if int(answ_text[0]) >= 5:
				if random.randint(0,100) > 50:
					balance[userid] += int(answ_text[0])
					apisay('Ты выиграл '+answ_text[0]+' кбкоинов!\nТеперь твой баланс составляет '+str(balance[userid])+' кбкоинов',toho)
					augdb.replace('system/users.db','balance','id='+str(userid),'money='+str(balance[userid]))
				else:
					balance[userid] -= int(answ_text[0])
					apisay('Лох, ты проебал '+answ_text[0]+' кбкоинов.\nТеперь твой баланс составляет '+str(balance[userid])+' кбкоинов',toho)
					augdb.replace('system/users.db','balance','id='+str(userid),'money='+str(balance[userid]))
			else:
				apisay('Нельзя юзать числа которые меньше чем 5 кбкоинов :(',toho)
		elif balance[userid] >= 5:
			apisay('У тебя нет столько денег, лол',toho)
	else:
		apisay('А параметр то не является числом, ты чо наебать меня хотел? ( ͡° ͜ʖ ͡°)',toho)