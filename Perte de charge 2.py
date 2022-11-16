def my_function():
    print("Perte de charge EX2")
    print("Question 1")
    Mv = input("Entrez la masse volumique de l'eau :")
    Vd = input("Entrez la viscosité dynamique :")
    D = input("Entrez la densité: ")
    try:
        Mv = float(Mv)
        Vd = float(Vd)
        D = float(D)
        Vc = Vd / (D * Mv)
        print("La viscosité cénimatique est ", Vc)
    except:
        print("Erreur")

    print("Question 2")
    Qv = input("Entrez le débit volumique :")
    D = input("Entrez le diamétre de la conduite :")
    try:
        Qv = float(Qv)
        D = float(D)
        Pi = 3.14
        V = 4 * Qv / (Pi * D ^ 2)
        print("La vitesse est ", V)

    except:
        print("Erreur")

    from turtle import end_fill
    print("Question 3")
    D1 = input("Entrez la diamétre  de la conduite")
    try:
        V = float(V)
        D1 = float(D1)
        Ve = 1000
        Re = ((V * D1) / Ve)
        if Re > 100000
            print("Régime Turbulent")
        else:
            print("Régime laminaire")
        end_fill
    except:
        print("Erreur")

    print("Question 4")
    print("Lnd=f(Re)")
    try:
        Lnd = 64 / Re
        print("La vitesse est ", V)

    except:
        print("Erreur")


my_function