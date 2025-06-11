from person_class_created import Person 


granbois_7 = Person("Eugénie Granbois", born = 1838, died = 1907)
baquié_47 = Person("Ferdinand Baquié", born = 1837, died = 1883)
baquié_46 = Person("Louise Baquié", mom=granbois_7, dad=baquié_47, born = 1868, died = 1945)
ramos_1459 = Person("Marie Ramos", born = 1826, died = 1904)
martinez_8709 = Person("Jacques Martinez", born = 1822, died = 1891)
martinez_8708 = Person("Joseph Martinez", mom=ramos_1459, dad=martinez_8709, born = 1864, died = 1928)
martinez_9931 = Person("Adele Martinez", mom=ramos_1459, dad=martinez_8709, born = 1860)
martinez_9927 = Person("Mildred Martinez", mom=baquié_46, dad=martinez_8708, born = 1911, died = 1990)
prevost_1179 = Person("Jeanne Prevost")
fontaine_2773 = Person("Ernest Fontaine", born = 1857, died = 1919)
fontaine_2776 = Person("Suzanne Fontaine", mom=prevost_1179, dad=fontaine_2773, born = 1894, died = 1979)
fontaine_2783 = Person("Andre Louis Fontaine", mom=prevost_1179, dad=fontaine_2773, born = 1888)
fontaine_2784 = Person("Henry Eugene Fontaine", mom=prevost_1179, dad=fontaine_2773, born = 1891, died=1954)
alioto_37 = Person("Maria Alioto", born = 1834, died = 1908)
riggitano_1 = Person("Santo Riggitano", born = 1824, died = 1989)
riggitano_2 = Person("Salvatore Riggitano", mom=alioto_37, dad=riggitano_1, born = 1876, died = 1960 )
prevost_1164 = Person("John Prevost", mom = fontaine_2776, dad = riggitano_2, born = 1917, died = 1996)
prevost_1163 = Person("Louis Prevost", mom=fontaine_2776, dad=riggitano_2, born = 1920, died = 1997)
prevost_1162 = Person("Robert Prevost", mom=martinez_9927, dad=prevost_1163, born = 1955)

grace_1 = Person("Amanda Grace")
butcher_3 = Person("Paul Butcher")
munsil_2 = Person("Wesley Munsil")
hodge_1 = Person("Jane Hodge")
munsil_1 = Person("Angela Munsil", mom=grace_1, dad=munsil_2, born = 1977, died = "alive")
butcher_2 = Person("Matthew Butcher", mom=hodge_1, dad=butcher_3, born= 1977, died = "alive")
butcher_5 = Person("Katherine Butcher", mom=munsil_1, dad=butcher_2, born = 2007, died = "alive")
butcher_4 = Person("Annabelle Butcher", mom=munsil_1, dad=butcher_2, born = 2001, died = "alive")
butcher_1 = Person("Claire Butcher", mom=munsil_1, dad =butcher_2, born= 2004, died = "alive")


butcher_1.print_family_tree()




