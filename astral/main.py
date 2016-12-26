#!/usr/bin/env python3

from astral import Astral, Location

#Astral', 'AstralError', 'AstralGeocoder', 'GoogleGeocoder', 'Location', 'LocationGroup', 'SUN_RISING', 'SUN_SETTING', 'SunBelowHorizonError', 'URLError', '_LOCATION_INFO'

def info(city):
    sun = city.sun()

    #print('Astral           :', city.astral)
    print('Blue Hour        :', city.blue_hour()[0], '---', city.blue_hour()[1])
    print('Dawn             :', city.dawn())
    print('Daylight         :', city.daylight()[0], '---', city.daylight()[1])
    print('Dusk             :', city.dusk())
    print('Elevation        :', city.elevation)
    print('Golden Hour      :', city.golden_hour()[0], '---', city.golden_hour()[1])
    print('Latitude         :', city.latitude)
    print('Longitude        :', city.longitude)
    print('Moon Phase       :', city.moon_phase())
    print('Name             :', city.name)
    print('Night            :', city.night()[0], '---', city.night()[1])
    print('Rahukaalam       :', city.rahukaalam()[0], '---', city.rahukaalam()[1])
    print('Region           :', city.region)
    print('Solar Azimuth    :', city.solar_azimuth())
    print('Solar Depression :', city.solar_depression)
    print('Solar Elevation  :', city.solar_elevation())
    print('Solar Midnight   :', city.solar_midnight())
    print('Solar Noon       :', city.solar_noon())
    print('Solar Zenith     :', city.solar_zenith())
    print('Sun              :')#, city.sun())
    print('          Dawn   :', sun['dawn'])
    print('          Sunrise:', sun['sunrise'])
    print('          Noon   :', sun['noon'])
    print('          Sunset :', sun['sunset'])
    print('          Dusk   :', sun['dusk'])
    print('Sunrise          :', city.sunrise())
    print('Sunset           :', city.sunset())
    print('Time At Elevation:', city.time_at_elevation)
    print('Timezone         :', city.timezone)
    print('Twilight         :', city.twilight)
    print('TZ               :', city.tz)
    print('TZinfo           :', city.tzinfo)
    print('Url              :', city.url)
    print('-'*80)

if __name__ == '__main__':

    astral = Astral()

    city = astral['Warsaw']
    info(city)

    loc = Location(('Toruń', 'Poland', 53.022222, 18.611111, 'Europe/Warsaw', 0))
    info(loc)

    for x in astral.geocoder._groups['europe'].keys():
        print(x)

