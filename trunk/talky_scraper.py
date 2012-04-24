import urllib2
# Scrapes Wiki response pages and generates captions
# MrMagoolachub

#options
lang = "" #need to include the / e.g. /es. Leave blank for english.
#/end options

startMedia = "Media:"
startQuote = "|"
endQuote = "]"
classes = ['Scout', 'Soldier', 'Pyro', 'Demoman', 'Heavy', 'Engineer', 'Medic', 'Sniper', 'Spy']
colors = ["<clr:52,90,124>", #scout
"<clr:198,91,75>", #soldier
"", #pyro
"<clr:147,163,164>", #demo
"<clr:205,87,64>", #heavy
"<clr:243,152,56>", #engy
"<clr:133,73,65>", #medic
"<clr:190,166,144>", #sniper
"<clr:98,133,155>"] #spy
count = 0
wereDoingResponses = True
pageType = "responses"
outputFile = "responses_scrape" + "_" + lang.replace("/", "") + ".txt"

outpoot = open(outputFile, "w")

while (count <= 8):
	url = "http://wiki.teamfortress.com/w/index.php?title=" + classes[count] + "_" + pageType + lang + "&action=edit"
	file = urllib2.urlopen(url)
	line = file.readline()
	outpoot.write("\n" + "\n" + classes[count] + " " + pageType + "\n" + "\n" + "\n")
	while (line != ""):
		line = file.readline()
		subtractor = 0
		if (line.find(".wav") != -1):
			line = line.replace("_", ".")
			if (line.find("|&lt;nowiki>") != -1):
				charToPrint = charToPrint - 1
			if (line.find("|&lt;nowiki>") != -1):
				subtractor = 1
			if (line.find("|\"") == -1 and line.find("|[") == -1):
				subtractor = 1
			if (line.find("nowiki") != -1):
				line = line.replace("&lt;nowiki>", "")
				line = line.replace("&lt;/nowiki>", "")
			charToPrint = line.find(startQuote) + 2 - subtractor
			charToEnd = line.rfind(endQuote) - 1
			mediaCounter = line.find(startMedia) + 6
			quote = ""
			media = ""
			while(mediaCounter < line.find(".wav")):
				media = media + line[mediaCounter]
				mediaCounter += 1
			while(charToPrint < charToEnd):
				if ("\'" != line[charToPrint]):
					quote = quote + line[charToPrint]
					charToPrint += 1
				else:
					counter = 0
					if (line[charToPrint - 1] != "\'" and line[charToPrint + 1] != "\'"):
						quote = quote + line[charToPrint]
						charToPrint += 1
					else:
						charToPrint += 1
			#print ("\t" + "\"" + media + "\"" + "\t" + "\"" + colors[count] + classes[count] + ": " + quote)
			quote = quote.replace("\"", "")
			outpoot.write("\t" + "\"" + media + "\"" + "\t" + "\"" + colors[count] + classes[count] + ": " + quote + "\"" + "\n")
	print (classes[count] + " " + pageType + " done!")
	count += 1
	if (wereDoingResponses == True):
		count = count -1
		pageType = "voice_commands"
		wereDoingResponses = False
	else:
		pageType = "responses"
		wereDoingResponses = True
	file.close()

print "all done!"
outpoot.close()