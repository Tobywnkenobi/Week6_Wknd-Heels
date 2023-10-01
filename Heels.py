from flask import Flask, request


app = Flask(__name__)

@app.route('/index')
def index():
    return 'Heels'

wrestlers = [
    {'wrestler':'Randy Orton',
     'height':'6ft 3in',
     'weight':'285',
     'smack_talk':[{'body':'RKO'}]
     },
     {'wrestler':'Matt Riddle',
     'height':'6ft 2in',
     'weight':'260',
     'smack_talk':[{'body':'BRO'}]
     },
     {'wrestler':'Kevin Owens',
     'height':'5ft 11in',
     'weight':'285',
     'smack_talk':[{'body':'Pop up Power Bomb'}]
     },
     {'wrestler':'Sami Zayne',
     'height':'6ft',
     'weight':'256',
     'smack_talk':[{'body':'Puts the ginga in jinja'}]
     },
     {'wrestler':'Toby',
      'height':'5ft 5in',
      'weight':'223',
      'smack_talk':[{'body':'Fun sized'}]
     }
]

@app.get('/wrester')
def get_wrestler():
    return {'Wrestler': wrestlers}, 200

#routes for each

@app.post('/wrestler')
def create_wrestler():
    wrestler_data = request.get_json()
    wrestlers.append(wrestler_data)
    return wrestler_data, 201

@app.put('/wrestler')
def update_wrestler():
    wrestler_data = request.get_json()
    filtered_wrestlers = list(filter(lambda wrestler: wrestler['wrestler'] == wrestler_data['name'], wrestlers))
    
    if filtered_wrestlers:
        # Update the first matching wrestler's name
        filtered_wrestlers[0]['name'] = wrestler_data['new name']
        return filtered_wrestlers[0], 200
    else:
        return {"message": "Wrestler not found"}, 404

  
    
    
    # wrestler = list(filter(lambda wrestler: wrestler['wrestler_name'] == wrestler_data['wrestler_name'],wrestlers))[0]
    # wrestler['wrestler_name'] = wrestler_data['new_wrestler_name']
    # return wrestlers, 200
    

@app.delete('/wrestler')
def delete_wrestler():
    wrestler_data = request.get_json()
    for wrestler in enumerate(wrestlers):
        if wrestler['wrestler'] == wrestler_data['wrestler']:
            wrestlers.pop(i)
    return {'message':f'{wrestler_data["wrestler"]} deleted'}, 202
