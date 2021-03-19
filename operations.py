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
def get_totalrun_time():
    log_file=open("runtime.log",'r+')
    time=log_file.read()
    if len(time)==0:
        log_file.write('0')
        log_file.close()
        return 0
    else:
        log_file.close()
        return str(round(int(time)/60,2))

def set_totalrun_time(x):
    log_file = open("runtime.log", 'r')
    oldtime=log_file.read()
    print(oldtime,type(oldtime))
    log_file.close()
    log_file = open("runtime.log", 'w')
    log_file.write(str(x))
    log_file.close()
    print("runtime updated")
