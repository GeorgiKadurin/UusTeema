def number(nimi:str):
    tähestik = {
        "а": 1, "б": 2, "в": 3, "г": 4, "д": 5, "е": 6, "ё": 7, "ж": 8, "з": 9,
        "и": 1, "й": 2, "к": 3, "л": 4, "м": 5, "н": 6, "о": 7, "п": 8, "р": 9,
        "с": 1, "т": 2, "у": 3, "ф": 4, "х": 5, "ц": 6, "ч": 7, "ш": 8, "щ": 9,
        "ъ": 1, "ы": 2, "ь": 3, "э": 4, "ю": 5, "я": 6,

        "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9,
        "j": 1, "k": 2, "l": 3, "m": 4, "n": 5, "o": 6, "p": 7, "q": 8, "r": 9,
        "s": 1, "t": 2, "u": 3, "v": 4, "w": 5, "x": 6, "y": 7, "z": 8 }
    

    x = "ru"   # tähestiku määratlus
    for f in nimi:
        if f.isalpha():
            if f.lower() in tähestik:
                x = "ru"
            elif f.lower() in tähestik.values():
                x = "eng"
            break

    
    numder_nimi = 0  # nimenumbri arvutamine
    for f in nimi:
        if f.isalpha():
            numder_nimi+=tähestik[f.lower()] 
         
    if  numder_nimi > 9:
        numbrid = [int(numbri) for numbri in str(numder_nimi)] #teisendab numder_nimi numbrite loendiks.
        numder_nimi = sum(numbrid)

    return numder_nimi





