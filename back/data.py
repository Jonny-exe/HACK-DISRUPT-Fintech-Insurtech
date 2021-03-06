#
# CO2 Emission Data
#


# Food choices / nutrition:
# 1.7 US tons = 1,542.21406 kilograms of CO2/year - vegetarian.
# 2.5 US tons = 2,267.96185 kilograms of CO2/year - average. 6.21359410958904 kg/day per person, 2.07kg CO2/meal at 3 meals per day,
# 3.3 US tons = 2,993.70964 kilograms of CO2/year - meat lover.

food_exact = {
    "Average": 2.07, # average meal
    "Pan": 1.4,
    "Maiz": 1.1,
    "Cerveza": 1.1,
    "Avena": 1.6,
    "Arroz": 4.0,
    "Patatas": 0.3,
    "Mandioca": 0.9,
    "Caña de azucar": 2.6,
    "Azúcar de remolacha": 1.4,
    "Chícharos": 0.8,
    "Nueces": 0.2,
    "Cacahuetes": 2.4,
    "Leche de soja": 1.0,
    "Tofu": 3.0,
    "Aceite de soja": 6.0,
    "Aceite de palma": 7.6,
    "Aceite de girasol": 3.5,
    "Aceite de colza": 3.7,
    "Aceite de oliva": 6.0,
    "Tomates": 1.4,
    "Cebollas y puerros": 0.3,
    "Vegetales de raíz": 0.3,
    "Verduras": 0.5,
    "Limón": 0.3,
    "Naranjas": 0.3,
    "Plátanos": 0.8,
    "Manzanas": 0.3,
    "Bayas": 1.1,
    "Uvas": 1.1,
    "Vino": 1.4,
    "Fruta": 0.7,
    "Café": 16.5,
    "Chocolate negro": 18.7,
    "Carne de vaca": 59.6,
    "Cordero": 24.5,
    "Cerdo": 7.2,
    "pollo": 6.1,
    "Leche": 2.8,
    "Queso": 21.2,
    "Huevos": 4.5,
    "Pescado": 5.1,
    "Camarones": 11.8
}

food = [
    "comida",
    "amaranto",
    "arroz",
    "avena",
    "tortillas",
    "pan integral",
    "fideos",
    "pasta",
    "cereales",
    "buñuelos",
    "muffins",
    "tortillas",
    "churros",
    "pan blanco",
    "pan dulce",
    "cereales",
    "bolillos",
    "maracuyá",
    "arepas",
    "bananos",
    "chirimoya",
    "durazno",
    "fresas",
    "granadilla",
    "guayaba",
    "limón",
    "mango",
    "manzana",
    "melón",
    "naranja",
    "nectarina",
    "papaya",
    "pasas",
    "pera",
    "piña",
    "uva",
    "zapote",
    "aguacate",
    "coco",
    "berenjena",
    "brécol",
    "brocoli",
    "camote",
    "cebolla",
    "chayote",
    "espárrago",
    "hongos",
    "jícama",
    "lechuga",
    "maíz",
    "malanga",
    "nopales",
    "pana",
    "papas",
    "pepino",
    "pimentón",
    "plátanos",
    "repollo",
    "tomate",
    "tomatillo",
    "yautía",
    "yuca",
    "zanahoria",
    "tofu",
    "pavo",
    "pollo",
    "pescado",
    "mariscos",
    "huevos",
    "mantequilla",
    "nueces",
    "chorizo",
    "menudo",
    "res",
    "puerco",
    "margarina",
    "aceite",
    "manteca",
    "olivas",
    "aceitunas",
    "salsa",
    "aguacate",
    "mantequilla",
    "crema",
    "queso",
]

#
#
#
restaurants_exact = {
    "Average": 2.07, # average meal
}


restaurants = [
    "restaurante",
    "bar",
    "Applebee's",
    "Arby's",
    "Auntie Anne's",
    "Baton Rouge",
    "BeaverTails",
    "Big Smoke Burger",
    "Bonchon Chicken",
    "Buffalo Wild Wings",
    "Burger King",
    "Cafe Coffee Day",
    "Carl's Jr.",
    "Charleys Philly Steaks",
    "Chick-Fil-A",
    "Chili's",
    "Chipotle Mexican Grill",
    "Church's Chicken",
    "Cora",
    "Costa Coffee",
    "Crepes & Waffles",
    "Dairy Queen",
    "Délifrance",
    "Denny's",
    "Dôme",
    "Din Tai Fung",
    "Domino's Pizza",
    "Dunkin' Donuts",
    "Earls Kitchen + Bar",
    "East Side Mario's",
    "Five Guys",
    "Freshly Chopped",
    "Gloria Jean's Coffees",
    "Hamburguesas El Corral",
    "Hard Rock Cafe",
    "Hardee's",
    "Harvey's",
    "Hooters",
    "IHOP",
    "Jack Astor's Bar and Grill",
    "Jack in the Box",
    "Jimmy John's",
    "Joe & The Juice",
    "Jollibee",
    "Juan Valdez Cafe",
    "The Keg",
    "Kenny Rogers Roasters",
    "KFC",
    "Krispy Kreme",
    "Little Caesars",
    "Long John Silver's",
    "Loving Hut",
    "Marrybrown",
    "McDonald's",
    "McDonalds",
    "MK Restaurant",
    "MOS Burger",
    "Nando's",
    "Olive Garden",
    "Outback Steakhouse",
    "Panda Express",
    "Panera Bread",
    "Papa John's Pizza",
    "Paris Baguette",
    "Perkins Restaurant and Bakery",
    "PizzaExpress",
    "The Pizza Company",
    "Pizza Hut",
    "Planet Hollywood",
    "Pollo Campero",
    "Ponderosa and Bonanza Steakhouses",
    "Popeyes",
    "Quiznos",
    "Rainforest Cafe",
    "Red Lobster",
    "Red Robin",
    "Ruby Tuesday",
    "Secret Recipe",
    "Shakey's Pizza",
    "Sizzler",
    "Sonic Drive-In",
    "Starbucks",
    "Steak 'n Shake",
    "Subway",
    "Swensen's",
    "TGI Friday's",
    "Taco Bell",
    "Telepizza",
    "Tim Hortons",
    "Tony Roma's",
    "Waffle House",
    "Wendy's",
    "Wendys",
    "Whataburger",
    "White Castle",
    "Yoshinoya",
]

#
#
#
# flights, vuelos
# average domestic commercial flight emitted 0.39 pounds of CO2e per passenger mile, 0.39*0.45359237/1.609344 == 0.109921200377297 kg CO2 per passenger flight km
transport_aereo_exact = {
    "Average" : 0.11*1000, # average distance of flight: 1000km, STD FLIGHT
    "vuelo": 0.11*1000, # average distance of flight: 1000km
    "vuelo national": 0.11*500, # average distance of flight: 500km
    "vuelo international": 0.11*2000, # average distance of flight: 2000km
    "MAD-BCN": 0.11*500, # distance of flight: 500km
    "BCN-MAD": 0.11*500, # distance of flight: 500km
    "MAD-BIO": 0.11*400, # distance of flight: 400km
    "BIO-MAD": 0.11*400, # distance of flight: 400km
}

# various air lines
transport_aereo = [
    "Aegean Airlines",
    "Aer Lingus",
    "Aeroflot",
    "Aerolineas Argentinas",
    "Aeromexico",
    "Air Arabia",
    "Air Astana",
    "Air Austral",
    "Air Baltic",
    "Air Belgium",
    "Air Canada",
    "Air Caraibes",
    "Air China",
    "Air Corsica",
    "Air Dolomiti",
    "Air Europa",
    "Air France",
    "Air India",
    "Air India Express",
    "Air Macau",
    "Air Malta",
    "Air Mauritius",
    "Air Namibia",
    "Air New Zealand",
    "Air North",
    "Air Seoul",
    "Air Serbia",
    "Air Tahiti Nui",
    "Air Transat",
    "Air Vanuatu",
    "AirAsia",
    "AirAsia X",
    "Aircalin",
    "Alaska Airlines",
    "Alitalia",
    "Allegiant",
    "American Airlines",
    "ANA",
    "Asiana",
    "Austrian",
    "Avianca",
    "Azerbaijan Hava Yollary",
    "Azores Airlines",
    "Azul",
    "Bamboo Airways",
    "Bangkok Airways",
    "British Airways",
    "Brussels Airlines",
    "Caribbean Airlines",
    "Cathay Dragon",
    "Cathay Pacific",
    "Cayman Airways",
    "CEBU Pacific Air",
    "China Airlines",
    "China Eastern",
    "China Southern",
    "Condor",
    "Copa Airlines",
    "Croatia Airlines",
    "Czech Airlines",
    "Delta",
    "easyJet",
    "Edelweiss Air",
    "Egyptair",
    "EL AL",
    "Emirates",
    "Ethiopian Airlines",
    "Etihad",
    "Eurowings",
    "EVA Air",
    "Fiji Airways",
    "Finnair",
    "flydubai",
    "FlyOne",
    "French bee",
    "Frontier",
    "Garuda Indonesia",
    "Gol",
    "Gulf Air",
    "Hainan Airlines",
    "Hawaiian Airlines",
    "Helvetic Airways",
    "HK Express",
    "Hong Kong Airlines",
    "Iberia",
    "Icelandair",
    "IndiGo Airlines",
    "InterJet",
    "Japan Airlines",
    "Jeju Air",
    "Jet2",
    "JetBlue",
    "Jetstar",
    "Jin Air",
    "Kenya Airways",
    "KLM",
    "Korean Air",
    "Kulula",
    "La Compagnie",
    "LATAM",
    "Lion Airlines",
    "LOT Polish Airlines",
    "Lufthansa",
    "Luxair",
    "Malaysia Airlines",
    "Mango",
    "Middle East Airlines",
    "Nok Air",
    "Nordwind Airlines",
    "Norwegian Air International",
    "Norwegian Air Shuttle",
    "Norwegian Air Sweden",
    "Norwegian Air UK",
    "Oman Air",
    "Pakistan International Airlines",
    "Peach",
    "Pegasus Airlines",
    "Philippine Airlines",
    "Porter",
    "Qantas",
    "Qatar Airways",
    "Regional Express",
    "Rossiya - Russian Airlines",
    "Royal Air Maroc",
    "Royal Brunei",
    "Royal Jordanian",
    "RwandAir",
    "Ryanair",
    "S7 Airlines",
    "SAS",
    "Saudia",
    "Scoot Airlines",
    "Shanghai Airlines",
    "Silkair",
    "Silver",
    "Singapore Airlines",
    "Skylanes",
    "South African Airways",
    "Southwest",
    "SpiceJet",
    "SpanAir",
    "Spirit",
    "Spring Airlines",
    "Spring Japan",
    "SriLankan Airlines",
    "Sun Country",
    "Sunclass Airlines",
    "Sunwing",
    "SWISS",
    "Swoop",
    "TAAG",
    "TACA",
    "TAP Portugal",
    "THAI",
    "tigerair Australia",
    "Transavia Airlines",
    "TUI UK",
    "TUIfly",
    "Tunis Air",
    "Turkish Airlines",
    "Ukraine International",
    "United",
    "Ural Airlines",
    "UTair Aviation",
    "Uzbekistan Airways",
    "Vietnam Airlines",
    "Virgin Atlantic",
    "Virgin Australia",
    "Vistara",
    "Viva Aerobus",
    "Volaris",
    "Volotea",
    "Vueling Airlines",
    "WestJet",
    "Wizzair",
    "Xiamen Airlines",
]

#
#
# all transportation except air transporation
transport_exact = {
    "Average" : 0.22*30,  # most typical transport is car, so we use car data, average 30km per trip
    #
    #
    #
    # Transport: Total_emissions: kg CO2 per meaningful unit of distance
    "gasolina": 2.348*25, # Gasoline releases 19.6 pounds of CO2 per gallon when burned, 19.6/3.785411784*0.45359237 == 2.34859797541117 kg CO2 per 1l gasoline, average tank filling 25l
    "diesel": 2.684*25, # Gasoline releases 22.4 pounds of CO2 per gallon when burned, 22.4/3.785411784*0.45359237 == 2.68411197189848 kg CO2 per 1l gasoline, average tank filling 25l
    # gasolineras
    "Repsol": 2.5*25, # gasolina
    "Cepsa": 2.5*25, # gasolina
    "Galp": 2.5*25, # gasolina
    "Ballenoil": 2.5*25, # gasolina
    "Avia": 2.5*25, # gasolina
    "Shell": 2.5*25, # gasolina
    "BP": 2.5*25, # gasolina
    "FastFuel": 2.5*25, # gasolina
    "Nafte": 2.5*25, # gasolina

    #
    #
    #
    # viajes en taxi, etc
    # The average passenger car emits 0.78 pounds of CO2 per mile driven. 0.78*0.45359237/1.609344 == 0.219842400754593 kg CO2 per 1km driven
    "taxi": 0.22*10, # average trip length 10km
    "Uber": 0.22*10, # average trip length 10km
    "Lyft": 0.22*10, # average trip length 10km
    "Rideshare": 0.22*10, # average trip length 10km
    "BlaBlaCar": 0.22*10, # average trip length 10km
    "BlaBlaBus": 0.22*10, # average trip length 10km

    #
    #
    #
    # According to US EPA (2015):
    # Intercity rail (i.e., Amtrak) generates 0.14 kg CO2/passenger-mile
    # Commuter rail generates 0.17 kg CO2/passenger-mile
    # Transit rail (i.e., subway, metro, tram) generates 0.12 kg CO2/passenger-mile, 0.12/1.609344 == 0.07456454306848 kg CO2 per 1km train ride
    # Bus generates 0.06 kg CO2/passenger-mile
    # public transport, metro, tramvia, bus
    # 0.161 kg of CO2 per mile (public transportation), 0.161/1.609344 == 0.1 kg CO2 per 1km public transport
    "Bilbobus": 0.1*10, # 10km average distance
    "Tramvia": 0.1*10, # 10km average distance
    "metro": 0.1*10, # 10km average distance
    "bus": 0.1*10, # 10km average distance
    "tren": 0.0745*100, # 100km average distance
}

transport = [
    "barco",
    "coche",
    "abarth",
    "acura",
    "integra",
    "legend",
    "alfa romeo",
    "brera",
    "giulietta",
    "milano",
    "mito",
    "spider",
    "alpina",
    "american motors",
    "javelin",
    "pacer",
    "rebel",
    "aston martin",
    "audi",
    "allroad quattro",
    "cabriolet",
    "coupe",
    "coupe quattro",
    "e-tron",
    "tt roadster",
    "bentley",
    "continental",
    "flying spur",
    "bmw",
    "buick",
    "apollo",
    "cascada",
    "centurion",
    "century",
    "electra",
    "enclave",
    "encore",
    "excelle",
    "invicta",
    "lacrosse",
    "lesabre",
    "lucerne",
    "park avenue",
    "rainier",
    "reatta",
    "regal",
    "rendezvous",
    "riviera",
    "roadmaster",
    "skyhawk",
    "skylark",
    "special",
    "super",
    "terraza",
    "verano",
    "wildcat",
    "cadillac",
    "brougham",
    "calais",
    "catera",
    "cimarron",
    "deville",
    "eldorado",
    "escalade",
    "fleetwood",
    "series 62",
    "seville",
    "chevrolet",
    "astro",
    "avalanche",
    "avalanche",
    "aveo",
    "bel air",
    "beretta",
    "biscayne",
    "blazer",
    "brookwood",
    "c10 pickup",
    "c10 suburban",
    "c1500",
    "c1500 suburban",
    "c20 pickup",
    "c20 suburban",
    "c2500",
    "c2500 pickup",
    "c2500 suburban",
    "c30 pickup",
    "c3500",
    "c3500 pickup",
    "c4500 kodiak",
    "c5500 kodiak",
    "camaro",
    "caprice",
    "captiva",
    "captiva sport",
    "cavalier",
    "celebrity",
    "chevelle",
    "chevette",
    "chevy",
    "cheyenne",
    "city express",
    "classic",
    "cobalt",
    "colorado",
    "combo",
    "corsa",
    "corsica",
    "corvette",
    "cruze",
    "el camino",
    "epica",
    "equinox",
    "evanda",
    "express 1500",
    "express 2500",
    "express 3500",
    "express 4500",
    "impala",
    "impala limited",
    "k1500",
    "k2500",
    "k3500",
    "k5 blazer",
    "kalos",
    "kingswood",
    "lacetti",
    "laser",
    "lumina",
    "malibu",
    "matiz",
    "meriva",
    "metro",
    "montana",
    "monte carlo",
    "nova",
    "nubira",
    "optra",
    "orlando",
    "rezzo",
    "silverad",
    "sonic",
    "spark",
    "sprint",
    "suburban",
    "tacuma",
    "tahoe",
    "tornado",
    "townsman",
    "tracker",
    "trailblazer",
    "traverse",
    "trax",
    "uplander",
    "vectra",
    "vega",
    "venture",
    "vivant",
    "zafira",
    "chrysler",
    "aspen",
    "cirrus",
    "concorde",
    "conquest",
    "cordoba",
    "crossfire",
    "fifth avenue",
    "grand voyager",
    "intrepid",
    "lebaron",
    "neon",
    "new yorker",
    "newport",
    "pacifica",
    "pt cruiser",
    "sebring",
    "town & country",
    "voyager",
    "citroen",
    "berlingo",
    "aircross",
    "picasso",
    "aircross",
    "cactus",
    "grand picasso",
    "picasso",
    "c-elysee",
    "evasion",
    "jumper",
    "jumpy",
    "nemo",
    "saxo",
    "spacetourer",
    "visa",
    "xantia break",
    "xm-xm break",
    "xsara",
    "xsara picasso",
    "dacia",
    "duster",
    "lodgy",
    "logan",
    "logan mcv",
    "pick-up",
    "sandero",
    "solenzo",
    "daewoo",
    "cielo",
    "damas",
    "espero",
    "kalos",
    "korando",
    "lacetti",
    "lanos",
    "leganza",
    "lublin",
    "matiz",
    "musso",
    "nexia",
    "nubira",
    "pick-up",
    "polonez",
    "rezzo",
    "tico",
    "daihatsu",
    "charade",
    "extol",
    "hi-jet",
    "materia",
    "sirion",
    "terios",
    "dodge",
    "aries",
    "aspen",
    "attitude",
    "avenger",
    "caliber",
    "caravan",
    "challenger",
    "charger",
    "coronet",
    "dakota",
    "dart",
    "daytona",
    "dinasty",
    "diplomat",
    "durango",
    "grand caravan",
    "imperial",
    "intrepid",
    "journey",
    "lebaron",
    "magnum",
    "monaco",
    "neon",
    "new yorker",
    "nitro",
    "omni",
    "phantom",
    "polara",
    "ram 1500",
    "ram 2500",
    "ram 3500",
    "ram 4500",
    "ram 50",
    "ram 5500",
    "ramcharger",
    "rampage",
    "shadow",
    "sprinter 2500",
    "sprinter 3500",
    "sprit",
    "stealth",
    "stratus",
    "eagle",
    "summit",
    "talon",
    "vision",
    "vista",
    "edsel",
    "citation",
    "corsair",
    "pacer",
    "ranger",
    "roundup",
    "villager",
    "fiat",
    "panorama",
    "familiare",
    "panorama",
    "mirafiori",
    "panorama",
    "albea",
    "barchetta",
    "bravo",
    "brava",
    "cinquecento",
    "coupe",
    "croma",
    "doblo",
    "doblo mpv",
    "ducato",
    "duna",
    "egea",
    "fiorino",
    "freemont",
    "fullback",
    "grande punto",
    "idea",
    "linea",
    "marea",
    "multipla",
    "palio",
    "panda",
    "pratico",
    "premio",
    "punto",
    "punto evo",
    "qubo",
    "regata",
    "ritmo",
    "scudo",
    "sedici",
    "seicento",
    "siena",
    "stilo",
    "strada",
    "talento",
    "tempra",
    "tipo",
    "ulysse",
]


#
#
#
# Amazon supply chain:
# 0.1289 kg CO2e per dollar (USD).
# 3,300,000 boxes/day * 365 days/year / 325,000,000 Americans = 3.70 boxes/American.
# 3.70 boxes/year * $47 / box = ~$173.90/year * 0.1289 kg / $1 USD= 22.41 kg CO2/year.
# 22.41 kg CO2/year / 3.70 boxes/year = 22.41/3.70 kg CO2/box = 6.06 kg CO2/box
onlineshopping_exact = {"Average" : 6.06}
#
onlineshopping = [
    "online shopping",
    "online shop",
    "Amazon",
    "Aliexpress",
    "Ali-express",
    "Ali express",
    "American Eagle Outfitters",
    "Anthropologie",
    "ASOS",
    "Boohoo",
    "eBay",
    "Forever 21",
    "Lululemon",
    "Modcloth",
    "Mystery Tackle Box",
    "Nasty Gal",
    "PrettyLittleThing",
    "Purple mattress",
    "Sephora",
    "Showpo",
    "Target",
    "Urban Outfitters",
    "Wayfair",
    "Zara",
]

#
#
#
# For each kilowatt hour generated in the U.S., an average of 0.953 pounds of CO2e is released at the power plant.
# Electricity:
# Electric bill - 11,698 kwh/year = average energy consumption / household.
# the U.S. average is 13.27 cents per kilowatt hour (kwh), 0.62 kilogramCO2 / kwh.
# 11,698 kwh/year * 0.62 kgCO2/kwh = 7,252.76 kg CO2/year.
# 604.4kg CO2/month/household, average monthly electricity utility bill is 604.4kg CO2
electricity_exact = {"Average" : 604.4}
#
electricity = [
    "energía",
    "eléctrica",
    "electrica",
    "hidroeléctrica",
    "endesa",
    "iberdrola",
    "edp",
    "bassols",
    "estabanell",
    "Fenosa",
    "arcos",
    "aduriz",
    "gaselec",
    "enercoluz",
    "factor",
    "alpapat",
    "engie",
    "alpiq",
    "naturgy",
    "navarro",
    "nexus",
    "hidroelectrica",
    "bp",
    "agr",
    "fluid",
    "global3",
    "axpo",
    "cepsa",
    "energya",
    "factor",
    "repsol",
    "wind",
    "energya",
    "enel",
    "acciona",
    "atel",
    "energya",
    "gdf",
    "geoatlanter",
    "fortia",
    "constellation",
    "gesternov",
    "viacav",
    "rwe",
    "baser",
    "escandinava",
    "régsiti",
    "cide",
    "energia",
    "alpiq",
    "accord",
    "barclays",
    "bp",
    "danske",
    "electrabe",
    "uniper",
    "edf",
    "electricité",
    "elektrizität",
    "enbw",
    "enel",
    "kalibra",
    "rede",
    "shell",
    "sonelgaz",
    "statkraft",
    "total",
    "hidroelectrica",
    "sociedad",
    "energias",
    "electra",
    "hidroelectrica",
    "curenergía",
    "societat",
    "distribuidora",
    "energy",
    "distribuidora",
    "orus",
    "elèctrica",
    "cateneribas",
    "estabanell",
    "municipal",
    "energias",
    "societat",
    "talarn",
    "gazprom",
    "servicios",
    "madrileña",
    "nexus",
    "naturgy",
    "saltos",
    "hidroelectrica",
    "lonjas",
    "hidroeléctrica",
    "geoatlanter",
    "elecva",
    "evergreen",
    "villar",
    "audax",
    "syder",
    "respira",
    "eléctricas",
    "fluido",
    "fenie",
    "enara",
    "alpiq",
    "electro",
    "holalu",
    "iposta",
    "energia",
    "celtica",
    "aracan",
    "grupo",
    "aayum",
    "cooperativa",
    "mallorquina",
    "sampol",
    "nordjysk",
    "dreue",
    "forces",
    "zeltria",
    "switch",
    "knet",
    "canary",
    "gdf",
    "zence",
    "gestionna",
    "electrourbano",
    "cooperativa",
    "ecoeq",
    "holding",
    "sunair",
    "compañia",
    "unielectrica",
    "olte",
    "vóltico",
    "laboil",
    "watiu",
    "gnera",
    "energias",
    "ampere",
    "carvisa",
    "solvay",
    "alcanzia",
    "xenera",
    "atlas",
    "europa",
    "iner",
    "goiener",
    "vertsel",
    "euroenergia",
    "stagioni",
    "aurora",
    "adelfas",
    "iberoelectra",
    "bkw",
    "integración",
    "indexo",
    "mercuria",
    "concis",
    "ninobe",
    "solelec",
    "watio",
    "nueva",
    "energy",
    "corpolu",
    "foener",
    "nortedison",
    "centrica",
    "conecta2",
    "tecnos",
    "energia",
    "insignia",
    "corporación",
    "petronieves",
    "energi",
    "siesta",
    "catralense",
    "aldro",
    "sunair",
    "suministros",
    "aldefe",
    "nemon",
    "eleva",
    "iberelectrica",
    "energia",
    "eneluz",
    "telefónica",
    "daimuz",
    "adixa",
    "elecnova",
    "ledesma",
    "multienergia",
    "adetec",
    "global",
    "iniciativa",
    "jorge",
    "hefameco",
    "enerxia",
    "trailstone",
    "rofeica",
    "servigas",
    "sunair",
    "horeca",
    "aserval",
    "enerplus",
    "nobe",
    "eleva",
    "energysave",
    "loop",
    "ayluz",
    "alterna",
    "ingeniería",
    "elygas",
    "inserimos",
    "pulsar",
    "energetica",
    "pepeenerg",
    "renewable",
    "gaolania",
    "accion",
    "alnair",
    "electiaplus",
    "electroroute",
    "apeles",
    "noble",
    "adeinnova",
    "luvon",
    "elegrand",
    "energika",
    "ronda",
    "emasp",
    "luzdeaqu",
    "enstrog",
    "cemoi",
    "catgas",
    "gestiona",
    "neoelectra",
    "optimus",
]


#
#
#
clothes_exact = {"Average" : 7.0}  # average 7kg CO2 per item of clothing

clothes = [
    "anillo",
    "arete",
    "pendiente",
    "cinturón",
    "gorro",
    "guante",
    "pantalón",
    "sombrero",
    "sujetador",
    "suéter",
    "jersey",
    "traje",
    "vestido",
    "billetera",
    "blusa",
    "boina",
    "camisa",
    "camiseta",
    "chaqueta",
    "corbata",
    "falda",
    "gorra",
    "piyama",
    "pijama",
    "botas",
    "gafas",
    "pantuflas",
    "calcetines",
    "calzoncillos",
    "zapatos",
    "pantalones",
    "falda",
    "vestido",
    "camisa",
    "camiset",
    "calcetines",
    "zapatos",
    "suéter",
    "chamarra",
    "sombrero",
    "pantalones",
    "pantalones",
    "chanclas",
    "uniforme",
    "traje",
    "abrigo",
    "anorak",
    "cinturón",
    "boina",
    "bikini",
    "blusa",
    "botas",
    "pajarita",
    "sujetador",
    "tirantes",
    "botón",
    "gorra",
    "rebeca",
    "abrigo",
    "vestido",
    "cordones",
    "gemelos",
    "smoking",
    "vestido",
    "bata",
    "guantes",
    "sombrero",
    "tacones altos",
    "chaqueta",
    "vaqueros",
    "jersey",
    "jersey",
    "bragas",
    "camisón",
    "skirt",
    "mini-falda",
    "mono",
    "calzoncillos",
    "pijama",
    "impermeable",
    "sandalias",
    "bufanda",
    "camisa",
    "zapatos",
    "pantalones",
    "pantalones cortos",
    "falda",
    "zapatillas",
    "calcetines",
    "tacón de aguja",
    "medias",
    "traje",
    "liguero",
    "jersey",
    "sudadera",
    "bañador",
    "camiseta",
    "corbata",
    "panty",
    "chandal",
    "pantalones",
    "uniforme",
    "chaleco",
    "botas de goma",
    "cremallera",
]

# EOF
