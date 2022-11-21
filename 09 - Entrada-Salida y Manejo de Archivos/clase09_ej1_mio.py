import sys

if len(sys.argv) == 5:
    c1 = sys.argv[1]
    c2 = sys.argv[2]
    c3 = sys.argv[3]
    c4 = sys.argv[4]

    print(f'Tus argumentos son: {c1}, {c2}, {c3}, {c4} {type(c1)}')

elif len(sys.argv) != 5:
    print('Este script solo acepta 4 argumentos, no más ni menos.')
    print(len(sys.argv), sys.argv)
