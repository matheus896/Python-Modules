import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in args:
        if ':' not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        name, qty_str = arg.split(':', 1)
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            qty = int(qty_str)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
            continue
        inventory[name] = qty
    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = parse_inventory(sys.argv[1:])
    print(f"Got inventory: {inventory}")
    items = list(inventory.keys())
    print(f"Item list: {items}")
    total = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total}")
    for name in inventory.keys():
        pct = round(inventory[name] / total * 100, 1)
        print(f"Item {name} represents {pct}%")
    most = items[0] if items else ""
    least = items[0] if items else ""
    for name in items:
        if inventory[name] > inventory[most]:
            most = name
        if inventory[name] < inventory[least]:
            least = name
    if items:
        print(f"Item most abundant: {most} with quantity {inventory[most]}")
        print(f"Item least abundant: {least} with quantity {inventory[least]}")
    inventory.update({'magic_item': 1})
    print(f"Updated inventory: {inventory}")


main()
