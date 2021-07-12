from detect import run


# Currently for regular camera maybe find a way to decide if there is a depth camera and otherwise use input 0?

def update_things(thing):
    print(thing)
    if thing[0] == 'chair':
        print('FUCK YEAH')

run(things=update_things,source='1',nosave=True)
