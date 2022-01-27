#Practical python exercise, to understand if else elif
idade= int(input("How old are you:: "))

if idade < 12:
	print ("Kid")
elif idade < 18:
	print("Adolescent")
elif idade < 60:
	print ("Adult")
else:
	print ("Old man/woman")