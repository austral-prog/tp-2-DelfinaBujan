def change():
    expense = 23.75
    money = 100
    vuelto=money-expense
    pesos= int(vuelto)
    centavos= int((vuelto-pesos)*100)
    print(f"Ingresar gasto:\n{expense}")
    print(f"Dinero Recibido\n{money}")
    print(f"\nVuelto\n{vuelto}")
    print(f"\nPesos:\n{pesos}")
    print(f"Centavos:\n{centavos}")
