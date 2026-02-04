def ru():
    hpy_skill=bool(input()).strip()
    yrs_exp=int(input()).strip()
    has_deg=bool(input()).strip()
    sc=50;
    if hpy_skill:
        sc+=10

    sc=sc+yrs_exp*5    
    if has_deg:
        sc*=1.1
    print("Final match score: ",sc)
ru()        