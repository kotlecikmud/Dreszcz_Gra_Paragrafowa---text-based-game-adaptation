def gb_update(language='pl'):
    if language == 'en':
        gameboook = {
            "00a": "\rWhile wandering through the underground, you will find different types of weapons and items. \
                            \nRemember that - except for the sword - each weapon can be used only once. \
                            \nSimilarly, the found items are for single use. \
                            \nYou can take one bottle of elixir with you.",
            "00b": "Hey, Brave One! \
                            \n \
                            \nThey say about you that icy water flows in your veins instead of blood, \
                            \nand your muscles are made of the noblest steel? \
                            \nIf so, look towards the setting sun. \
                            \nThere, at the borders of the kingdom of Almanhagor, the uncharted Underground begins. \
                            \nOnly you can unveil its Great Secret. Go forth!",
            "01": "The entrance to the underground is wide, overgrown with grass and lush bushes. \
                            \nYou adjust your clothing and equipment. \
                            \nLight your lantern! You enter the corridor. It is tall, and you don't have to stoop. \
                            \nIt leads straight to the north. Soon, you reach a crossroads. \
                            \nIt has the shape of the letter T. The branches lead west, east, and south (where you came from)."
        }

    if language == 'pl':
        gameboook ={
            "00a": "\rPodczas wędrówki podziemiem znajdziesz różne rodzaje broni i przedmiotów. \nPamiętaj, że - oprócz miecza - każda broń można użyć tylko raz. \nPodobnie znalezione przedmioty są przeznaczone do jednorazowego użycia. \nMożesz zabrać ze sobą jedną butelkę eliksiru.",
            "00b": "Hej, Waleczny! \n\nMówią o tobie, że w twoich żyłach płynie lodowata woda zamiast krwi, \na twoje mięśnie są z najszlachetniejszej stali? \nJeśli tak, spojrzyj w kierunku zachodzącego słońca. \nTam, na granicach królestwa Almanhagor, zaczyna się niezbadane Podziemie. \nTylko ty możesz odkryć jego Wielką Tajemnicę. Wyruszaj!",
            "01": "Wejście do podziemia jest szerokie, porośnięte trawą i bujnymi krzewami. \nDopasowujesz swoje ubranie i wyposażenie. \nZapal latarnię! Wchodzisz do korytarza. Jest wysoki, nie musisz się schylać. \nProwadzi prosto na północ. Wkrótce docierasz do skrzyżowania. \nMa kształt litery T. Gałęzie prowadzą na zachód, wschód i na południe (skąd przybyłeś)."
        }

    return gameboook

# print every value in dictionary
