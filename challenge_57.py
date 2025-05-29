"""create a function to get an item into a strings list"""


values: list[str] = ["Julien", "Marie", "Pierre"]



def get_item(items: list[str], index: int) -> str:
    try:
        return items[index]
    except IndexError:
        return f"Index {index} hors de la liste"



if __name__ == "__main__":
    print(get_item(values, 0))
    print(get_item(values, 5))
    print(get_item(values, -13))
