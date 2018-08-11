


'''
author: Tyler J Dryden
app: Lan_Tran
twitter: @codeforthestreets
'''


from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.lang import Builder
from collections import defaultdict

vTok = {}
nKeyList = []
nValList = []
lexicon = {
        #adjectives
    'adjectives':{
        'forever':'plirtjhir', 'all':'plírt', 'alot':'plirt', 'probably':'pírbli', 'red':'riscirt', 'stupid':'ritter',
        'dark':'nwumei', 'night':'nwumweijhir','evening':'nwumweijhirplir', 'stagnantly':'nwujhirli',
        'next':'jonír', "easy": "fajile", 'easy going': 'fajweh', 'skinny':'flirc', 'fat':'gírd', 'fatness':'girjírn',
        'overweight':'girplir', 'obease':'girplírt','fragile':"fajirl","easy": "nwuarmír", "a":"une",
        "white":",blankirt","thoroughly" : "bonírli", 'bright':'ilum', 'charismatic':'jírsmiweh',
        'brown':'kacirt', 'hot':'kuh','hell-like':'kuhplirtli','black':'nekírt', 'powerless':'nwuhpír',
        'next':'siguír',
        "good":"bonír", "great":"bonírplir", "excellent":"bonírplirt",'little' :'írto',},


            #nouns]
    'nouns':{
           'types' : 'tirps', 'movement':'víjín', 'vision':'vision', 'whole-world':'tirahplírt',
         'bluntness':'yavírn', 'close-range-murder':'yavírjide',
        'nose':'wumzír', 'image': 'wehvír', 'nostrils':'wumzirplír', 'victory':'vicjírn','matter':'weh',
         'other':'tras','verse':'vírse','embarresment':'wehjide','cold-blooded-murder':'tírbjide',
        'tongue':'reh', 'mouth':'rechír','language':'rejah','dictionary':'sensaíre', 'art':'sensweh','earth':'tirah',
         'human-extinction':'sírjin', 'society':'sírjin', 'body': 'tiraweh', 'stone':'tira-okpukír','hell':'terrir',
         'south':'sír', 'sister':'sisma', 'little-sister':'sismírto', 'southern':'síjírn','others':'sírj', 'smart':'smirt',
        'double-murder':'pírehjíde','flat':'plairn', 'child':'pickney', 'conflict':'píreh', 'sometimes':'plirjhir',
        'message':'okwíjírn', 'heart':'oozirjír', 'mobility':'oozírjírn', 'father':'prair', 'son':'bwoy-pickney',
        'daughter':'ngyal-pickney', 'everything':'plirtweh',
         'bones':'okpukpír','tommorow':'neímweijhir', 'time':'ojhír', 'word':'okwír', 'door':'oozír',
         'water':'osmír', 'blood':'osmírtaweh', 'eye':'oozírweh', 'pupils':'oorjweplírt','possession':'obtírjírn',
         'nwuhweh': 'variable', 'last':'nuhplír','barren' :'nwuhjadírne', 'unconscious':'nwuhtira',
        'deceit':'nwukijírn', 'nonsense':'nwuhsensír', 'past':'nwujhir', 'west':'nwehs', 'ears':'nwir',
         'north':'nwírh','discord': 'nwuhjarmijírn', 'bad':'nwuhbonír', 'life-essence':'nduhweh', 'vagina':'nduzi',
        'girl':'ngyal', 'everyday':'mjawehplirt', 'everyone':'mjawehplirt', 'nothing':'nuhweh', 'alone': 'nwuhnír',
        'medicine':'mjadírne', 'god':'mjah', 'logic':'mjahijwo', 'mother':'maira', 'beginning':'malijhír','start':'malír',
        'monument': 'monírme', 'generation':'mjwajhírn', 'person':'mjaweh',  'homicide':'mjahwehjide',
        'man':'mwon', 'woman': 'mwomei', 'morning':'mwírn', 'stars' : ' mwesehly','day': 'mweíjhir','sun':'mwei',
        'garden': 'jadírne', 'moon':'lune', 'lamír': 'name', 'perfect': 'jírseplirt','hell on earth':'jaíplírt', 'charisma':'jírsmíjírn',
        'drug':'jírg','master':'jukír', 'most high':'jukweh', 'sound':'jírtu', 'chaos':'jaís', 'partner': 'jenyír',
        'chapter':'isi', 'gold':'ír', 'money':'irjírn', 'east':'írste', 'communication' : 'ikjírn',
        'right now':'curojhir', "now" : "cur", "white": "blankirt", "today" : "curmweijhir", "almost-dead": "curnwuh",
         "cambír" : "change", "country": "citeir", 'city': 'citeírto', 'face': 'círa', 'heavens':'kushírme',
         "thoroughly":"bonírli", "greatness":"boníjírn", "brick":"brírck","young-boy":"bwoyírto" ,
         "boy":"bwoy", "brother":"brahfir", "to be alive": "curonduh", 'eye lids': 'írve-oozirweh',
         "little-brother": "brafírto", 'pregnant':'encírt', 'house':'hiruse','harmony':'jarmírne', 'fire':'kuhplir',
         "hard-work" : "armírplír", "adjective":"ajirtev", "easy":"nwuarmír",'destruction':'detrírplírt',
        "pig" : "swírn",},

        #verbs
        'verbs':{
        'create':'malirweh', 'mortar': 'mortír', 'die':'nwuh','cannot':'nwuhpír','lie':'nwuhkwír', 'dislike':'nwuhjír',
        'like':'jír', 'kill':'jide',  'know':'jírse', 'force':'jyub', 'tell':'jíatír','burn' :'kunír',
         'own':'tenír', 'give':'díhr', 'chat':'chatír',
         'stay':'restír','understand':'sensír','happen':'sucidír','hear':'senwír','impress':'vírjide',
         'win':'vicír','come':'vírn','see':'veyír' , 'rebel':'tuhrnír','look':'veícir','unsettle':'tírb',
         'reach':'gantir', 'close': 'imecír', 'shut':'imejír', 'think (mediate)' :'íkjwaír','complete-destruction':'plírtwehjide',
         'upset':'infierír', 'go' :'irte', 'loose':'nubtenír', 'live':'nduzi', 'get':'obtír',
         "add": "ahsumír", "work" : "armír", "function":"armírbon","can":"pír",'must or should':'faírte',
         "see": "veyír", "functions":"armírbon", 'discover':'discírve', 'do':'dírn','have':'nwír', 'can':'pír',
         'scatter':'diaspír', 'stop':'detenír', 'destroy':'detrír' , 'form or shape':'fírme','allow':'permír',
},
        #preps
        'preps':{
        'right-here':'yasa',
        'and':'inírt','over or on top of or cover':'írve','instead':'inna-lujír','in':'inna',
         'the':'irle', 'for':'fi', 'because':'fircirse','here':'dehyah','all directions':'dehplirt',
         'there': 'dede', 'right there': 'dehsuh', "-ing":"a", "it's right there":"a-dede","it's in there":"a-inna",
         "to (or as)": "ah","sometimes (or at times)":"a-jhíer", "again":"aplir", "with":"anír", 'if':'síre',
         "with many":"anírplirt", "all together" :"Anírplirt",  "is":"esír","at this time":"ahkírjir",
         "at times": "A-jhíer", "doing" : "a" , 'or' :'ih', 'really or yes': 'ihh', 'but':'píhr', "all-directions":'suh-ah-suh',
         "when":"ahkírjir", 'what': 'kírse', 'how':'kedgírse','who': 'mjahwírse',
         'why':'pírcirse', 'because':'fircirse',
},
#pros
 'pros':{   
"he": "im","i":"mi",
"she":"ji",
"her":"ji",
"we":"nus",
'it':'oí',
"you":"vus",
"you all":"unnos",
"they" : "dimz",
"my" :"a-mírn" ,
"yours" :"a-vírm",
"his": "a-im ",
"hers ":"a-smweí",
"ourselves" :'nus-mírnes',
"each-other":"tras-mírmes",
},
        #preplist
        'preplist':{
        "ing":"a","its-there": "a-dede",'its-in-there': "a-inna",
        'sometimes': "a-jhíer",'at-times': "aplir",
         "again":"anír", "more": "anírplirt",
},
        #negations:
        'negations':{
        "no": "buh", "not": "bun",

}}

pastMark = ['ed',]

lanToEngDict = {}




#individual characters List

indCharsList = []
wList3 = ''
regChars = []
past = 2 > 100
pastProps = []
keys = []
vals = []
wList2 = ''
wList = []
pastNow = ''
vToK = {}
transDirect =  1 < 2


class Query(BoxLayout):

        #splitter function will check for spaces in user input
        #& when a space is found it will split the string into a list.
        #Next it will join each element of the list for each iteration of response.

    def splitter(self):

        global wList
        global wAmt
        global newList
        global answer
        global ANSWER

        wList = self.ids.entry.text.split(' ')
        wAmt = len(wList)
        newList = []
        answer = ' '.join(wList)
        ANSWER = answer.lower()

        if transDirect:
            self.tenseMark()

        else:
            self.checker()
            
    def tenseMark(self):

        global response
        global respond      

        for response in wList:

            respond = response.lower()

            if past == True:
                self.pastTense()

            if past == False:

                self.checker()

            

    def checker(self):

        
        if respond in lexicon['adjectives']:
            
            newList.append(lexicon['adjectives'][respond])

        if respond in lanToEngDict.keys():
            newList.append(''.join(lanToEngDict[respond]))


        if respond in lexicon['verbs']:

            newList.append(lexicon['verbs'][respond])

        if respond in lexicon['nouns']:
            newList.append(lexicon['nouns'][respond])
            
        if respond in lexicon['pros']:
            newList.append(lexicon['pros'][respond])

        if respond in lexicon['preps']:

            newList.append(lexicon['preps'][respond])
                
        if respond in lexicon['negations']:
            newList.append(lexicon['negations'][respond])
                
        self.finalOut()


    def finalOut(self):

        global fTrans
        global output

        fTrans = ' '.join(newList)
        output = fTrans[:]
        self.ids.result.text = output

    def reverseDict(self):
        global lanToEngDict

        lanToEngDict = defaultdict(list)

        for k,v in lexicon['adjectives'].items():
           lanToEngDict[v].append(k)


        for k,v in lexicon['nouns'].items():
           lanToEngDict[v].append(k)

        for k,v in lexicon['verbs'].items():
           lanToEngDict[v].append(k)

        for k,v in lexicon['preps'].items():
           lanToEngDict[v].append(k)

        for k,v in lexicon['preplist'].items():
           lanToEngDict[v].append(k)

        for k,v in lexicon['pros'].items():
           lanToEngDict[v].append(k)

        for k,v in lexicon['negations'].items():
           lanToEngDict[v].append(k)



        self.lanToEng()


    def lanToEng(self):
        self.splitter()

    def pastTense(self):
        global pastAns
        global PASTANS

        for chars in self.ids.entry.text:
            indCharsList.append(chars)

            if chars == 'd':

                regChars.append(indCharsList)
                past = 1 < 2
                   

                if past:
                    pastAns = ANSWER.split('d')
                    PASTANS = ''.join(pastAns)
                    fpastAns = PASTANS.split(' ')
                    wList.append(fpastAns)

                    for pasts in fpastAns:
            
                        if pasts in lexicon['verbs']:
                            newList.append(lexicon['verbs'][pasts]+'d')


                            self.finalOut()
                        


    def engToLan(self):
        global indCharsList
        global wList2
        global wList3
        global past
        global pastNow
        global pastProps

        transDirect = 2 > 1

        if ' ' not in self.ids.entry.text:
            self.oneWord()


        if ' ' in self.ids.entry.text:
            self.splitter()


        if 'ed ' in self.ids.entry.text:
                self.pastTense()
        # checking if this is past tense

        # split entry into indiv chars if the last two chars in the potential past tense
        #words are ed. this is one way that i am handling the past tense. NEed to figure
        #something out for irregular past tense verbs


    def oneWord(self):
        
        global oneWordResponse

        oneWordResponse = self.ids.entry.text.lower()
        
        if oneWordResponse in lexicon['adjectives']:

            output = lexicon['adjectives'][oneWordResponse]
            self.ids.result.text = output
            wList = []

        if oneWordResponse in lexicon['nouns']:

            output = lexicon['nouns'][oneWordResponse]
            self.ids.result.text = output
            wList = []

        if oneWordResponse in lexicon['verbs']:

            output = lexicon['verbs'][oneWordResponse]
            self.ids.result.text = output
            wList = []

        if oneWordResponse in lexicon['preps']:

            output = lexicon['preps'][oneWordResponse]
            self.ids.result.text = output
            wList = []

        if oneWordResponse in lexicon['negations']:

            output = lexicon['negations'][oneWordResponse]
            self.ids.result.text = output
            wList = []

        if oneWordResponse in lexicon['pros']:

            output = lexicon['pros'][oneWordResponse]
            self.ids.result.text = output
            wList = []

        if oneWordResponse in lexicon['preplist']:

            output = lexicon['preplist'][oneWordResponse]
            self.ids.result.text = output
            wList = []
        
        else:

            output = "Sorry that word doesn't exist. Try Again. Use - for compund words like 'little-brother.'"
            self.ids.result.text = output



class Lan_TranApp(App):
    def build(self):
        return Query()

if __name__== "__main__":
    Lan_TranApp().run()
