def foo(x,y,z,*agrs,**kwargs):
    print(x,y,z)
    print(*agrs)
    print(**kwargs)

foo(1, 2, 3, 10, 12, 14, name = "Olga", age = 14)