

class Singleton(type):

    __instance = None
    
    def __call__(self,*args,**kwargs): 
        if self.__instance is None:
            self.__instance = super().__call__(*args,**kwargs)
        else:
            self.__instance.__init__(*args,**kwargs)
        return self.__instance   