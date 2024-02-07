import sqlite3
from User import User
from Singleton import Singleton


class UserDAO(metaclass=Singleton):


    def __init__(self,db_file) -> None:
        self.__con = sqlite3.connect(db_file)


    def __enter__(self):
        print("enter")
        return self
    
    def __exit__(self, *exc):
        print("exit")
        self.__con.close()
        self.__con = None
        return False


    def findById(self,id):

        sql = "SELECT * FROM users_tbl WHERE id = ?"
        cur = self.__con.cursor()
        
        res = cur.execute(sql,(id,))        
        u = res.fetchone() 
        print(u)


    def findAll(self):
        sql = "SELECT * FROM users_tbl"
        cur = self.__con.cursor()

        res = cur.execute(sql)

        for r in res.fetchall():
            u = User(*r)
            yield u
        

    def __del__(self):
        if self.__con:
            self.__con.close()