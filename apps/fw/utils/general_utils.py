def title_case(objeto: object, atributo: str) -> str | None:
    return (
        objeto.get(atributo).title()
        if objeto.get(atributo) != None
        else objeto.get(atributo)
    )


def row_to_title_case(row):
    try:
        row["NOMBRES"] = row["NOMBRES"].title()
        row["APELLIDOS"] = row["APELLIDOS"].title()
        row["NACIONALIDAD"] = row["NACIONALIDAD"].title()
    except Exception as e:
        print(e)
