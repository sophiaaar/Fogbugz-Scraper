from fogbugz import FogBugz
import csv

# Fill in the following values as appropriate to your installation
S_FOGBUGZ_URL   = 'https://fogbugz.unity3d.com'
TOKEN			= ""
S_EMAIL         = ''
S_PASSWORD      = ''

fb = FogBugz(S_FOGBUGZ_URL, TOKEN)
#fb.logon(S_EMAIL, S_PASSWORD)

#Get all cases in milestone 2018.2
resp = fb.search(q='milestone:"2018.2"',cols="ixBug,ixBugParent,fOpen,sTitle,ixProject,ixArea,sArea,ixStatus,ixPriority,sFixFor,sVersion,sComputer,c,ixCategory,dtOpened,dtClosed")
print resp
filename = "fogbugzData.csv"

csv = open(filename, "w")

columnTitleRow = "ixBug, ixBugParent, fOpen, ixProject, ixArea, sArea, ixStatus, ixPriority, sFixFor, sVersion, c, ixCategory"

csv.write(columnTitleRow)
csv.write("\n")

for case in resp.cases.childGenerator():
	#assign the cols to variables
	if case.ixBug.string != None:
		bugID = case.ixBug.string

	if case.ixBugParent.string != None:
		bugParentID = case.ixBugParent.string
	else:
		bugParentID = "0"

	if case.fOpen.string != None:
		openBool = case.fOpen.string
	else:
		openBool = "false"

	#if case.sTitle.string != None:
	#	title = case.sTitle.string
	#else:
	#	title = "No Title"

	if case.ixProject.string != None:
		project = case.ixProject.string
	else:
		project = ""

	if case.ixArea.string != None:
		areaID = case.ixArea.string
	else:
		areaID = "0"

	if case.sArea.string != None:
		area = case.sArea.string
	else:
		area = ""

	if case.ixStatus.string != None:
		status = case.ixStatus.string
	else:
		status = "Unknown"

	if case.ixPriority.string != None:
		priority = case.ixPriority.string
	else:
		priority = "0"

	if case.sFixFor.string != None:
		milestone = case.sFixFor.string
	else:
		milestone = "2018.2" #change this when I make the milestone a cmd line arg

	if case.sVersion.string != None:
		version = case.sVersion.string
	else:
		version = "Unknown"

	#if case.sComputer.string != None:
	#	computer = case.sComputer.string
	#else:
	#	computer = "Unknown"

	if case.c.string != None:
		occurences = case.c.string
	else:
		occurences = "0"

	if case.ixCategory.string != None:
		category = case.ixCategory.string
	else:
		category = "Unknown"

	row = bugID +","+ bugParentID +","+ openBool +","+ project +","+ areaID +","+ area +","+ status +","+ priority +","+ milestone +","+ version +","+ occurences +","+ category +","+ "\n"

	csv.write(row)
