def ft_inventory_system():
    print("=== Player Inventory System ===\n")
    print("=== Alice's Inventory ===")
    alice_inventory = [
            {
                "name": "sword",
                "category": ["weapon", "rare"],
                "quantity": 1,
                "values": 500
            },
            {
                "name": "potion",
                "category": ["consumable", "common"],
                "quantity": 5,
                "values": 50
            },
            {
                "name": "shield",
                "category": ["armor", "uncommon"],
                "quantity": 1,
                "values": 200
            }
        ]
    total_value = 0
    count = 0
    for item in alice_inventory:
        print(f"{item['name']}: ", end="")
        print(f"{item['category']} ", end="")
        print(f'{item["quantity"]}x @ {item["values"]} ', end="")
        print(f'gold each = {item["quantity"] * item["values"]} gold')
        total_value += item['quantity'] * item['values']
        count += item['quantity']
    print(f"\nInventory value: {total_value} gold")
    print(f"Item count: {count} items")


ft_inventory_system()
