def display_inventory(inventory):
    total_value = 0
    count = 0
    categories = set()
    for item in inventory:
        print(f"{item['name']} ", end="")
        print(f"({item['category']}, {item['type']} ): ", end="")
        print(f'{item["quantity"]}x @ {item["values"]} ', end="")
        print(f'gold each = {item["quantity"] * item["values"]} gold')
        total_value += item['quantity'] * item['values']
        count += item['quantity']
        categories.add(item["category"])
    print(f"\nInventory value: {total_value} gold")
    print(f"Item count: {count} items")
    print("Categories: ", categories)


def count_total_gold(inventory):
    total = 0
    try:
        for item in inventory:
            total += item['values'] * item['quantity']
        return total
    except KeyError as e:
        print(e)


def ft_inventory_system():
    print("=== Player Inventory System ===\n")
    alice_inventory = [
            {
                "name": "sword",
                "category": "weapon",
                "type": "rare",
                "quantity": 1,
                "values": 500
            },
            {
                "name": "potion",
                "category": "consumable",
                "type": "common",
                "quantity": 5,
                "values": 50
            },
            {
                "name": "shield",
                "category": "armor",
                "type": "uncommon",
                "quantity": 1,
                "values": 200
            }
    ]
    print("=== Alice's Inventory ===")
    display_inventory(alice_inventory)
    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    bob_inventory = []
    make_transaction(alice_inventory, bob_inventory, 'potion', 2)
    print(bob_inventory)
    print("=== Updated Inventories ===")
    alice_potions_count = count_item_inventory(alice_inventory, 'potion')
    bob_potions_count = count_item_inventory(bob_inventory, 'potion')
    print(f"Alice potions: {alice_potions_count}")
    print(f"Bob potions: {bob_potions_count}\n")


def make_transaction(inventory1, inventory2, item, quantity):
    try:
        for i in inventory1:
            if (i['name'] == item):
                i['quantity'] -= quantity
                if (i['quantity'] == 0):
                    inventory1.remove(i)
                elif (i['quantity'] < 0):
                    i['quantity'] += quantity
                    print("Can't Make Transaction Not Enough Items")
                    break
                c = i.copy()
                c['quantity'] = quantity
                inventory2.append(c)
                print("Transaction successful!\n")
                break
    except KeyError as e:
        print(e)


def count_item_inventory(inventory, item):
    count = 0
    try:
        for i in inventory:
            if (i['name'] == item):
                count += i['quantity']
    except KeyError as e:
        print(e)
    return count


ft_inventory_system()
