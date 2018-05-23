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
resp = fb.search(q='milestone:"2018.2"',cols="ixBug,ixBugParent,fOpen,sTitle,sProject,ixArea,sArea,sStatus,ixPriority,sFixFor,sVersion,sComputer,ixCategory,dtOpened,dtClosed,plugin_customfields_at_fogcreek_com_userxpainr32d")
#print resp
filename = "fogbugzData.csv"

csv = open(filename, "w")

columnTitleRow = "Bug ID,Bug Parent ID,is Open,Title,Project,Area ID,Area,Status,Priority,Fix For,Version,Computer,Category,User Pain"

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

	if case.sTitle.string != None:
		title = case.sTitle.string.encode('utf-8').decode('ascii', 'ignore').replace(',',' ')
	else:
		title = "No Title"

	if case.sProject.string != None:
		project = case.sProject.string
	else:
		project = ""

	if case.ixArea.string != None:
		areaID = case.ixArea.string
	else:
		areaID = "0"

	if case.sArea.string != None:
		area = case.sArea.string.replace(',',' ')
	else:
		area = ""

	if case.sStatus.string != None:
		status = case.sStatus.string
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
		version = case.sVersion.string.replace(',',' ')
	else:
		version = "Unknown"

	if case.sComputer.string != None:
		computer = case.sComputer.string.encode('utf-8').decode('ascii', 'ignore').replace(',',' ')
	else:
		computer = "Unknown"

	if case.ixCategory.string != None:
		category = case.ixCategory.string
	else:
		category = "Unknown"

	if case.plugin_customfields_at_fogcreek_com_userxpainr32d.string != None:
		userpain = case.plugin_customfields_at_fogcreek_com_userxpainr32d.string
	else:
		userpain = "0"

	row = bugID +","+ bugParentID +","+ openBool +","+ title +","+ project +","+ areaID +","+ area +","+ status +","+ priority +","+ milestone +","+ version +","+ computer +","+ category +","+ userpain +","+ "\n"

	csv.write(row)
