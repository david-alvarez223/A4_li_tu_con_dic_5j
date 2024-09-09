print("Ejemplo de tuplas")
cancones=("Te amo","El NoNoa","Amor eterno")
print(cancones)
y=list(cancones)
y[1]="La puerta negra"
cancones=tuple(y)
print(cancones)