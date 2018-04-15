from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.lang import Builder
 

lexicon = {
        #adjectives

        'forever':'plirtjhir', 'all':'plírt', 'alot':'plirt', 'probably':'pírbli', 'red':'riscirt', 'stupid':'ritter',
        'dark':'nwumei', 'night':'nwumweijhir','evening':'nwumweijhirplir', 'stagnantly':'nwujhirli',
        'next':'jonír', "easy": "fajile", 'easy going': 'fajweh', 'skinny':'flirc', 'fat':'gírd', 'fatness':'girjírn', 
        'overweight':'girplir', 'obease':'girplírt','fragile':"fajirl","easy": "nwuarmír", "a":"une",
        "white":",blankirt","thoroughly" : "bonírli", 'bright':'ilum', 'charismatic':'jírsmiweh',
        'brown':'kacirt', 'hot':'kuh','hell-like':'kuhplirtli','black':'nekírt', 'powerless':'nwuhpír',
        'next':'siguír',
        "good":"bonír", "great":"bonírplir", "excellent":"bonírplirt",'little' :'írto',


            #nouns
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
        "pig" : "swírn",

        #verbs

        'create':'malirweh', 'mortar': 'mortír', 'die':'nwuh','cannot':'nwuhpír','lie':'nwuhkwír', 'dislike':'nwuhjír',
        'like':'jír', 'kill':'jide',  'know':'jírse', 'force':'jyub', 'tell':'jíatír','burn' :'kunír',
         'own':'tenír', 'give':'díhr',
         'stay':'restír','understand':'sensír','happen':'sucidír','hear':'senwír','impress':'vírjide',
         'win':'vicír','come':'vírn','see':'veyír' , 'rebel':'tuhrnír','look':'veícir','unsettle':'tírb',
         'reach':'gantir', 'close': 'imecír', 'shut':'imejír', 'think (mediate)' :'íkjwaír','complete-destruction':'plírtwehjide',
         'upset':'infierír', 'go' :'irte', 'loose':'nubtenír', 'live':'nduzi', 'get':'obtír',
         "add": "ahsumír", "work" : "armír", "function":"armírbon","can":"pír",'must or should':'faírte',
         "see": "veyír", "functions":"armírbon", 'discover':'discírve', 'do':'dírn','have':'nwír', 'can':'pír',
         'scatter':'diaspír', 'stop':'detenír', 'destroy':'detrír' , 'form or shape':'fírme','allow':'permír',

        #preps
        'right-here':'yasa',
        'and':'inírt','over or on top of or cover':'írve','instead':'inna-lujír','in':'inna',
         'the':'irle', 'for':'fi', 'because':'fircirse','here':'dehyah','all directions':'dehplirt',
         'there': 'dede', 'right there': 'dehsuh', "-ing":"a", "it's right there":"a-dede","it's in there":"a-inna",
         "to (or as)": "ah","sometimes (or at times)":"a-jhíer", "again":"aplir", "with":"anír", 'if':'síre',
         "with many":"anírplirt", "all together" :"Anírplirt",  "is":"esír","at this time":"ahkírjir",
         "at times": "A-jhíer", "doing" : "a" , 'or' :'ih', 'really or yes': 'ihh', 'but':'píhr', "all-directions":'suh-ah-suh',
         "when":"ahkírjir", 'what': 'kírse', 'how':'kedgírse','who': 'mjahwírse',
         'why':'pírcirse', 'because':'fircirse', 

#pros
"he": "im","i":"mi",
"we":"nus",
'it':'oí',
"you":"vus",
"you all":"unnos",
"they" : "dims",
"my" :"a-mírn" ,
"yours" :"a-vírm", 
"his": "a-im ",
"hers ":"a-smweí",
"ourselves" :'nus-mírnes',
"each-other":"tras-mírmes",

        #preplist

        "ing":"a","its-there": "a-dede",'its-in-there': "a-inna",
        'sometimes': "a-jhíer",'at-times': "aplir",
         "again":"anír", "more": "anírplirt",

        #negations:

        "no": "buh", "not": "bun", 

}

pastMark = ['ed',]
past = 0

#individual characters List
indCharsList = []

class Query(BoxLayout):

    
    def engToLan(self):
        global past
        global indCharsList
        #check for spaces in user input
        #when space found split the string into list
        #join each word into into list for each iteration

        

        if ' ' in self.ids.entry.text:
            wList = self.ids.entry.text.split(' ')
            wAmt = len(wList)
            newList = [] 
            answer = ' '.join(wList)
            ANSWER = answer.lower()

        # checking if this is past tense

        # split entry into indiv chars if the last two chars in the potential past tense
        #words are ed. this is one way that i am handling the past tense. NEed to figure
        #something out for irregular past tense verbs
            
            if 'ed' in self.ids.entry.text:
                for chars in self.ids.entry.text:
                
                    if chars =='e':
                        
                        indCharsList.append('e')
                        print('found an e')
                        

                        #if indCharsLi

                    if chars == 'd':
                        indCharsList.append('d')
                        past = 1 > 2
                        print('found a d')   
                            #print(indCharsList)

                    else:
                        #indCharsList.append(' ')
                        print('nothing')

               # print(indCharsList[-1])
                #print(indCharsList[:-2])

                if indCharsList[-1:] == 'd' and indCharsList[:-2] == 'e':
                  
                        
                    print(past)
                    past = 1 < 2
                        
                    while past:
                        wList2 = str(indCharsList[:]).split('d')
                        wList3 = str(wList2[:]).split(' ')
                        pastProps = []
                        pastProps.append(wList2)
                        pastNow = ','.join(wList2)
                        #print(wList3)
                        #print(indCharsList)
                        #print(wList3)
                        past = 1 > 2

                        
                else:
                    past = 1 > 2
                #    innerCharsList.remove('e')
                    
                    print('no e')

                    print('future or present')

    
                
                    '''
                    for char in wList:
                        n = char.split(' ')
                        if 'ed' in n:
                            print(n)
                            print('ed found')
                        
                            pastProps = []
                            #pastNow = ''.join(pastID)
                            pastProps.append(wList)
                            pastNow = pastProps.split(' ')
                            
                        #print(pastNow)
                    print(pastNow)
'''
            
                    
                
               # print(wList)
            #print(wAmt)
           
            for response in wList:

                respond = response.lower()
                
                if respond in lexicon:
                    

                    newList.append(lexicon[respond])
                    print(newList)
                    fTrans = ' '.join(newList)
                    output = fTrans[:] 
                    self.ids.result.text = output

               # if 'ing' in self.ids.entry.text:
                #    present = wList.append('a')

                 
        else:
    #directions for if there is no space in the user input

            oneWordResponse = self.ids.entry.text.lower()
            
            if oneWordResponse in lexicon:
            
                output = lexicon[oneWordResponse]
                self.ids.result.text = output
                wList = []
            else:
        #this is where the english to lantousir conditions will be declared
                
                if 'í' in self.ids.entry.text:
                    output = self.ids.entry.text
                    #self.ids.result.text = output
                    

                else:

                    output = "Sorry that word doesn't exist. Try Again. Use - for compund words like 'little-brother.'"
                    self.ids.result.text = output
                        

    
            
                            
                          
           
        
class Lan_TranApp(App):
    def build(self):
        return Query()

if __name__== "__main__":
    Lan_TranApp().run()
            

