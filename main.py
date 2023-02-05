import eel

eel.init('eelstuff')

@eel.expose
def get_data():
    return 'Data'


eel.start('index.html')