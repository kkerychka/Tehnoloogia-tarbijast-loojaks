def eelarve(inimene):
    return inimene * 10 + 55

kutsutud = int(input("Mitu inimest on kutsutud? "))
tuleb = int(input("Mitu inimest tuleb? "))
print("Maksimaalne eelarve:", eelarve(kutsutud))
print("Minimaalne eelarve:", eelarve(tuleb))