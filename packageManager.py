import sys

if __name__ == "__main__":


    if (sys.argv[1] == "python"):
        filename = sys.sys.argv[2]

    if (sys.argv[1] == 'add'):
        name = sys.argv[2]
        l = list()
        for arg in sys.argv[3:]:
            l.append(arg)

        note = input("Please provide a note for the packages:\n")
        while (len(note)> 100):
            note = input("Please provide a note for the packages in less than 100 characters:\n")
        f = open("packages.txt", "a")
        f.write(name+" "+" ".join(l)+'\n' + note + '\n')
        f.close()

        # check for existence

    # creates a file with the package
    if (sys.argv[1] == "make"):
        file = open(sys.argv[2], "w")
        packageName = sys.argv[3]
        dir = open("packages.txt", "r")
        line = dir.readline()

        while((line) and (not line.startswith(packageName))):
            line = dir.readline()
        if (not line):
            print("the package does not eixst")

        args = line.split()
        for arg in args[1:]:
            file.write("import "+ arg+'\n')

        file.close()

    if (sys.argv[1] == "list"):
        f = open("packages.txt", "r")
        l = []
        fl = f.readline()
        count = 0
        while (fl):
            if (count == 10):
                res = input("Do you want to print more? Press y to continue\n")
                count = 0
                if (res != "y"):
                    break
            sl = f.readline()
            pkgs = fl.split()
            print("Group Name:          " + pkgs[0])
            print("Associated packages: " + ", ".join(pkgs[1:]))
            print("Note:                " + sl + '\n')
            count+=1
            fl = f.readline()

    # help

    # show one package

