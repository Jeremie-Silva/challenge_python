"""Retrieve date of birth based en age and birth_month"""


from datetime import datetime


age: int = 25
mois_de_naissance: int = 10


def calculate_year_of_birth(age: int, birth_month: int) -> datetime:
    current_year: int = datetime.now().year
    return datetime.now().replace(year=current_year - age, month=birth_month)


if __name__ == "__main__":
    result: datetime = calculate_year_of_birth(age=age, birth_month=mois_de_naissance)
    print(result)
