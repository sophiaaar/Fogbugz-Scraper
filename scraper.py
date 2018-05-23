from fogbugz import FogBugz
from datetime import datetime, timedelta
import csv

# Fill in the following values as appropriate to your installation
S_FOGBUGZ_URL   = 'https://fogbugz.unity3d.com'
S_EMAIL         = ''
S_PASSWORD      = ''

fb = FogBugz(S_FOGBUGZ_URL)
fb.logon(S_EMAIL, S_PASSWORD)

#Get all cases in milestone 332 (2018.2)
resp = fb.search(q='ixFixFor=332"',cols='ixBug, ixBugParent, fOpen, sTitle, ixProject, ixArea, sArea, ixStatus, ixPriority,sFixFor, dtFixFor, sVersion, sComputer, c, ixCategory, dtOpened, dtClosed')
print resp
filename = "fogbugzData.csv"

csv = open(filename, "w")

columnTitleRow = "ixBug, ixBugParent, fOpen, sTitle, ixProject, ixArea, sArea, ixStatus, ixPriority,sFixFor, dtFixFor, sVersion, sComputer, c, ixCategory, dtOpened, dtClosed"
csv.write(columnTitleRow)

for case in resp.cases.childGenerator():
	#no 'if' check needed (currently)
	#assign the cols to variables
	print "hello"
	bugID = case.ixBug.string
	print bugID
	title = case.sTitle.string
	print title

	row = bugID + "," + title #etc!!

	csv.write(row)
