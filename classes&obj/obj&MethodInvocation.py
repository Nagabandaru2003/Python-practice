class Naga:
    def __init__(self,lang):
        self._lang = lang
        
    def lang(self):
        print("language: ",self._lang)
    
ins = Naga("python")
ins.lang()