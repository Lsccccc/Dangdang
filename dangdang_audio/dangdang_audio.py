import pygame, time
mixer = pygame.mixer
mixer.init( 11025 )
#music = mixer.music

#path = os.path
#curr_dir = path.dirname( path.abspath( __file__ ) )

def play(file_path,debug=False):
    sound = mixer.Sound(file_path)
    sound.set_volume( 5 )
    channel = sound.play()
    if debug:
        print( sound.get_length() )
    while channel.get_busy() :
        time.sleep(0.1)
    sound.stop()
