arr=[5, 5, 10, 100, 10, 5]
ecal=0
incal=0
for i in arr:
    new_excl =max(incal,ecal)

    incal=ecal+i
    ecal=new_excl
print(max(incal,ecal))