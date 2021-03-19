import datetime


def runtimer(run_min):
    now = datetime.datetime.now()
    start_time = now.strftime("%H:%M")
    future= now + datetime.timedelta(minutes = run_min)
    stop_time=future.strftime("%H:%M")
    print("Timer will stop at:",stop_time)
    FMT = '%H:%M'
    tdelta = datetime.datetime.strptime(stop_time, FMT) - datetime.datetime.strptime(start_time, FMT)
    str_tdata=str(tdelta).split(':')
    min=(int(str_tdata[0])*60)+int(str_tdata[1])
    lasttime=min
    while lasttime!=0:
        now = datetime.datetime.now()
        start_time = now.strftime("%H:%M")
        tdelta = datetime.datetime.strptime(stop_time, FMT) - datetime.datetime.strptime(start_time, FMT)
        str_tdata = str(tdelta).split(':')
        min = (int(str_tdata[0]) * 60) + int(str_tdata[1])
        if min==lasttime:
            pass
        else:
            print("left time: ",min)
            lasttime=min
    print("Stop")


runtimer(2)
