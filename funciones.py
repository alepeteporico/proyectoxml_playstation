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

def ej3(datos,fecha):
    consolas=(datos.xpath('//date[year/text()<"%s"]/../@id'%fecha))
    return consolas

def ej4(datos,juego):
    consola=(datos.xpath('//games[game/text()="%s"]/../@id'%juego))[0]
    precio=float((datos.xpath('//Console[@id="%s"]/price/text()'%consola))[0])
    return consola,precio