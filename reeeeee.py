get_prime = (lambda a: list(filter(lambda b:b[0]==a, enumerate(list(filter(lambda c: all(c%i!=0 for i in range(2, int(c/2)+1)), range(2, 1337*2))))))[0][1])

__import__("os").write(True, bytes((lambda _: _).__code__.co_name[....__str__()=="....":int(((0+1j)**(lambda _, __: _).__code__.co_argcount + True).real)].join((map(lambda x: chr(get_prime(5)*int((get_prime(4)*abs(x-pow(get_prime(1)*get_prime(6), 1/4)+2)-x+pow(get_prime(get_prime(1)), 1/2)-2)/(2*abs(x-pow(get_prime(get_prime(get_prime(get_prime(4))*2)-1), 1/8)+2))) + ....__sizeof__()+True), range(20)))), "utf8"))

"""0 2
1 3
2 5
3 7
4 11
5 13
6 17
7 19
8 23
9 29
10 31
11 37
12 41
13 43
14 47
15 53
16 59
17 61
18 67
19 71
20 73
21 79
22 83
23 89
24 97"""