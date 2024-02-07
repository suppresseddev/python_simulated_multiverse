class TABIMC:
    def __init__(self,name = "ConsoleBot", role = "", style = None):
        #This initializes a new bot.
        #You may optionally add a role, along with a style to your bot for pizazz.
        #Constants:
        self.Name = name
        self.Msg = ""
        self.Role = str(role)
        if self.Role != None:
            self.RoleStyle = str(style)
        else:
            self.RoleStyle = ""
    def role(self, role = None, style = None):
        #This method allows you to:
        #1. preview how your selected role looks
        #2. set a new role & style for the bot
        if role != None:
            self.Role = str(role)
            if style != None:
                self.RoleStyle = str(style)
        center = round(len(self.RoleStyle) / 2)
        front = self.RoleStyle[:center-1]
        back = self.RoleStyle[center:]
        if self.RoleStyle == "":
            front = ""
            back = ""
        return(str(front+str(self.Role)+back))
    def name(self, name = None):
        #This method allows you to:
        #1. identify the bot's name
        #2. set a new name for the bot
        if name != None:
            self.Name = str(name)
        else:
            return(self.Name)
    def say(self, msg):
        #Speaks the message "aloud" to the console.
        self.Msg = msg
        print(str(self.role())+" "+self.Name+": "+self.Msg)
    def tell(self, msg = None):
        if msg != None:
            self.Msg = str(msg)
        #Speaks the message "quietly" to whoever asked.
        return(str(self.role())+" "+self.Msg)
class MENU:
    def __init__(self):
        self.PageCount = 0
        self.PageNumber = None
        self.BarLength = 40
        self.Pages = []
        self.Header = []
    def addPage(self, title, func = None, desc = ""):
        #[Title, Function, Description]
        self.Pages.append([title, func, desc])
        self.PageCount += 1
    def removePage(self, page):
        self.Pages.remove(page-1)
        self.PageCount += -1
    def defHeader(self, title, desc = ""):
        self.Header = [str(title), None, str(desc)]
    def genTitle(self, title):
        halfbar = round((self.BarLength-(len(title)+1.5))/2)
        bar = "="*halfbar
        print(bar+"["+title+"]"+bar)
    def genDesc(self, desc):
        bar = "="*self.BarLength
        if len(bar)<len(desc):
            for i in range(0, len(desc), len(bar)):
                print(desc[i: i+len(bar)])
        else:
            print(desc)
        print(bar)
    def genPagenum(self):
        self.genTitle(str(self.PageNumber))
    def nextPage(self):
        self.PageNumber += 1
        if self.PageNumber > self.PageCount:
            self.PageNumber += -1
    def setPage(self, page):
        print(self.PageCount)
        if page in range(1, self.PageCount+1):
            self.PageNumber = int(page)
        else:
            print('Outside of page range.')
    def prevPage(self):
        self.PageNumber += -1
        if self.PageNumber < 1:
            self.PageNumber = 1
    def broadcast(self):
        if self.PageNumber == None:
            curTitle = self.Header[0]
            curFunc = self.Header[1]
            curDesc = self.Header[2]
            self.PageNumber = 1
        else:
            curTitle = self.Pages[self.PageNumber-1][0]
            curFunc = self.Pages[self.PageNumber-1][1]
            curDesc = self.Pages[self.PageNumber-1][2]
            self.genPagenum()
        self.genTitle(curTitle)
        self.genDesc(curDesc)
        if curFunc != None:
            curFunc()
    def stream(self):
        #CAUTION!!! THIS FUNCTION IS FOR FULLY DEVELOPED PROGRAMS WITH
        #PRE-PROGRAMMED PAGE NAVIGATION
        while True:
            megamenu.broadcast()
            serverInput = str(input('<Menu Control>')).upper()
            ends = ['ENDSTREAM', 'ENDBROADCAST', 'CLOSESTREAM', 'CLOSEBROADCAST']
            if serverInput in ends:
                print('Broadcast ended by server.')
                break
    def simplestream(self):
        #All purpose menu navigation, trust in the tried and true while loop.
        while True:
            megamenu.broadcast()
            serverInput = str(input('<Menu Control>')).upper()
            ends = ['ENDSTREAM', 'ENDBROADCAST', 'CLOSESTREAM', 'CLOSEBROADCAST']
            if serverInput in ends:
                print('Broadcast ended by server.')
                break
            if serverInput == "NEXTPAGE":
                print('Moving to next page.')
                self.nextPage()
            if serverInput[:7] == "SETPAGE":
                newpage = int(serverInput[7:])
                print('Moving to page '+ str(newpage) + ".")
                self.setPage(newpage)
            if serverInput == "PREVPAGE":
                print('Moving to previous page.')
                self.prevPage()
#TIME TO TEST!
# megamenu = MENU()
# def test():
#     print("OML ITS ACTUALLY RUNNING IT!?!?")
#     print("WTF IS UP WORLD!?")
#     a = int(input("Enter a number: "))
#     b = int(input("Enter a number: "))
#     print(str(a)+" multiplied by "+str(b))
#     print(a*b)
# megamenu.defHeader("My first header", "Hello World.")
# megamenu.addPage("Holy moly! Its the first Page!", None, "Update! This page now has a function. Lets see how it goes?")
# megamenu.addPage("The mystical second page!", test, "Navigating this may get confusing after a while.")
# megamenu.simplestream()
def generic_header(title = "", size = 35):
    #Generic Title Header
    barlen = round(((size-len(title))/2)+0.5)
    bar = ("="*barlen)
    heading = bar+"[ "+title+" ]"+bar
    print(heading)
def indented_header(title = "", size = 35):
    #Indented (centered) Title Header
    barlen = round(((size-len(title))/2)+0.5)
    bar = (" "*barlen)
    heading = bar+"[ "+title+" ]"+bar
    print(heading)
def indent(size = 35):
    #Segment of indent for a centered length of 'size'
    barlen = round(((size)/2)+0.5)
    bar = (" "*barlen)
    return(bar)