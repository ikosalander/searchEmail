import requests
import time

prenom = "test"
nom = "test"


declinaison = []

resultat = prenom[0] + nom
declinaison.append(resultat)
resultat = prenom[0] + "." + nom
declinaison.append(resultat)
resultat = prenom + nom
declinaison.append(resultat)
resultat = prenom + "." + nom
declinaison.append(resultat)
resultat = prenom + "_" + nom
declinaison.append(resultat)

#optional rules
region = "region"
yearOfBirth = "yearOfBirth"
pseudo = "pseudo"
cp = "cp"

resultat = prenom + nom + region
declinaison.append(resultat)

resultat = prenom + region
declinaison.append(resultat)

resultat = pseudo + region
declinaison.append(resultat)

resultat = pseudo + cp
declinaison.append(resultat)


resultat = prenom + cp
declinaison.append(resultat)


resultat = pseudo + nom + cp
declinaison.append(resultat)

mail = [
'@gmail.com',
'@hotmail.com',
'@hotmail.fr',
'@yahoo.fr',	
'@yahoo.com',
'@laposte.net',
'@live.fr',
'@live.com',
'@msn.com',
'@msn.fr',
'@outlook.fr',
'@outlook.com'
]

result = []
i= 0
j = 0

while i < len(declinaison):
	while j < len(mail):
		rslt = declinaison[i] + mail[j]
		result.append(rslt)
		j += 1
	j = 0
	i += 1

# print result

urls = []
x = 0

while x < len(result):
	url = "https://haveibeenpwned.com/api/v2/breachedaccount/" + result[x]
	urls.append(url)
	x += 1


# print urls
z = 0
leakPerf = 0
totalTry = 0

while z < len(urls):
	# print urls[z]
	r = requests.get(urls[z])
	# r = requests.get("https://haveibeenpwned.com/api/v2/breachedaccount/pierreyves59@gmail.com")
	res = r.content
	# print res
	if "Title" in res:
		print urls[z] + " : is pwnd"
		leakPerf += 1
	# else:
	# 	print urls[z] + " not enough"
	z += 1 
	totalTry +=1
	time.sleep(1)

print "Perform : " + str(leakPerf) + " sur " + str(totalTry)