from character import Character

spiderman = Character("Peter Parker", "Spiderman")

print(spiderman.rname)
print(spiderman.sname)

spiderman.set_power("Spidey Sense")
spiderman.get_power()

spiderman.set_villain("Kraven The Hunter")
spiderman.get_villain()

superman = Character("Clark Kent", "Superman")

print(superman.rname)
print(superman.sname)

superman.set_power("Super Strength")
superman.set_villain("Lex Luthor")

superman.get_power()
superman.get_villain()

