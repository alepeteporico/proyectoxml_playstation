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
    consolas=[]
    years=(datos.xpath("//date/year/text()"))
    for year in years:
        if fecha>year:
            consolas.append(datos.xpath('//Console/date[year="%s"]/../Console/@id'%year))
    return consolas