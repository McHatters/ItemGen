msg = "Dom 5 ItemGen - 2022"
print(msg)

def test_write(f, lines):
    for line in lines:
        f.write(line)
        f.write("test num" + str(1) + "\n")
        f.write('\n')

#TODO: Put this in its own py file
def hideVanillaItems(f):
    for i in range(1, 500):
        f.write("#selectitem " + str(i) + "\n")
        f.write("#constlevel 12\n")
        f.write("#end\n")

def generateModInfo(f):
    modname = '#modname "Test ItemGen Mod"\n'
    desc = '#description "ItemGen Test"\n'
    version = '#version 1.00\n'
    f.writelines([modname, desc, version])

def genTestItem(f):
    itemID = "#newitem 500\n"
    name = '#name "testItem"\n'
    desc = '#descr "Test Item Please Ignore"\n'
    constlevel = "#constlevel 0\n"
    itemtype = "#type 9\n"
    mainpath = '#mainpath 5\n'
    mainlevel = '#mainlevel 2\n'
    hp = '#hp 5\n'
    armor = '#armor 300\n'
    end = "#end\n"

    armor1 = '#newarmor 300\n'
    armor2 = '#type 6\n'
    armor3 = '#name "test"\n'
    armor4 = '#descr "test"\n'
    armor5 = '#prot 9\n'
    armor6 = '#magicarmor\n'

    f.writelines([itemID, name, desc, constlevel, itemtype, mainpath, mainlevel, hp, armor, end])
    f.writelines([armor1, armor2, armor3, armor4, armor5, armor6, end])


    

lines = ["Hello World!", "Dom5 ItemGen file test"]
with open("test.dm", 'w') as f:
    #test_write(f,lines)
    generateModInfo(f)
    hideVanillaItems(f)
    genTestItem(f)

