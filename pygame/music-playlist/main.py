import pygame

NEXT = pygame.USEREVENT + 1

playlist = [
    "Muzyka/efect/Shotgun 12 gauge sPAs-12 semi automatic single shot distant.mpeg",
    "Muzyka/efect/Shotgun blast shot_BLASTWAVEFX_31658.mp3",
    'track_one.ogg',
    'track_two.ogg',
    'track_three.ogg',
    'track_four.ogg',
]

tracks_number = len(playlist)
current_track = 0

pygame.init() # need it for event loop
#screen = pygame.display.set_mode((800,600)) # it can be useful to stop program 

pygame.mixer.init(frequency = 48000)

# start first track
pygame.mixer.music.load(playlist[current_track])
pygame.mixer.music.play()

# send event NEXT when tracks ends
pygame.mixer.music.set_endevent(NEXT) 

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == NEXT:
            
            # get next track (modulo number of tracks)
            current_track = (current_track + 1) % tracks_number
            
            print("Play:", playlist[current_track])
            
            pygame.mixer.music.load(playlist[current_track])
            pygame.mixer.music.play()

            
pygame.quit()

