# Google Geocoding API

This code uses [Python Client for Google Maps Services](https://github.com/googlemaps/google-maps-services-python) to get location (and more) for query `'221B Baker Street, London, United Kingdom'`

    pip install --upgrade googlemaps


It needs private API key (`key=`) to work. 

To get API key you have to 

- create account on Google (ie. Gmail) if you don't have it.

- create new project on [developers.google.com/console](https://developers.google.com/console), 

- in `Library` on [developers.google.com/console](https://developers.google.com/console) (in menu on left side) activate `Geocoding API` 

- create credencial for `Geocoding API` - it will give you API key.

---

Result: (available keys and all informations)

    key: address_components
    key: formatted_address
    key: geometry
    key: place_id
    key: types
    -----
    formatted_address: 221B Baker St, Marylebone, London NW1 6XE, UK
    lat: 51.523767
    lng: -0.1585557
    location: {'lat': 51.523767, 'lng': -0.1585557}
    {'long_name': '221B', 'short_name': '221B', 'types': ['street_number']}
    {'long_name': 'Baker Street', 'short_name': 'Baker St', 'types': ['route']}
    {'long_name': 'Marylebone', 'short_name': 'Marylebone', 'types': ['neighborhood', 'political']}
    {'long_name': 'London', 'short_name': 'London', 'types': ['postal_town']}
    {'long_name': 'Greater London', 'short_name': 'Greater London', 'types': ['administrative_area_level_2', 'political']}
    {'long_name': 'England', 'short_name': 'England', 'types': ['administrative_area_level_1', 'political']}
    {'long_name': 'United Kingdom', 'short_name': 'GB', 'types': ['country', 'political']}
    {'long_name': 'NW1 6XE', 'short_name': 'NW1 6XE', 'types': ['postal_code']}
    ---
    address_components: [{'long_name': '221B', 'short_name': '221B', 'types': ['street_number']}, {'long_name': 'Baker Street', 'short_name': 'Baker St', 'types': ['route']}, {'long_name': 'Marylebone', 'short_name': 'Marylebone', 'types': ['neighborhood', 'political']}, {'long_name': 'London', 'short_name': 'London', 'types': ['postal_town']}, {'long_name': 'Greater London', 'short_name': 'Greater London', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'England', 'short_name': 'England', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'United Kingdom', 'short_name': 'GB', 'types': ['country', 'political']}, {'long_name': 'NW1 6XE', 'short_name': 'NW1 6XE', 'types': ['postal_code']}]
    formatted_address: 221B Baker St, Marylebone, London NW1 6XE, UK
    geometry: {'bounds': {'northeast': {'lat': 51.52379759999999, 'lng': -0.1584259}, 'southwest': {'lat': 51.52370519999999, 'lng': -0.1587058}}, 'location': {'lat': 51.523767, 'lng': -0.1585557}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 51.5251003802915, 'lng': -0.157216869708498}, 'southwest': {'lat': 51.5224024197085, 'lng': -0.159914830291502}}}
    place_id: ChIJEYJiM88adkgR4SKDqHd2XUQ
    types: ['premise']
