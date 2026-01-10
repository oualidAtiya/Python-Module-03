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
            },
            "dddddd": {
                "category": "armor",
                "type": "uncommon",
                "quantity": 1,
                "values": 200
            }
        }

}

inventories['alice'].get("sword").update({"category": "value"})
print(inventories['alice'])

categories = {}
categories['waepon']
