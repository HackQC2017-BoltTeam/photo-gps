import exifread


def extrapolationGPS(CheminPhoto):
    f = open(CheminPhoto, 'rb')
    tags = exifread.process_file(f)


    exifread.geo = {i: tags[i] for i in tags.keys() if i.startswith('GPS GPSLatitude')}
    gpslatitude = exifread.geo
    degre = gpslatitude['GPS GPSLatitude'].values[0]  ## float
    minute = gpslatitude['GPS GPSLatitude'].values[1]  ## float
    seconde = gpslatitude['GPS GPSLatitude'].values[2]  ## float
    direction = gpslatitude['GPS GPSLatitudeRef'].values[0]
    strseconde = str(seconde)
    num, divnum = strseconde.split('/')
    seconde = int(num) / int(divnum)
    LongLatitude = [dms2dd(degre, minute, seconde, direction)]

    exifread.geo = {i: tags[i] for i in tags.keys() if i.startswith('GPS GPSLongitude')}
    gpsLongitude = exifread.geo
    degre2 = gpsLongitude['GPS GPSLongitude'].values[0]
    minute2 = gpsLongitude['GPS GPSLongitude'].values[1]
    seconde2 = gpsLongitude['GPS GPSLongitude'].values[2]
    strseconde2 = str(seconde2)
    num2, divnum2 = strseconde2.split('/')
    seconde2 = int(num2) / int(divnum2)
    direction2 = gpsLongitude['GPS GPSLongitudeRef'].values[0]
    LongLatitude.append(dms2dd(degre2, minute2, seconde2, direction2))
    return LongLatitude


def dms2dd(degrees, minutes, secondes, direction):

    dd = float(degrees.num) + float(minutes.num) / 60 + secondes / (60 * 60)
    if direction == "W" or direction == "S":
        dd *= -1
    return dd

## retourne une coordonner
print(extrapolationGPS('test.jpg'))
