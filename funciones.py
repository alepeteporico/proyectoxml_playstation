def ej1(datos):
    sobremesas=(datos.xpath("//Consoles/Console/@id"))
    portables=(datos.xpath("wiki/Handhelds/Console/@id"))
    return sobremesas,portables