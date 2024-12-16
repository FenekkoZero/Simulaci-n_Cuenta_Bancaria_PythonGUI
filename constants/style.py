home_backg="#FFF4B0" #Defino un color de fondo global


#Defino variables para cargar en el estilo de texto de los objetos
# que inserte con TKinter
GLOBAL_FONT= ("Arial", 15)
GLOBAL_COMP_COLOR = "#B64C0E"
GLOBAL_TEXT_COLOR = home_backg

text_style = {
    "font": GLOBAL_FONT,
    "bg": GLOBAL_COMP_COLOR,
    "fg": GLOBAL_TEXT_COLOR,
}


SALDO_FONT= ("Arial", 20, "bold")
SALDO_TEXT_COLOR = "#B64C0E"

text_saldo = {
    "font": SALDO_FONT,
    "bg": home_backg,
    "fg": SALDO_TEXT_COLOR
}