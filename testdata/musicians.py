from music.musician_module import Musician

# Data

# The Beatles
johnLennon = Musician('John Lennon', is_band_member=True)
paulMcCartney = Musician('Paul McCartney', is_band_member=True)
georgeHarrison = Musician('George Harrison', is_band_member=True)
ringoStarr = Musician('Ringo Starr', is_band_member=True)

# The Rolling Stones
mickJagger = Musician('Mick Jagger')          # default: is_band_member=True
keithRichards = Musician('Keith Richards')
charlieWatts = Musician('Charlie Watts')
ronWood = Musician('Ron Wood')

# Pink Floyd
sydBarrett = Musician('Syd Barrett')
rogerWaters = Musician('Roger Waters')
davidGilmour = Musician('David Gilmour')
nickMason = Musician('Nick Mason')
rickWright = Musician('Rick Wright')

# Solo musicians
nickCave = Musician('Nick Cave', is_band_member=False)
bobDylan = Musician('Bob Dylan', is_band_member=False)
taylorSwift = Musician('Taylor Swift', is_band_member=False)
elliottSmith = Musician('Elliott Smith', is_band_member=False)

