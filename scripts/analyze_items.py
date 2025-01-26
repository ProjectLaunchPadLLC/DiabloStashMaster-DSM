from utils import load_items

def analyze_items(build_type=None):
    """Analyzes items, optionally filtering by build type."""
    items = load_items()

    if build_type:
        items = [item for item in items if build_type.lower() in item.get("Best Build For", "").lower()]

    if not items:
        print("No items found for the specified build type.")
        return

    print(f"Analyzing items", f" for build: {build_type}" if build_type else "", ":\n")
    for item in items:
        print(f"Item Name: {item['Item Name']}")
        print(f"Item Type: {item['Item Type']}")
        print(f"Item Power: {item['Item Power']}")
        if item.get('Armor'):
            print(f"Armor: {item['Armor']}")
        if item.get('Intelligence'):
            print(f"Intelligence: {item['Intelligence']}")
        if item.get('Critical Strike Chance'):
            print(f"Critical Strike Chance: {item['Critical Strike Chance']}")
        if item.get('Required Level'):
            print(f"Required Level: {item['Required Level']}")
        if item.get('Sell Value'):
            print(f"Sell Value: {item['Sell Value']}")
        if item.get('Tempers'):
            print(f"Tempers: {item['Tempers']}")
        if item.get('Resistance to All'):
            print(f"Resistance to All: {item['Resistance to All']}")
        if item.get("Unique/Legendary Power"):
            print(f"Unique/Legendary Power: {item['Unique/Legendary Power']}")
        if item.get('Damage Reduction'):
            print(f"Damage Reduction: {item['Damage Reduction']}")
        if item.get('Resource Increase'):
            print(f"Resource Increase: {item['Resource Increase']}")
        if item.get('Cooldown Reduction'):
            print(f"Cooldown Reduction: {item['Cooldown Reduction']}")
        if item.get('Lucky Hit Chance to Heal'):
            print(f"Lucky Hit Chance to Heal: {item['Lucky Hit Chance to Heal']}")
        if item.get("Resource Cost Reduction"):
            print(f"Resource Cost Reduction: {item['Resource Cost Reduction']}")
        if item.get("Movement Speed"):
            print(f"Movement Speed: {item['Movement Speed']}")
        if item.get("Socket"):
            print(f"Socket: {item['Socket']}")
        if item.get("Damage Over Time"):
            print(f"Damage Over Time: {item['Damage Over Time']}")

        print(f"Hash: {item['Hash']}")
        if item.get("Notes"):
            print(f"Notes: {item['Notes']}")
        print("-" * 20)

if __name__ == "__main__":
    build_type_input = input("Enter build type to filter by (or leave blank for all items): ")
    analyze_items(build_type_input)
