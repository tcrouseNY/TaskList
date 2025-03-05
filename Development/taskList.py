################################################
###         Written by:  Todd Crouse
###         For project tracking
################################################
from idlelib.sidebar import EndLineDelegator

### Things to get from a datasource connection
def UserLogin(userID: str, userPassword: str) -> int:

    ### Need data source for user login to return the userID
    return 1



### Get a list of the projects in the DB
def GetProjectList(boCurrent: bool) -> list:
    ### This that and the other stuff goes here.  Only return active projects!
    if boCurrent:
        return 1
    else:
        return 1

##
def CreateNewProject( ) -> bool:
    ### Lets add a new project... yeah!
    strNewProj = input("Need new project name: ")
    strProjLaunchDate = input("Need new project launch date: ")
    ### if success add to datasource
    return True

def GetProjectHeaders(intProjID: str) -> list:
    ### needs to come from datasource
    ### Report title info
    strProjectName = 'Delivery Schedduling API Load Testing Status'
    intLogedInUserID = 1
    strTodaysDate  = '03/03/2025'
    return f"strProjectName + ' ' + strTodaysDate"


def GetProjectDetails(intProjID: str) -> list:
    ### needs to come from datasource
    ###  Task List
    GetProjectDetails =  [
        "Scheduled"|
        "03/12/2025"|
        "100"|
        "Plan for release is on 03/24/2025"
    ]

### print the needed info
def printProjectInfo(strProjInfo: str):
    print(strProjInfo)

### Run
intUserID = UserLogin("tcrouse","password")
if GetProjectList(True):
    GetProjectHeaders(1)
else:
    GetProjectHeaders(1)

GetProjectDetails(1)

CreateNewProject()



###
"""add tasks
retrieve them (all or by id)
update % complete and notes (assuming due date is static for now)
optionally: delete or archive them"""
###
