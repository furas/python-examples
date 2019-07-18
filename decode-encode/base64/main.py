import base64

def path_decode(filename):

    bytes_name = filename.encode('utf-8')
    encodig_path = base64.b64encode(bytes_name)
    print(encodig_path)

    bytes_name = base64.b64decode(encodig_path)
    filename = bytes_name.decode('utf-8')
    print(filename)

image_file_name = r'C:\Users\User_Name\Documents\photos\photo.png'
path_decode(image_file_name)

