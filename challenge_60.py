"""Recreate an alternative to dict.get built-in function"""


def custom_get(d: dict, default: str, *keys):
    for key in keys:
        try:
            d = d[key]
        except KeyError:
            return default
    return d



if __name__ == "__main__":
    values_1: dict = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}
    result_1: str = custom_get(values_1, "valeur inconnue", *["01", "identite", "prenom"])
    print(result_1)

    values_2: dict = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}
    result_2: str = custom_get(values_2, "valeur inconnue", *["01", "identite", "numéro_de_carte_bleu"])
    print(result_2)
