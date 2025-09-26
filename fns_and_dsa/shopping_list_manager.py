shopping_list = []
def add_item(item):
    shopping_list.append(item)
    return shopping_list

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
    return shopping_list

def view_items():
    return shopping_list
def main(menu):
    while True:
        if menu == 'add':
            item = input("Enter the item name: ")
            shopping_list.append(item)
        elif menu == 'remove':
            item = input("Enter the item name: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print(f"{item} not found in the shopping list.")
        elif menu == 'view':
            for idx, item in enumerate(shopping_list, start=1):
                print(f"{idx}. {item}")
        else:
            print("Invalid menu option. Please choose 'add', 'remove', or 'view'.")