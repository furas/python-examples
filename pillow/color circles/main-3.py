from PIL import Image, ImageDraw, ImageChops

def synthese(red=255, green=255, blue=255, file_prefix=''):

    # transparent images
    image_R = Image.new('RGBA', (450, 450), 0)
    image_G = Image.new('RGBA', (450, 450), 0)
    image_B = Image.new('RGBA', (450, 450), 0)
    
    # draw circle on red layer
    draw_R = ImageDraw.Draw(image_R)
    draw_R.ellipse((10,150,300,440), (red, 0, 0))
    
    # draw circle on green layer
    draw_G = ImageDraw.Draw(image_G)
    draw_G.ellipse((150,150,440,440), (0, green, 0))
    
    # draw circle on blue layer
    draw_B = ImageDraw.Draw(image_B)
    draw_B.ellipse((75,10,375,300), (0, 0, blue))
    
    result = ImageChops.add(image_R, image_G, 0.5)
    result = ImageChops.add(result, image_B, 0.5)
    
    #result.save(file_prefix + 'add_RGB.png')
    result.show()
    
synthese(255, 255, 255, 'normal_')

