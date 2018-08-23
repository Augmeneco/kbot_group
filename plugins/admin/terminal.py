import subprocess
if len(answ_text)==0:
	apisay('А текст мб стоит вписать?)',toho,torep)
else:
	cmd = ' '.join(answ_text).split('<br>')
	with open('tmp/cmd.sh', 'w') as cl:
		for i in range(len(cmd)):
			cl.write(cmd[i]+'\n')
	shell = subprocess.getoutput('chmod 755 tmp/cmd.sh;bash tmp/cmd.sh')
	apisay(shell,toho)