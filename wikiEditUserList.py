import json
import requests
alias = raw_input("Name the wikipedia user:- ")
url = "https://en.wikipedia.org/w/api.php?action=query&format=json&list=usercontribs&ucuser=" + alias + "&ucdir=newer&uclimit=5&callback=?"

js = requests.get(url)
oldstr =  js.content
oldstr2 = oldstr.replace("/**/(", "")
newstr = oldstr2.replace("}]}})", "}]}}")

data  = json.loads(newstr)

array = data["query"]["usercontribs"]
for temp in array:
	print "User: " + temp["user"]
	print "Title: " + temp["title"]
	print "Timestamp: " + temp["timestamp"] + "\n"
   
