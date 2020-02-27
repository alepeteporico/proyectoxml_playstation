def ej1(datos):
    sobremesas=(datos.xpath("//Consoles/Console/@id"))
    portables=(datos.xpath("//Handhelds/Console/@id"))
    return sobremesas,portables

def ej1_2(datos,consola):
    juegos=(datos.xpath('//Console[@id="%s"]/games/game/text()'%consola))
    return juegos

def ej2(datos,consola):
    total=len((datos.xpath('//Console[@id="%s"]/games/game/text()'%consola)))
    exclusivos=len((datos.xpath('//Console[@id="%s"]/games/game/@tipo'%consola)))
    return total,exclusivos

def convertir_fecha(fecha):
    dia=fecha.split("/")[0]
    mes=fecha.split("/")[1]
    year=fecha.split("/")[2]

def ej3(datos):
    