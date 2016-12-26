#!/usr/bin/env python3

from astral import AstralGeocoder, Location

#Astral', 'AstralError', 'AstralGeocoder', 'GoogleGeocoder', 'Location', 'LocationGroup', 'SUN_RISING', 'SUN_SETTING', 'SunBelowHorizonError', 'URLError', '_LOCATION_INFO'

if __name__ == '__main__':

    coder = AstralGeocoder()

    for group in coder._groups:
        print('---', group, '---')
        
        for city in coder._groups[group]:
            print(city.name)

