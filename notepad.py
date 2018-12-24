import datetime
class CreateNote():
    def __init__(self,title,text=''):
        self.title=title
        self.dateTime=datetime.datetime.now()
        self.text=text
        
    def Edit(self):
        x=self.text
        y=input('Edit the text:')
        self.text=x+y
        
    def __str__(self):
        return('TITLE:{}\nDATE AND TIME OF CREATION:{}\nTEXT:{}'.format(self.title,self.dateTime,self.text))


