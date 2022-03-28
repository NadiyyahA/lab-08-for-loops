partycountdown = input("How long until the party starts? ")
partycountdown = int(partycountdown)

if partycountdown < 1:
    print("PARTY NOW!")
else:
    for i in range(partycountdown, 0, -1):
        print(i)
       if i == 1:
          print("PARTY TIME!")
