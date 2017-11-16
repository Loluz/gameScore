class HtmlGenerator:
    def pagina(self):
        html = ""
        for i in range(0, 10):
            html += str(i)
        < !DOCTYPE
        html >
        < html >

        < head >
        < link
        rel = "stylesheet"
        type = "text/css"
        href = "index.css" >
        < meta
        charset = "utf-8" >
        < meta
        name = "CriminalDirectory"
        content = "width=device-width" >
        < title > Busqueda
        Antecedentes < / title >
        < / head >

        < body >
        < table
        style = "width: 990px; text-align: left; margin-left: auto; margin-right: auto;"
        border = "0" >
        < tbody >
        < tr
        align = "center" > < td
        colspan = "2"
        align = "center" >
        < table
        align = "center"
        border = "0"
        cellpadding = "0"
        cellspacing = "0"
        width = "990" >
        < tbody >
        < tr
        align = "center" > < td
        align = "left"
        bgcolor = "E79D00"
        width = "12" > & nbsp; < / td >
        < td
        align = "left"
        bgcolor = "E79D00"
        width = "7024" >
        < font

        class ="Estilo1" face="Verdana, Geneva, sans-serif" >

        < / font > < / td > < / tr >
        < tr >
        < th
        colspan = "3"
        scope = "col"
        align = "center"
        height = "100" >
        < div
        id = "j_idt7_content"

        class ="ui-panel-content ui-widget-content" > < span style="font-weight: bold; font-size: 18px;" >

        < img
        src = "./files/banner-web-amarillo.jpg"
        title = "Criminal Directory"
        align = "middle" >
        < div
        id = "Layer1"
        align = "center" >
        < table
        bgcolor = "F9C30B"
        border = "0"
        width = "998" >
        < / div >
        < div

        class ="absoluto" >

        < img
        src = "https://image.freepik.com/iconos-gratis/logo-fishofish_318-52716.jpg"
        width = "120"
        height = "160" >
        < / div >

< tbody >
< tr > < td
width = "1098" >
< ul
id = "MenuBar1"


class ="MenuBarHorizontal" >

< li >
< a
href = "/WebJudicial"
title = "Inicio" >
< strong > Inicio < / strong >
< / a >
< / li >
< li >
< a
href = "http://www.policia.gov.co/"
title = "Busqueda de personas"


class ="MenuBarItemSubmenu" >

< strong > Busqueda
de
personas < / strong >
< / a >
< / li >
< li >
< a
href = "http://www.policia.gov.co/portal/page/portal/Noticias_y_Documentacion/Medios_Comunicacion_Institucionales/Contactos_CE"
title = "Contáctenos" >
< strong > Contáctenos < / strong >
< / a >
< / li >
< / ul >
< / td >
< / tr >
< / tbody >
< / table >
< / div >
< / th >
< / tr >
< / tbody >
< / table >
< / td >
< / tr >
< tr >
< td
style = "width: 40%; text-align: center; vertical-align: top; margin-left: auto; margin-right: auto;" >
< form
id = "form"
name = "form"
method = "post"
action = "/WebJudicial/index.xhtml;jsessionid=Ln3KhH6SkWsNQGB23pjyy5L1Mxkc1nXsx02Tj011x1C9g8pXhSwy!-1895617418"
enctype = "application/x-www-form-urlencoded" >
< input
type = "hidden"
name = "form"
value = "form" >
< div
id = "j_idt7"


class ="ui-panel ui-widget ui-widget-content ui-corner-all" style="min-height: 300px;" > < div id="j_idt7_content" class ="ui-panel-content ui-widget-content" > < span style="font-weight: bold; font-size: 17px;" > Bienvenido a la consulta de Antecedentes Judiciales < / span >

< br > < br > < div
id = "j_idt10"


class ="ui-messages ui-widget" > < / div > < table style="margin-left: auto; margin-right: auto;" >

< table
cellpadding = 0
cellspacing = 0
border = 0 >
< tr >
< td
style = "font-family: Arial, Helvetica, sans-serif; font-size: 20pt; width: 40%; text-align: center; vertical-align: top; margin-left: auto; margin-right: auto;" >
< form
style = "margin:0px; margin-top:4px;"
action = "http://search.freefind.com/find.html"
method = "get"
accept - charset = "utf-8"
target = "_self" >
< input
type = "hidden"
name = "si"
value = "47091246" >
< input
type = "hidden"
name = "pid"
value = "r" >
< input
type = "hidden"
name = "_charset_"
value = "" >
< input
type = "hidden"
name = "bcd"
value = "&#247;" >
< center >
< input
type = "text"
name = "query"
size = "50" >
< input
type = "submit"
value = "Buscar" >
< / form >
< / table >

< / body >
< / html >


return html


def createList(self):
    list = "<ol>"
    for i in range(0, 10):
        list += "<li>" + str(i) + "</li>"
    list += "</ol>"

    return list
