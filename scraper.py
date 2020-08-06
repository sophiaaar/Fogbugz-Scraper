from fogbugz import FogBugz
import csv
import sys
from collections import Counter

# Fill in the following values as appropriate to your installation
S_FOGBUGZ_URL   = 'https://fogbugz.unity3d.com'
TOKEN			= ""
S_EMAIL         = ''
S_PASSWORD      = ''

fb = FogBugz(S_FOGBUGZ_URL, TOKEN)

resp = fb.search(q='area:"Universal RP"',cols="fOpen,sTitle")

wordlist = ['universal', 'cases']

for case in resp.cases.childGenerator():

	if case.fOpen.string != None:
		openBool = case.fOpen.string
	else:
		openBool = "false"

	if case.sTitle.string != None:
		title = case.sTitle.string.encode('utf-8').decode('ascii', 'ignore').replace(',',' ').replace('[', ' ').replace(']', ' ').lower()
		#print(title)
		titlelist = title.split()
		wordlist.extend(titlelist)
	else:
		title = "No Title"


ignore_list = ['is', 'with', 'using', 'render', 'of', 'rp', 'after', 'does', 'project', 'thrown', 'the', 'and', 'urp', 'universal', 'a', 'but', 'to', 'are', 'for', 'have', 'has', 'cases', 'when', 'on', 'uwp', 'errors', 'in', 'not', 'wsa', 'build', 'backport']
#print(wordlist)
#most_common_words= [word for word, word_count in Counter(wordlist).most_common(3) if word not in ignore_list]
most_common_words = Counter(word for word in wordlist if word not in ignore_list).most_common(10)
#top_3 = {k: most_common_words[k] for k in list(most_common_words)[:10]}
print(most_common_words)
print("Done")
