def ej1(datos):
    sobremesas=(datos.xpath("wiki/Consoles"))
    portables=(datos.xpath("wiki/Handhelds"))
    return sobremesas,portables