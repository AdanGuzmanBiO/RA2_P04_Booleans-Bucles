print("\nBenvingut/uda a la creacio del teu avatar de videojoc!")  # Missatge de benvinguda

nom = input("\nQuin es el teu nom? ")                         # Demana el nom a l'usuari
cognom = input("Quin es el teu cognom? ")                   # Demana el cognom a l'usuari
nom_avatar = input("Indica el nom del teu avatar: ")        # Demana el nom de l'avatar
edat_avatar = int(input("Indica l'edat del teu avatar: "))       # Demana l'edat de l'avatar

## Linea 6-33: 

PuntsHabilitatRestants = 100
PuntsUtilitzatsTotals = 0
nivell_intelligencia_Total = 0
nivell_velocitat_Total = 0
nivell_forca_Total = 0

while PuntsHabilitatRestants > 0:
    print("Punts d'habilitat restants: ", PuntsHabilitatRestants)

    try:

        nivell_intelligencia_Agregats = float(input("Indica el nivell d'intelligencia del teu avatar: "))               # Demana el nivell d'intelligencia
        nivell_velocitat_Agregats = float(input("Indica el nivell de velocitat del teu avatar: "))                      # Demana el nivell de velocitat
        nivell_forca_Agregats = float(input("Indica el nivell de força del teu avatar: "))                              # Demana el nivell de força
        
        PuntsUtilitzatsActuals = nivell_intelligencia_Agregats + nivell_velocitat_Agregats + nivell_forca_Agregats
        PuntsUtilitzatsTotals = PuntsUtilitzatsTotals + PuntsUtilitzatsActuals

        if nivell_intelligencia_Agregats < 0 or nivell_velocitat_Agregats < 0 or nivell_forca_Agregats < 0:
            print("No pots utilitzar punts negatius.")
            PuntsUtilitzatsTotals = PuntsUtilitzatsTotals - PuntsUtilitzatsActuals
            PuntsUtilitzatsActuals = 0
            nivell_intelligencia_Agregats = 0
            nivell_velocitat_Agregats = 0
            nivell_forca_Agregats = 0


        if PuntsUtilitzatsTotals > 100:
             print("Has superat els punts d'habilitat que pots utlitzat, el maxim que pots utilitzat son 100.")
             PuntsUtilitzatsTotals = PuntsUtilitzatsTotals - PuntsUtilitzatsActuals
             PuntsUtilitzatsActuals = 0
             nivell_intelligencia_Agregats = 0
             nivell_velocitat_Agregats = 0
             nivell_forca_Agregats = 0
            
        PuntsHabilitatRestants = PuntsHabilitatRestants - PuntsUtilitzatsActuals
        nivell_intelligencia_Total = nivell_intelligencia_Total + nivell_intelligencia_Agregats
        nivell_velocitat_Total = nivell_velocitat_Total + nivell_velocitat_Agregats
        nivell_forca_Total = nivell_forca_Total + nivell_forca_Agregats

        
        print("Punts utilitzats: ", PuntsUtilitzatsTotals)

    except ValueError: 
            print("Valor incorrecte")

mitjana_stats = (nivell_intelligencia_Total + nivell_velocitat_Total + nivell_forca_Total) / 3     # Calcula la mitjana dels stats
descripcio_avatar = input("Fes una desctipcio del teu avatar: ")                                # Demana una descripcio de l'avatar


# Mostra tota la informacio recollida a la consola
print("\nEl teu nom es:", nom, cognom)
print("El nom del teu avatar es:", nom_avatar)
print("L'edat del teu avatar es:", edat_avatar)
print("El nivell d'intelligencia del teu avatar es:", nivell_intelligencia_Total)
print("El nivell de velocitat del teu avatar es:", nivell_velocitat_Total)   
print("El nivell de força del teu avatar es:", nivell_forca_Total)
print("La mitjana dels stats del teu avatar es:", mitjana_stats)
print("La descripcio del teur avatar es:", descripcio_avatar)


bios = 500.00
Preu_AugmentarInteligencia = 10.00
Preu_AugmentarVelocitat = 25.00
Preu_AugmentarForca = 50.00

while True:
     
     print("\n1. Veure Fitxa del teu Avatar")
     print("2. Augmentar Nivell d'Intelligencia (10 Bios)")
     print("3. Augmentar Nivell de Velocitat (25 Bios)")
     print("4. Augmentar Nivell de Força (50 Bios)")
     print("5. Sortir de la botiga")

     opcio_menu = input("\nTria una opció del menú: " )
     match opcio_menu:
         
        case "1":
            print("\nFitxa del teu Avatar")
            print("\nEl teu nom es:", nom, cognom)
            print("El nom del teu avatar es:", nom_avatar)
            print("L'edat del teu avatar es:", edat_avatar)
            print("El nivell d'intelligencia del teu avatar es:", nivell_intelligencia_Total)
            print("El nivell de velocitat del teu avatar es:", nivell_velocitat_Total)   
            print("El nivell de força del teu avatar es:", nivell_forca_Total)
            print("Bios disponibles: ", bios)
        
        case "2":
            nivell_intelligencia_Agregats = float(input("Indica quants punts d'intelligencia vols augmentar: "))
            Preu_AugmentarInteligencia_Total = nivell_intelligencia_Agregats * Preu_AugmentarInteligencia

            if Preu_AugmentarInteligencia_Total > bios:
                nivell_intelligencia_Agregats = 0
                Preu_AugmentarInteligencia_Total = 0
                print("No tens suficients bios per augmentar aquest nivell d'intelligencia.")
            else:
                nivell_intelligencia_Total = nivell_intelligencia_Total + nivell_intelligencia_Agregats
                bios = bios - Preu_AugmentarInteligencia_Total
                print("\nHas Augmentat el nivell d'Intelligencia del teu avatar, ara es de:", nivell_intelligencia_Total)
                print("Bios restants:", bios)
        
        case "3":
            nivell_velocitat_Agregats = float(input("Indica quants punts de velocitat vols augmentar: "))
            Preu_AugmentarVelocitat_Total = nivell_velocitat_Agregats * Preu_AugmentarVelocitat

            if Preu_AugmentarVelocitat_Total > bios:
                nivell_velocitat_Agregats = 0
                Preu_AugmentarVelocitat_Total = 0
                print("No tens suficients bios per augmentar aquest nivell de velocitat.")
            else:
                nivell_velocitat_Total = nivell_velocitat_Total + nivell_velocitat_Agregats
                bios = bios - Preu_AugmentarInteligencia_Total
                print("\nHas Augmentat el nivell de velocitat del teu avatar, ara es de:", nivell_velocitat_Total)
                print("Bios restants:", bios)

        case "4":
            nivell_forca_Agregats = float(input("Indica quants punts de força vols augmentar: "))
            Preu_AugmentarForca_Total = nivell_forca_Agregats * Preu_AugmentarForca

            if Preu_AugmentarForca_Total > bios:
                nivell_forca_Agregats = 0
                Preu_AugmentarForca_Total = 0
                print("No tens suficients bios per augmentar aquest nivell de velocitat.")
            else:
                nivell_forca_Total = nivell_forca_Total + nivell_forca_Agregats
                bios = bios - Preu_AugmentarForca_Total
                print("\nHas Augmentat el nivell de velocitat del teu avatar, ara es de:", nivell_forca_Total)
                print("Bios restants:", bios)
        
        case "5":
            print("\nGràcies per visitar la botiga!")
            break
         