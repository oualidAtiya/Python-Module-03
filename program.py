alice_ach = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
bob_ach = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
char_ach = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon'}
char_ach.add('perfectionist')

alice_rare_ach = alice_ach.difference(bob_ach).difference(char_ach)
bob_rare_ach = bob_ach.difference(alice_ach).difference(char_ach)
char_rare_ach = char_ach.difference(alice_ach).difference(bob_ach)
print(alice_rare_ach.union(bob_rare_ach).union(char_rare_ach))
