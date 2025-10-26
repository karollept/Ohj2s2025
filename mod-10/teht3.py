#Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys,
# joka käskee kaikki hissit pohjakerrokseen.
#Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

from classes.Talo import house

house1 = house(3)

#house1.aja_hissia(2,5)
#house1.aja_hissia(3,7)
#house1.aja_hissia(1,8)
house1.palohalytys()
