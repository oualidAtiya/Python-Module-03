def make_transaction(inv1, inv2, item, q):
    copy = inv1.get(item).copy()
    inv2.update({item: copy})
    inv2.get(item).update({"quantity": q})
    inv1.get(item).update({"quantity": inv1.get(item).get("quantity") - q})
    print("Transaction successful!\n")


def display_inventory(inventory):
    try:
        total = 0
        count = 0
        categories = {}
        for k, v in inventory.items():
            print(f'{k} ({v.get("category")}, {v.get("type")}): ', end="")
            print(f'{v.get("quantity")}x  @ {v.get("values")} gold', end="")
            print(f' each = {v.get("quantity") * v.get("values")} gold')
            total += v.get("values") * v.get("quantity")
            count += v.get("quantity")
            if (v.get("category") in categories):
                n = categories.get(v.get("category"))
                categories.update({v.get("category"): n + v.get("quantity")})
            else:
                categories.update({v.get("category"): v.get("quantity")})
        print(f"Inventory value: {total} gold")
        print(f"Item count: {count} items")
        print("Categories: ", end="")
        for k, v in categories.items():
            print(f"{k}({v}) ", end="")
    except Exception as e:
        print(e)


def count_total_gold(inventory):
    total = 0
    for v in inventory.values():
        total += v.get("values") * v.get("quantity")
    return total


def count_items(inventory):
    count = 0
    for v in inventory.values():
        count += v.get("quantity")
    return count


def ft_inventory_system():
    print("=== Player Inventory System ===\n")
    inventories = {
            "alice": {
                "sword": {
                    "category": "weapon",
                    "type": "rare",
                    "quantity": 1,
                    "values": 500
                },
                "potion": {
                    "category": "consumable",
                    "type": "common",
                    "quantity": 5,
                    "values": 50
                },
                "shield": {
                    "category": "armor",
                    "type": "uncommon",
                    "quantity": 1,
                    "values": 200
                }
            },
            "bob": {
                "magic_ring": {
                    "category": "consumable",
                    "type": "rare",
                    "quantity": 1,
                    "values": 50
                },
                "shield": {
                    "category": "armor",
                    "type": "uncommon",
                    "quantity": 1,
                    "values": 200
                }
            }

    }
    print("=== Alice's Inventory ===")
    try:
        alice_inventory = inventories.get('alice')
        display_inventory(alice_inventory)
    except KeyError as e:
        print(e)
    print("\n\n=== Transaction: Alice gives Bob 2 potions ===")
    bob_inventory = inventories.get("bob")
    make_transaction(alice_inventory, bob_inventory, 'potion', 2)
    print("=== Updated Inventories ===")
    alice_potions_count = alice_inventory.get("potion").get("quantity")
    bob_potions_count = bob_inventory.get("potion").get("quantity")
    print(f"Alice potions: {alice_potions_count}")
    print(f"Bob potions: {bob_potions_count}\n")
    print("=== Inventory Analytics ===")
    player = None
    total_gold = -1
    for k, v in inventories.items():
        if (count_total_gold(v) > total_gold):
            total_gold = count_total_gold(v)
            player = k
    print(f"Most valuable player: {player.capitalize()}: ({total_gold} gold)")
    player = None
    count = -1
    for k, v in inventories.items():
        if (count_items(v) > count):
            count = count_items(v)
            player = k
    print(f"Most items: {player.capitalize()}: ({count} items)")

    all_items = {}
    for v in inventories.values():
        for k in v.keys():
            if (k not in all_items):
                all_items.update({k: 1})
            else:
                all_items.update({k: all_items.get(k) + 1})
    print("Rarest items: ", end="")
    for k, v in all_items.items():
        if (v == 1):
            print(k, end=" ")


ft_inventory_system()
