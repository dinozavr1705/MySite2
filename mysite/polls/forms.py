from django import forms

class User:
    def __init__(self,username,password):
        self.__password = password
        self.username = username

