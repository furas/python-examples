from PIL import Image, ImageDraw

def synthese(red=255, green=255, blue=255, background=0, file_prefix=''):

    # layers in greyscale
    layer_R = Image.new('L', (450, 450), background)
    layer_G = Image.new('L', (450, 450), background)
    layer_B = Image.new('L', (450, 450), background)
    
    # draw circle on red layer
    draw_R = ImageDraw.Draw(layer_R)
    draw_R.ellipse((10,150,300,440), red)
    
    # draw circle on green layer
    draw_G = ImageDraw.Draw(layer_G)
    draw_G.ellipse((150,150,440,440), green)
    
    # draw circle on blue layer
    draw_B = ImageDraw.Draw(layer_B)
    draw_B.ellipse((75,10,375,300), blue)
    
    #layer_R.show()               
    #layer_G.show()               
    #layer_B.show()

    layer_R.save(file_prefix + 'layer_r.png')
    layer_G.save(file_prefix + 'layer_g.png')
    layer_B.save(file_prefix + 'layer_b.png')
    
    # create RGB image using greyscale layers
    image_RGB = Image.merge('RGB', (layer_R, layer_G, layer_B))
    
    # show it
    image_RGB.show()               
    image_RGB.save(file_prefix + 'rgb.png')
    
synthese(255, 255, 255, 0, 'normal_')
synthese(0, 0, 0, 255, 'inverted_')
