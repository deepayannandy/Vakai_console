import os
import pygame



current_path=os.getcwd()
####################################### Music related functions #############################################
pygame.mixer.init()
songname=''
volume=.5
started=0
def play_music():
    if len(songname)>0:
        music=current_path+'/music/'+songname+'.mp3'
        pygame.mixer.music.load(music)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loops=-1)
def stop_music():
    pygame.mixer.music.stop()
def music_pause():
    pygame.mixer.music.pause()
def music_unpause():
    pygame.mixer.music.unpause()
def changevol(x):
    pygame.mixer.music.set_volume(x)

#######################################  Control related functions #######################################
f1=5
f2=5
m1=5
m2=5
def serial_update():
    print('speed update to:',f1,f2,m1,m2)
def serial_stop():
    print("serial_stop")

#######################################  runtime related functions #######################################
def totalrun_time():
    x=10
    return x