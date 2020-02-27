def ej1(datos):
    sobremesas=(datos.xpath("//Consoles/Console/@id"))
    portables=(datos.xpath("//Handhelds/Console/@id"))
    return sobremesas,portables

def ej1_2(datos,consola):
    juegos=(datos.xpath('//Console[@id="%s"]/games/game/text()'%consola))
    return juegos