discs = 256
counter = 0
mn = '1000'

for disc in range(discs):
    print('create-volume '+counter+'(unit='+mn+')')
    counter = counter + 1
    mn = hex(counter)
    mn = mn.split(2:4)
    mn = '10' + mn