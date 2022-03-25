import requests

#url = 'https://gis2.westberks.gov.uk/arcgis/rest/services/maps/Wbc_Highways/MapServer/11/query?f=json&returnGeometry=true&spatialRel=esriSpatialRelIntersects&geometry=%7B%22xmin%22%3A442520.89976831735%2C%22ymin%22%3A178788.66371417744%2C%22xmax%22%3A443314.65135582053%2C%22ymax%22%3A179582.41530168062%2C%22spatialReference%22%3A%7B%22wkid%22%3A27700%2C%22latestWkid%22%3A27700%7D%7D&geometryType=esriGeometryEnvelope&inSR=27700&outFields=OBJECTID%2CItem_Type%2CItem_Identity_Code%2CLocation_Description%2CAssigned_Street%2CLocality%2CTown%2CType%2CBracket_Type%2CLantern_Type%2CLamp_Type%2CBallast_Type%2CControl_Type%2CSign_Lantern_Type%2CSign_Bracket_Type%2CSign_Post_Type%2CBollard_Base_Type%2CBollard_Shell_Type%2CColumn_Manufacturer%2CMaterial_Type%2CLamp_Wattage%2CLantern_Manufacturer%2CNumber_of_Lamps%2CSwitching_Regime_Code%2CSwitching_Regime%2CLamp_Type2%2CEasting%2CNorthing&outSR=27700'

params = {
    'f': ['json'],
    'geometry': [
         '{"xmin":442520.89976831735,"ymin":178788.66371417744,"xmax":443314.65135582053,"ymax":179582.41530168062,"spatialReference":{"wkid":27700,"latestWkid":27700}}'
    ],
    'geometryType': ['esriGeometryEnvelope'],
    'inSR': ['27700'],
    'outFields': ['OBJECTID,Item_Type,Item_Identity_Code,Location_Description,Assigned_Street,Locality,Town,Type,Bracket_Type,Lantern_Type,Lamp_Type,Ballast_Type,Control_Type,Sign_Lantern_Type,Sign_Bracket_Type,Sign_Post_Type,Bollard_Base_Type,Bollard_Shell_Type,Column_Manufacturer,Material_Type,Lamp_Wattage,Lantern_Manufacturer,Number_of_Lamps,Switching_Regime_Code,Switching_Regime,Lamp_Type2,Easting,Northing'],
    'outSR': ['27700'],
    'returnGeometry': ['true'],
    'spatialRel': ['esriSpatialRelIntersects']
}

url = 'https://gis2.westberks.gov.uk/arcgis/rest/services/maps/Wbc_Highways/MapServer/11/query'

response = requests.get(url, params=params)
#print(response.url)
#print(response.status_code)

data = response.json()

for item in data['features']:
    print('Locality:', item['attributes']['Locality'].strip())
    print('Town    :', item['attributes']['Town'].strip())
    print('Street  :', item['attributes']['Assigned_Street'].strip())
    print('Geometry:', item['geometry'])
    print('---')

