# from base_person import *  # импортируем все классы
import base_person

man = base_person.Person("Andrey", 30, 100)
man.description_person()

warrior = base_person.Warrior("Aragorn", 35, 185)
print(warrior.description_person())

# Нового человека зовут: Andrey, ему 30, его рост 100, его вес 100
# Aragorn, ему 35, его заряд ярости 100




