if len(answ_text)==0:
	apisay('А текст мб стоит вписать?)',toho,torep)
else:
	cmd = ' '.join(answ_text).split('<br>')
	with open('tmp/eval.py', 'w') as cl:
		for i in range(len(cmd)):
			cl.write(cmd[i]+'\n')
		exec(open('tmp/eval.py','r').read())