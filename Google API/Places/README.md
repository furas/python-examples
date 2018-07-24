# Google Places API

This code uses [Python Client for Google Maps Services](https://github.com/googlemaps/google-maps-services-python) to get names and locations (and more) for query `'Rugby Club, London'`

    pip install --upgrade googlemaps


It needs private API key (`key=`) to work. 

To get API key you have to 

- create account on Google (ie. Gmail) if you don't have it.

- create new project on [developers.google.com/console](https://developers.google.com/console), 

- in `Library` on [developers.google.com/console](https://developers.google.com/console) (in menu on left side) activate `Places API Web Service` 
  (there is no version for `Desktop Application`) 

- create credencial for `PlacesAPI` - it will give you API key.

---

Result: (available keys and some names and locations)

    key: formatted_address
    key: geometry
    key: icon
    key: id
    key: name
    key: opening_hours
    key: photos
    key: place_id
    key: plus_code
    key: rating
    key: reference
    key: types    

    -----
    name: East London Rugby Football Club
    lat: 51.5291765
    lng: 0.0102242
    location: {'lat': 51.5291765, 'lng': 0.0102242}
    ---
    name: Hampstead Rugby Football Club
    lat: 51.5571358
    lng: -0.1555037
    location: {'lat': 51.5571358, 'lng': -0.1555037}
    ---
    name: Chiswick Rugby Club
    lat: 51.47323
    lng: -0.256633
    location: {'lat': 51.47323, 'lng': -0.256633}
    ---
    name: Wimbledon Rugby Football Club
    lat: 51.41975009999999
    lng: -0.2464434
    location: {'lat': 51.41975009999999, 'lng': -0.2464434}
    ---
    name: Saracens Amateur RFC
    lat: 51.64230209999999
    lng: -0.1429848
    location: {'lat': 51.64230209999999, 'lng': -0.1429848}
    ---
    name: Kilburn Cosmos RFC
    lat: 51.55542000000001
    lng: -0.2297043000000001
    location: {'lat': 51.55542000000001, 'lng': -0.2297043000000001}
    ---
    name: Barnes Rugby Football Club
    lat: 51.47568860000001
    lng: -0.2373847
    location: {'lat': 51.47568860000001, 'lng': -0.2373847}
    ---
    name: Southwark Tigers Rugby Club
    lat: 51.4839377
    lng: -0.07720149999999999
    location: {'lat': 51.4839377, 'lng': -0.07720149999999999}
    ---
    name: HACKNEY RFC
    lat: 51.5732467
    lng: -0.0611062
    location: {'lat': 51.5732467, 'lng': -0.0611062}
    ---
    name: UCS Old Boys Rugby Club
    lat: 51.5575127
    lng: -0.2022654
    location: {'lat': 51.5575127, 'lng': -0.2022654}
    ---
    name: Millwall Rugby Club
    lat: 51.487884
    lng: -0.010493
    location: {'lat': 51.487884, 'lng': -0.010493}
    ---
    name: Haringey Rhinos RFC
    lat: 51.604738
    lng: -0.099553
    location: {'lat': 51.604738, 'lng': -0.099553}
    ---
    name: Finchley RFC
    lat: 51.6067705
    lng: -0.1698911
    location: {'lat': 51.6067705, 'lng': -0.1698911}
    ---
    name: Trailfinders Rugby Club
    lat: 51.520878
    lng: -0.306115
    location: {'lat': 51.520878, 'lng': -0.306115}
    ---
    name: Old Ruts Rugby Club
    lat: 51.4079431
    lng: -0.1993505
    location: {'lat': 51.4079431, 'lng': -0.1993505}
    ---
    name: Ealing Trailfinders Rugby Club
    lat: 51.524832
    lng: -0.3293849999999999
    location: {'lat': 51.524832, 'lng': -0.3293849999999999}
    ---
    name: Chingford Rugby Football Club
    lat: 51.6301123
    lng: -0.0171661
    location: {'lat': 51.6301123, 'lng': -0.0171661}
    ---
    name: Old Elthamians RFC Senior Rugby
    lat: 51.43445149999999
    lng: 0.0296538
    location: {'lat': 51.43445149999999, 'lng': 0.0296538}
    ---
    name: Eton Manor RFC
    lat: 51.579528
    lng: 0.03874
    location: {'lat': 51.579528, 'lng': 0.03874}
    ---
    name: London Skolars Rugby League Club
    lat: 51.60465900000001
    lng: -0.100032
    location: {'lat': 51.60465900000001, 'lng': -0.100032}
    ---
