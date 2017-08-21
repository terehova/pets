class Pet(object):
    def __init__(self, name, species):
        self. name = name
        self.species = species
        
    def get_name(self):
        return self.name
    
    def get_species(self):
        return self.species
    
    def __str__(self):
        return "{} is a {}". format(self.name, self.species)
    

class Dog(Pet):
    def __init__(self, name, chases_cats):
        Pet.__init__(self, name, 'Dog')
        self.chases_cats = chases_cats
        
    def is_chases_cats(self):
         return self.chases_cats
        
    def say_smth(self):
         print "Woof,woof!!!"
         

class Cat(Pet):
    def __init__(self, name, hates_dogs):
        Pet.__init__(self, name, 'Cat')
        self.hates_dogs = hates_dogs
        
    def is_hates_dogs(self):
         return self.hates_dogs
        
    def say_smth(self):
         print "Meow,meow!!!"

class Mouse(Pet):
    def __init__(self, name, fears_cats):
        Pet.__init__(self, name, 'Mouse')
        self.fears_cats = fears_cats
        
    def is_fears_cats(self):
         return self.fears_cats
        
    def say_smth(self):
         print "Pe,pe!!!"
