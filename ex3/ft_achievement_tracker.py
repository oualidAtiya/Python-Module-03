def ft_achievement_tracker():
    print("=== Achievement Tracker System ===\n")
    alice_ach = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob_ach = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    char_ach = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon'}
    char_ach.add('perfectionist')
    print(f"Player alice achievements: {alice_ach}")
    print(f"Player bob achievements: {bob_ach}")
    print(f"Player charlie achievements: {char_ach}")

    print("=== Achievement Analytics ===")
    uniq_ach = alice_ach.union(bob_ach).union(char_ach)
    print(f"All unique achievements: {uniq_ach}")
    print(f"Total unique achievements: {len(uniq_ach)}\n")
    common_ach = alice_ach.intersection(bob_ach).intersection(char_ach)
    print(f"Common to all players: {common_ach}")
    alice_rare_ach = alice_ach.difference(bob_ach).difference(char_ach)
    bob_rare_ach = bob_ach.difference(alice_ach).difference(char_ach)
    char_rare_ach = char_ach.difference(alice_ach).difference(bob_ach)
    rare_ach = alice_rare_ach.union(bob_rare_ach).union(char_rare_ach)
    print(f"Rare achievements: (1 player): {rare_ach}\n")
    print(f"Alice vs Bob common: {alice_ach.intersection(bob_ach)}")
    print(f"Alice unique: {alice_ach.difference(bob_ach)}")
    print(f"Bob unique: {bob_ach.difference(alice_ach)}")


ft_achievement_tracker()
