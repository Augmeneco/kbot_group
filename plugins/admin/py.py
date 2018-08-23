import subprocess
if len(answ_text)==0:
	apisay('А текст мб стоит вписать?)',toho,torep)
else:
	cmd = ' '.join(answ_text)
	cmd = cmd.replace('»','	')
	cmd = cmd.split('<br>')
	with open('tmp/exec.py', 'w') as cl:
		for i in range(len(cmd)):
			cl.write(cmd[i]+'\n')
	shell = subprocess.getoutput('chmod 755 tmp/exec.py;python3 tmp/exec.py')
	apisay(shell,toho)
