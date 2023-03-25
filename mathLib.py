def formatUICoord(res, coord:tuple[int, int]):
    x, y = coord
    resx, resy = res
    
    if x < 0:
        x = resx - x
    if y < 0:
        y = resy - y
        
    return x, y