from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.clock import Clock
import threading

adjs = {'forever':'plirtjhir', 'all':'plírt', 'alot':'plirt', 'probably':'pírbli', 'red':'riscirt', 'stupid':'ritter',
        'dark':'nwumei', 'night':'nwumweijhir','evening':'nwumweijhirplir', 'stagnantly':'nwujhirli',
        'next':'jonír', "easy": "fajile", 'easy going': 'fajweh', 'skinny':'flirc', 'fat':'gírd', 'fatness':'girjírn', 
        'overweight':'girplir', 'obease':'girplírt','fragile':"fajirl","easy": "nwuarmír", "a":"une",
        "white":",blankirt","thoroughly" : "bonírli", 'bright':'ilum', 'charismatic':'jírsmiweh',
        'brown':'kacirt', 'hot':'kuh','hell-like':'kuhplirtli','black':'nekírt', 'powerless':'nwuhpír',
        'next':'siguír',
        "good or beautiful":"bonír", "very good":"bonírplir", "excellent":"bonírplirt",}


nouns = {'types': 'tirps', 'movement':'víjín', 'vision':'vision', 'whole-world':'tirahplírt',
         'bluntness':'yavírn', 'close-range-murder':'yavírjide',
        'nose':'wumzír', 'image': 'wehvír', 'nostrils':'wumzirplír', 'victory':'vicjírn','matter':'weh',
         'other':'tras','verse':'vírse','embarresment':'wehjide','cold-blooded-murder':'tírbjide',
        'tongue':'reh', 'mouth':'rechír','language':'rejah','dictionary':'sensaíre', 'art':'sensweh','earth':'tirah',
         'human-extinction':'sírjin', 'society':'sírjin', 'body': 'tiraweh', 'stone':'tira-okpukír','hell':'terrir',
         'south':'sír', 'sister':'sisma','southern':'síjírn','others':'sírj', 'smart':'smirt',
        'double-murder':'pírehjíde','flat':'plairn', 'child':'pickney', 'conflict':'píreh', 'sometimes':'plirjhir',
        'message':'okwíjírn', 'heart':'oozirjír', 'mobility':'oozírjírn', 'father':'prair', 'everything':'plirtweh',
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
         "hard-work" : "armírplír", "adjective":"ajirtev", "easy":"nwuarmír",'destruction':'detrírplírt'
         }

verbs = {'create':'malirweh', 'mortar': 'mortír', 'die':'nwuh','cannot':'nwuhpír','lie':'nwuhkwír', 'dislike':'nwuhjír',
        'like':'jír', 'kill':'jide',  'know':'jírse', 'force':'jyub', 'tell':'jíatír','burn' :'kunír',
         'own':'tenír',
         'stay':'restír','understand':'sensír','happen':'sucidír','hear':'senwír','impress':'vírjide',
         'win':'vicír','come':'vírn','see':'veyír' , 'rebel':'tuhrnír','look':'veícir','unsettle':'tírb',
         'reach':'gantir', 'close': 'imecír', 'shut':'imejír', 'think or mediate' :'íkjwaír','complete-destruction':'plírtwehjide',
         'upset or infuriate':'infierír', 'go' :'irte', 'loose':'nubtenír', 'live':'nduzi', 'get':'obtír',
         "add": "ahsumír", "work" : "armír", "function":"armírbon","can":"pír",'must or should':'faírte',
         "see": "veyír", "functions":"Armírbon", 'discover':'discírve', 'to do':'dírn','have':'nwír', 'can':'pír',
         'scatter':'diaspír', 'detenír':'stop', ' detrír': 'destroy', 'form or shape':'fírme','allow':'permír',
         }

preps = {'right-here':'yasa',
        'and':'inírt','over or on top of or cover':'írve','instead':'inna-lujír','in':'inna',
         'the':'irle', 'for':'fi', 'because':'fircirse','here':'dehyah','all directions':'dehplirt',
         'there': 'dede', 'right there': 'dehsuh', "-ing":"a", "it's right there":"a-dede","it's in there":"a-inna",
         "to (or as)": "ah","sometimes (or at times)":"a-jhíer", "again":"aplir", "with":"anír", 'if':'síre',
         "with many":"anírplirt", "all together" :"Anírplirt",  "is":"esír","at this time":"ahkírjir",
         "at times": "A-jhíer", "doing" : "a" , 'or' :'ih', 'really or yes': 'ihh', 'but':'píhr', "all-directions":'suh-ah-suh'
         }

quest = {"when":"ahkírjir", 'what': 'kírse', 'how':'kedgírse','who': 'mjahwírse',
         'why':'pírcirse', 'because':'fircirse', }

puncts = ["'", "."]

pros = {"he": "im","i":"mi",
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
"each-other":"tras-mírmes"
}

phrases = {"he is": "im-es", "you are": "vusir", "they are" : "dimsir", "i want " : "mi jhir ", }

preplst = ["a", "a-dede", "a-inna",
         "ah", "a-jhíer", "aplir",
         "anír", "anírplirt","esír",]
cont = 2 < 3

class Query(BoxLayout):
    
    def ask(self):

        if ' ' in self.ids.entry.text:
            if self.ids.entry.text not in pros or adjs or nouns or verbs or preps or quest:
                wList = self.ids.entry.text.split(' ')
                wAmt = len(wList)
                
            else:
                
                wList = []

            for response in wList:

                if response in pros:
                    
                    output = pros[response]
                    self.ids.result.text= output

                elif response in adjs:
                    output = adjs[response]
                    self.ids.result.text = output

                elif response in nouns:
                    output =nouns[response]
                    self.ids.result.text = output

                elif response in verbs:
                    output = verbs[response]
                    self.ids.result.text = output

                elif response in preps:
                    output = preps[response]
                        
                elif response in quest:
                    output = quest[response]

                elif response in phrases:
                    output = phrases[response]

        
        if self.ids.entry.text in pros:
            output= str(pros[self.ids.entry.text])
            self.ids.result.text = output
            
        elif self.ids.entry.text in adjs:
            output= str(adjs[self.ids.entry.text])
            self.ids.result.text = output

        elif self.ids.entry.text in nouns:
            output= str(nouns[self.ids.entry.text])
            self.ids.result.text = output

        elif self.ids.entry.text in verbs:
            output= str(verbs[self.ids.entry.text])
            self.ids.result.text = output

        elif self.ids.entry.text in preps:
            output= str(preps[self.ids.entry.text])
            self.ids.result.text = output

        elif self.ids.entry.text in quest:
            output= str(quest[self.ids.entry.text])
            self.ids.result.text = output
           
        

           
class Lan_TranApp(App):
    def build(self):
        return Query()

if __name__== "__main__":
    Lan_TranApp().run()
            
'''
while cont == True:
    
    trans = input("What would you like to translate into Lantousir?")
    

    if trans == "xx":
        cont = 2 > 3

        
    if " " in trans:
        if trans not in pros or adjs or nouns or verbs or preps or quest:
            wList = trans.split(' ')
            wAmt = len(wList)
    else:
        wList = []
        print('the word',"'", trans,"'" + ' was not found. Try again. some compound words')
        print("such as little brother don't exist in Lantuosir. Use a -. (ex. little-brother)")
        
                
    for response in wList:
        
        if response in pros:
            print(pros[response])
        elif response in adjs:
            print(adjs[response])
        elif response in nouns:
            print(nouns[response])
        elif response in verbs:
            print(verbs[response])
        elif response in preps:
            print(preps[response])
        elif response in quest:
            print(quest[response])
        elif trans in phrases:
            print(phrases[trans])
        else:
            print('the word',"'", response,"'" + ' was not found. Try again. some compound words')
            print("such as little brother don't exist in Lantuosir. Use a -. (ex. little-brother)")
    
        

        

    if trans in pros:
        print(pros[trans])
        
    elif trans in adjs:
        print(adjs[trans])

    elif trans in nouns:
        print(nouns[trans])

    elif trans in verbs:
        print(verbs[trans])
    elif trans in quest:
        print(quest[trans])
    elif trans in preps:
        print(preps[trans])
    
        
   

            
    '''
