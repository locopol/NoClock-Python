import schedule, time, json, requests, threading, queue
import importlib

#POR AGREGAR:
#  - LAST VIDEO VIEW COUNT YOUTUBE
#  - LIVE COUNT TWITCH (VALIDAR SOLO MODO ONLINE)
#  - REDDIT KARMA (FOR FUN)

#API Keys
noclock_apikey = "<noclock apikey>"
noclock_host = "<noclock ip x.x.x.x>"
noclock_port = "5000"
def_remaining_time = 5

t = threading.Thread()
q = queue.Queue()
ev = threading.Event()


# Para darle sonido (mejorar)
def get_sound(name):
    if (name == 'sound1'):
        return 'https://assets.mixkit.co/active_storage/sfx/2868/2868-preview.mp3'
    if (name == 'sound2'):
        return 'https://assets.mixkit.co/active_storage/sfx/2344/2344-preview.mp3'
    if (name == 'sound3'):
        return 'https://assets.mixkit.co/active_storage/sfx/951/951-preview.mp3'
    if (name == 'sound4'):
        return 'https://dm0qx8t0i9gc9.cloudfront.net/previews/audio/BsTwCwBHBjzwub4i4/audioblocks-bells-positive-sound_BKqfVgMUAvU_NWM.mp3'

def notification(**params):
    global q, def_remaining_time
    if ('msg' in params):
        print("Preparing ... Queued ... ")
        myobj = {"icon": {
                 "x": 1,
                 "y": 10,
                 "value": params['icon']
                },
                 "message":
                 { "x": 10,
                   "y": 1,
                   "value": params['msg']
                }
                }
        if ('time' in params):
            myobj['remaining_time'] = params['time']
        else:
            myobj['remaining_time'] = def_remaining_time

        if ('snd' in params):
            myobj['sound'] = params['snd']

        q.put(myobj)
        
        if('once' in params):
            return schedule.CancelJob
        
    else:
        q.put(params['myObj'])
        return "Queued ... "

def worker():
    global q
    try:
        while True:
            if ev.is_set():
                break
            else:
                item = q.get()
                url = 'http://' + noclock_host + ':' + noclock_port + '/notification'
                x = requests.post(url, json = item, headers = {"api-key": noclock_apikey})
                q.task_done()
                print(x.text)
                time.sleep(item["remaining_time"])
    except Exception as e:
        print(e)
        q.task_done()
        print("error en worker, liberando queue, finalizando ...")
        return


import modules
if __name__ == "__main__":
    for module in modules.__all__:
        importlib.import_module('modules.'+module).main()
        
try:
    print("Starting")
    url = 'http://' + noclock_host + ':' + noclock_port + '/js/lib/vue/vue.js'
    x = requests.get(url)
    if(x.status_code == 200):
        obj = {"icon": { "x": 1, "y": 10, "value": "call" }, "message": { "x": 10, "y": 12, "value": "Connected"}, "remaining_time": 3, "sound": get_sound("sound4") }
        print("Connected ... " + notification(myObj=obj))

    # Turn-on the worker thread.
    t = threading.Thread(target=worker, daemon=True)
    t.start()
    print("Started...")
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        q.join()
        t.join(0.1)
        if not t.is_alive():
            break
            
except requests.exceptions.ConnectionError:
    print("Not Connected, exiting ...")
    ev.set()

except KeyboardInterrupt:
    ev.set()
    t.join(0.1)
    print("exit")
except Exception as e:
    ev.set()
    print(e)
    print("Exit Shedule.")
