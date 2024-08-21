#RANDOM CLASS COD GHOST:

AK47 = 1
M4A1 = 2
G3 = 3
G36C = 4
M16 = 5
MP44 = 6
M14 = 7
M249_SAW = 8
M60E4 = 9
RPD = 10
P90 = 11
Mini_Uzi = 12
Skorpion = 13
MP5 = 14
AK74u = 15
W1200 = 16
M1014 = 17
Barrett_50cal = 18
M40A3 = 19
R700 = 20
Dragunov = 21
M21 = 22
M1911 = 23
USP_45 = 24
M9 = 25
Desert_Eagle = 26
Cegadora = 27
Aturdidora = 28
Humo = 29
C4x2 = 30
RPG7x2 = 31
Granadas_especialesx3 = 32
Escuadron_bomba = 33
Claymorex2 = 34
Bandolera = 35 
Fragmentacionx3 = 36
Fuerza_vulnerante = 37
JUGGERNAUT = 38
Boom_sonico = 39
Inhibidor_UAV = 40
Pretidigitacion = 41
Fuego_rapido = 42
Exceso_de_medios = 43
Condicionamiento_extremo = 44
Punteria_estable = 45
Impacto_profundo = 46
Ultima_batalla = 47 
Martirio = 48 
Pulmones_de_hierro = 49
Escuchar_a_escondidas = 50
Silencio_mortal = 51
Punto_rojo = 52
Lanzagranada = 53
Silenciador = 54
ACOG = 55

print("¿Quieres generar una clase aleatoria?")
comienzo = input("Comenzar: si/no ")

if comienzo == "si":
    import random

    while True:

        Principal = random.randrange(1, 22)
        print("Principal:")

        if Principal == 1:
            print("AK-47")
        elif Principal == 2:
            print("M4A1")
        elif Principal == 3:
            print("G3")
        elif Principal == 4:
            print("G36C")
        elif Principal == 5:
            print("M16")
        elif Principal == 6:
            print("MP44")
        elif Principal == 7:
            print("M14")
        elif Principal == 8:
            print("M249 SAW")
        elif Principal == 9:
            print("M60E4")
        elif Principal == 10:
            print("RPD")
        elif Principal == 11:
            print("P90")
        elif Principal == 12:
            print("Mini Uzi")
        elif Principal == 13:
            print("Skorpion")
        elif Principal == 14:
            print("MP5")
        elif Principal == 15:
            print("AK-74u")
        elif Principal == 16:
            print("W1200")
        elif Principal == 17:
            print("M1014")
        elif Principal == 18:
            print("Barrett .50cal")
        elif Principal == 19:
            print("M40A3")
        elif Principal == 20:
            print("R700")
        elif Principal == 21:
            print("Dragunov")
        elif Principal == 22:
            print("M21")
    
        Secundaria = random.randrange(23, 26)
        print("Secundaria:")

        if Secundaria == 23:
            print("M1911")
        elif Secundaria == 24:
            print("USP .45")
        elif Secundaria == 25:
            print("M9")
        elif Secundaria == 26:
            print("Desert Eadle")
    
        Tactica = random.randrange(27, 29)
        print("Tactica:")

        if Tactica == 27:
            print("Cegadora")
        elif Tactica == 28:
            print("Aturdidora")
        elif Tactica == 29:
            print("Humo")

        Ventaja1 = random.randrange(30, 36)
        print("Ventaja 1:")

        if Ventaja1 == 30:
            print("C4 x2")
        elif Ventaja1 == 31:
            print("RPG-7 x2")
        elif Ventaja1 == 32:
            print("Granadas especiales x3")
        elif Ventaja1 == 33:
            print("Escuadron bomba")
        elif Ventaja1 == 34:
            print("Claymore x2")
        elif Ventaja1 == 35:
            print("Bandolera")
        elif Ventaja1 == 36:
            print("Fragmentacion x3")
    
        Ventaja2 = random.randrange(37, 43)
        print("Ventaja 2:")

        if Ventaja2 == 37:
            print("Fuerza vulnerante")
        elif Ventaja2 == 38:
            print("JUGGERNAUT")
        elif Ventaja2 == 39:
            print("Boom sonico")
        elif Ventaja2 == 40:
            print("Inhibidor UAV")
        elif Ventaja2 == 41:
            print("Pretidigitacion")
        elif Ventaja2 == 42:
            print("Fuego rapido")
        elif Ventaja2 == 43:
            print("Exceso de medios")

        Ventaja3 = random.randrange(44, 51)
        print("Ventaja 3:")

        if Ventaja3 == 44:
            print("Condicionamiento extremo")
        elif Ventaja3 == 45:
            print("Punteria estable")
        elif Ventaja3 == 46:
            print("Impacto profundo")
        elif Ventaja3 == 47:
            print("Ultima batalla")
        elif Ventaja3 == 48:
            print("Martirio")
        elif Ventaja3 == 49:
            print("Pulmones de hierro")
        elif Ventaja3 == 50:
            print("Escuchar a escondidas")
        elif Ventaja3 == 51:
            print("Silencio mortal")
    
        again = input("¿Quieres generar una nueva clase? si/no ")
        if again != "si":
            break