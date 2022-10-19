# python3 auto1.py

import os
import openai

import subprocess
import sys

import datetime


iroop_0=25
iroop_1=125
iroop_2=650
iroop_3=1375


prompt_alf=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ialf=len(prompt_alf)

prompt_col=["red","blue","green","yellow","orange","purple","pink","brown","white","black","gray"]
icol=len(prompt_col)

zmodel="davinci"

ztemperature=0.7
zprompt0="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: " 
zprompt3=".\nAI:"

zprompt1=["Please give a color name that you will associate with a letter "]#0_alf
zprompt1.append("Please give an alphabet character that you will associate with color ")#1_col
zprompt1.append("Please name one color")#2
zprompt1.append("Please name one alphabet character")#3

path0="myfile"
path1=path0+".txt"

openai.api_key = "YOUR_ACCOUNT_API_KEY"


######################### 0
for i in range(ialf):
	zprompt2A="'"+prompt_alf[i]+"'"
	xprompt=zprompt0+zprompt1[0]+zprompt2A+zprompt3
	
	txt='\n' +'\n' +'##################################' + '\n'
	txt=txt+'PROMPT= ' + '\n'+ xprompt + '\n' + '\n'
	txt=txt+'MODEL= ' + zmodel + '\n'
	txt=txt+'TEMPERATURE= ' + str(ztemperature) + '\n'
	txt=txt+'##################################' + '\n' + '\n'

	f = open(path1, 'a', encoding='UTF-8')
	f.write(txt + '\n')
	f.close()

	start_sequence = "\nAI:"
	restart_sequence = "\nHuman: "

	for i in range(iroop_0):
		response = openai.Completion.create(
		  model=zmodel,
		  prompt=xprompt,
		  temperature=ztemperature,
		  max_tokens=150,
		  top_p=1,
		  frequency_penalty=0,
		  presence_penalty=0.6,
		  stop=["\n", " Human:", " AI:"]
		)

		txt=str(response['choices'][0]['text'])
		print(txt)

		f = open(path1, 'a', encoding='UTF-8')
		f.write(txt + '\n')
		f.close()

dt_now = datetime.datetime.now()
txt_date=str(dt_now.year)+"_"+str(dt_now.month)+"_"+str(dt_now.day)+"_"+str(dt_now.hour)+"_"+str(dt_now.minute)+"_"+str(dt_now.second)

path2=path0+"_txt1_"+txt_date+".txt"

res = subprocess.run(["cp", path1, path2], stdout=subprocess.PIPE)
sys.stdout.buffer.write(res.stdout)	

res = subprocess.run(["rm", path1], stdout=subprocess.PIPE)
sys.stdout.buffer.write(res.stdout)	


######################### 1
for i in range(icol):
	zprompt2C="'"+prompt_col[i]+"'"
	xprompt=zprompt0+zprompt1[1]+zprompt2C+zprompt3
	
	txt='\n' +'\n' +'##################################' + '\n'
	txt=txt+'PROMPT= ' + '\n'+ xprompt + '\n' + '\n'
	txt=txt+'MODEL= ' + zmodel + '\n'
	txt=txt+'TEMPERATURE= ' + str(ztemperature) + '\n'
	txt=txt+'##################################' + '\n' + '\n'

	f = open(path1, 'a', encoding='UTF-8')
	f.write(txt + '\n')
	f.close()

	start_sequence = "\nAI:"
	restart_sequence = "\nHuman: "

	for i in range(iroop_1):
		response = openai.Completion.create(
		  model=zmodel,
		  prompt=xprompt,
		  temperature=ztemperature,
		  max_tokens=150,
		  top_p=1,
		  frequency_penalty=0,
		  presence_penalty=0.6,
		  stop=["\n", " Human:", " AI:"]
		)

		txt=str(response['choices'][0]['text'])
		print(txt)

		f = open(path1, 'a', encoding='UTF-8')
		f.write(txt + '\n')
		f.close()

dt_now = datetime.datetime.now()
txt_date=str(dt_now.year)+"_"+str(dt_now.month)+"_"+str(dt_now.day)+"_"+str(dt_now.hour)+"_"+str(dt_now.minute)+"_"+str(dt_now.second)

path2=path0+"_txt2_"+txt_date+".txt"

res = subprocess.run(["cp", path1, path2], stdout=subprocess.PIPE)
sys.stdout.buffer.write(res.stdout)	

res = subprocess.run(["rm", path1], stdout=subprocess.PIPE)
sys.stdout.buffer.write(res.stdout)	



######################### 2
xprompt=zprompt0+zprompt1[2]+zprompt3

txt='\n' +'\n' +'##################################' + '\n'
txt=txt+'PROMPT= ' + '\n'+ xprompt + '\n' + '\n'
txt=txt+'MODEL= ' + zmodel + '\n'
txt=txt+'TEMPERATURE= ' + str(ztemperature) + '\n'
txt=txt+'##################################' + '\n' + '\n'

f = open(path1, 'a', encoding='UTF-8')
f.write(txt + '\n')
f.close()

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

for i in range(iroop_2):
	response = openai.Completion.create(
	  model=zmodel,
	  prompt=xprompt,
	  temperature=ztemperature,
	  max_tokens=150,
	  top_p=1,
	  frequency_penalty=0,
	  presence_penalty=0.6,
	  stop=["\n", " Human:", " AI:"]
	)

	txt=str(response['choices'][0]['text'])
	print(txt)

	f = open(path1, 'a', encoding='UTF-8')
	f.write(txt + '\n')
	f.close()

dt_now = datetime.datetime.now()
txt_date=str(dt_now.year)+"_"+str(dt_now.month)+"_"+str(dt_now.day)+"_"+str(dt_now.hour)+"_"+str(dt_now.minute)+"_"+str(dt_now.second)

path2=path0+"_txt3_"+txt_date+".txt"

res = subprocess.run(["cp", path1, path2], stdout=subprocess.PIPE)
sys.stdout.buffer.write(res.stdout)	

res = subprocess.run(["rm", path1], stdout=subprocess.PIPE)
sys.stdout.buffer.write(res.stdout)	



######################### 3
xprompt=zprompt0+zprompt1[3]+zprompt3

txt='\n' +'\n' +'##################################' + '\n'
txt=txt+'PROMPT= ' + '\n'+ xprompt + '\n' + '\n'
txt=txt+'MODEL= ' + zmodel + '\n'
txt=txt+'TEMPERATURE= ' + str(ztemperature) + '\n'
txt=txt+'##################################' + '\n' + '\n'

f = open(path1, 'a', encoding='UTF-8')
f.write(txt + '\n')
f.close()

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

for i in range(iroop_3):
	response = openai.Completion.create(
	  model=zmodel,
	  prompt=xprompt,
	  temperature=ztemperature,
	  max_tokens=150,
	  top_p=1,
	  frequency_penalty=0,
	  presence_penalty=0.6,
	  stop=["\n", " Human:", " AI:"]
	)

	txt=str(response['choices'][0]['text'])
	print(txt)

	f = open(path1, 'a', encoding='UTF-8')
	f.write(txt + '\n')
	f.close()

dt_now = datetime.datetime.now()
txt_date=str(dt_now.year)+"_"+str(dt_now.month)+"_"+str(dt_now.day)+"_"+str(dt_now.hour)+"_"+str(dt_now.minute)+"_"+str(dt_now.second)

path2=path0+"_txt4_"+txt_date+".txt"

res = subprocess.run(["cp", path1, path2], stdout=subprocess.PIPE)
sys.stdout.buffer.write(res.stdout)	

res = subprocess.run(["rm", path1], stdout=subprocess.PIPE)
sys.stdout.buffer.write(res.stdout)	

