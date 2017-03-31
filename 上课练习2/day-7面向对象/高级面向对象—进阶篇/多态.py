#!/usr/bin/env python
#-*-conding:utf-8-*-


class Animal:
    def __init__(self,name):
        self.name = name
    def talk(self):
        raise NotImplemented("subclass must implement absstact method")


class cat(Animal):
    def talk(self):
        return "Meow"

class dog(Animal):
    def talk(self):
        return "Woof Woof!"

def animal_talk(obj):
    print(obj.talk())

c = cat("sanjiangmei")
d = dog("sanjiangyuan")

animal_talk(c)
animal_talk(d)



'''
animals = [cat("missy"),
           dog("lassie")]

for animal in animals:
    print (animal.name + ':' + animal.talk())
'''

