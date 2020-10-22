from flask import session
def vrat_pocet():
    if not 'hrac_vyhry' in session:
        hrac_vyhry = 0
        session['hrac_vyhry'] = 0
    else:
        hrac_vyhry = session['hrac_vyhry']
    if not 'bot_vyhry' in session:
        bot_vyhry = 0
        session['bot_vyhry'] = 0
    else:
        bot_vyhry = session['bot_vyhry']
    if not 'remizy' in session:
        remizy = 0
        session['remizy'] = 0
    else:
        remizy = session['remizy']
    hry_celkove = hrac_vyhry + bot_vyhry + remizy
    return hrac_vyhry, bot_vyhry, remizy, hry_celkove;

def pridej(vyhry):#0 - hráč, 1 - bot, 2 - remíza
    if vyhry == 0:
        session['hrac_vyhry'] = session['hrac_vyhry'] + 1
    elif vyhry == 1:
        session['bot_vyhry'] = session['bot_vyhry'] + 1
    elif vyhry == 2:
        session['remizy'] = session['remizy'] + 1
    return;