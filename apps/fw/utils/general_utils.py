def title_case(objeto: object, atributo: str) -> str | None:
    return (
        objeto.get(atributo).title()
        if objeto.get(atributo) != None
        else objeto.get(atributo)
    )
