from flask import Flask, request


app = Flask(__name__)

@app.route('/index')
def index():
    return 'Heels'

Heels = [
    {'stagename':'Randy Orton',
     'height':'6ft 3in',
     'weight':'285',
     'smack_talk':[{'body':'RKO'}]
     },
     {'stagename':'Matt Riddle',
     'height':'6ft 2in',
     'weight':'260',
     'smack_talk':[{'body':'BRO'}]
     },
     {'stagename':'Kevin Owens',
     'height':'5ft 11in',
     'weight':'285',
     'smack_talk':[{'body':'Pop up Power Bomb'}]
     },
     {'stagename':'Sami Zayne',
     'height':'6ft',
     'weight':'256',
     'smack_talk':[{'body':'Puts the ginga in jinja'}]
     }
]

@app.get('/Heel')
def get_Heels():
    return {'Heels': Heels}

#routes for each

@app.post('/Heel')
def create_Heel():
    Heel_data = request.get_json()
    print (Heel_data)    

# @app.put('/Heel')
#     pass
# @app.delete('/Heel')
#     pass
