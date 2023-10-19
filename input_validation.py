import re


def validate(type, input, min_length, max_length):
    type_names = {
        "username": "Käyttäjätunnuksen",
        "password": "Salasanan",
        "message": "Viestin",
        "project_name": "Projektin nimen",
        "name": "Nimen",
        "role": "Roolin",
    }
    type_name = type_names[type]
    if len(input) < min_length:
        return False, f"{type_name} on oltava vähintään {min_length} merkkiä pitkä."
    elif len(input) > max_length:
        return False, f"{type_name} saa olla enintään {max_length} merkkiä pitkä."
    elif (type == "username" or type == "password") and not re.match(
        "^[a-zA-Z0-9]*$", input
    ):
        return (
            False,
            f"{type_name} ainoita sallittuja merkkejä ovat kirjaimet ja numerot.",
        )
    return True
