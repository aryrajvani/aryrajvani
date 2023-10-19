names= ["Angie", "Sonia","Mona","Sarita","Samona"]
#names = names_string.split(", ")
import random
number= len(names)
ran_choi= random.randint(0,number-1)
person_pay= names[ran_choi]
print(person_pay+ ",Hit it,Your Turn")
