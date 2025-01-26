from utils import load_items

def compare_items(item_name1, item_name2):
    """Compares two items by name."""
    items = load_items()
    item1 = next((item for item in items if item["Item Name"] == item_name1), None)
    item2 = next((item for item in items if item["Item Name"] == item_name2), None)

    if not item1 or not item2:
        print("One or both items not found.")
        return

    print(f"Comparing {item_name1} and {item_name2}:\n")
    for key in item1:  # Assuming both items have the same keys
        if key not in ["Notes", "Unique/Legendary Power", "Hash"]: # Handle these separately
            value1 = item1[key]
            value2 = item2[key]

            print(f"{key}:")
            print(f"  {item_name1}: {value1}")
            print(f"  {item_name2}: {value2}")

            # Add basic comparison logic here, e.g.:
            if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
                if value1 > value2:
                    print(f"    {item_name1} has a higher value.")
                elif value2 > value1:
                    print(f"    {item_name2} has a higher value.")
                else:
                    print(f"    Both items have the same value.")
            print()
        elif key == "Unique/Legendary Power":
            print(f"{key}:")
            print(f"  {item_name1}: {item1[key]}")
            print(f"  {item_name2}: {item2[key]}")
            print()
        elif key == "Hash":
            print(f"{key}:")
            print(f"  {item_name1}: {item1[key]}")
            print(f"  {item_name2}: {item2[key]}")
            if item1[key] == item2[key]:
                print("    Both items have the same hash, indicating they are likely the same item.")
            else:
                print("    The items have different hashes, indicating they are different items.")
            print()
        elif key == "Notes":
            if item1[key] or item2[key]:
                print(f"{key}:")
                if item1[key]:
                    print(f"  {item_name1}: {item1[key]}")
                if item2[key]:
                    print(f"  {item_name2}: {item2[key]}")
                print()

if __name__ == "__main__":
    item1_name = input("Enter the name of the first item: ")
    item2_name = input("Enter the name of the second item: ")
    compare_items(item1_name, item2_name)
