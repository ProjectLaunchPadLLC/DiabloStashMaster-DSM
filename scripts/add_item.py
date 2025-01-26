import json
import os
from utils import load_items, save_items, generate_item_hash

def get_user_input(prompt, type=str, required=True):
    """Gets user input with validation."""
    while True:
        try:
            user_input = input(prompt)
            if not user_input and not required:
                return None
            if user_input == "?":
                print_valid_inputs()
                continue
            return type(user_input)
        except ValueError:
            print(f"Invalid input. Please enter a valid {type.__name__}.")

def print_valid_inputs():
    """Prints valid inputs for each field."""
    print("Valid inputs for each field:")
    print("  Item Name: (text)")
    print("  Item Type: (text)")
    print("  Item Power: (integer)")
    print("  Armor: (float, optional)")
    print("  Intelligence: (float, optional)")
    print("  Critical Strike Chance: (float, optional)")
    print("  Unique/Legendary Power: (text, optional)")
    print("  Required Level: (integer, optional)")
    print("  Sell Value: (integer, optional)")
    print("  Tempers: (text, optional)")
    print("  Notes: (text, optional)")
    print("  Best Build For: (text, optional)")
    print("  Resistance to All: (float, optional)")
    print("  Damage Reduction: (text, optional)")
    print("  Resource Increase: (integer, optional)")
    print("  Cooldown Reduction: (float, optional)")
    print("  Lucky Hit Chance to Heal: (float or text, optional)")
    print("  Resource Cost Reduction: (float, optional)")
    print("  Movement Speed: (float, optional)")
    print("  Socket: (boolean, optional. true/false)")
    print("  Damage Over Time: (float, optional)")
    print("Enter '?' for help on valid inputs.")


def add_item():
    """Prompts the user to enter item details and adds the item to items.json."""
    item_data = {}

    fields = {
        "Item Name": (str, True),
        "Item Type": (str, True),
        "Item Power": (int, True),
        "Armor": (float, False),
        "Intelligence": (float, False),
        "Critical Strike Chance": (float, False),
        "Unique/Legendary Power": (str, False),
        "Required Level": (int, False),
        "Sell Value": (int, False),
        "Tempers": (str, False),
        "Notes": (str, False),
        "Best Build For": (str, False),
        "Resistance to All": (float, False),
        "Damage Reduction": (str, False),
        "Resource Increase": (int, False),
        "Cooldown Reduction": (float, False),
        "Lucky Hit Chance to Heal": (str, False),
        "Resource Cost Reduction": (float, False),
        "Movement Speed": (float, False),
        "Socket": (bool, False),
        "Damage Over Time": (float, False)
    }

    for field, (type, required) in fields.items():
        prompt = f"Enter {field}" + (f" (or leave blank): " if not required else ": ")
        item_data[field] = get_user_input(prompt, type, required)

    # Generate hash and add it to item data
    item_hash = generate_item_hash(item_data)
    item_data["Hash"] = item_hash

    # Add item to items.json
    items = load_items()
    items.append(item_data)
    save_items(items)

    print(f"Item '{item_data['Item Name']}' added successfully with hash: {item_hash}")

if __name__ == "__main__":
    add_item()
