from flask import Flask, render_template, redirect
from random import randint
from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.validators import DataRequired
import vyhry
app = Flask(__name__)
app.debug = True
app.secret_key = 'kascf ascfhasiocfhasiocfawefawfhasiocfh'
#
class pocet_kostek_form(FlaskForm):
    pocet = StringField("pocet", validators=[DataRequired()])

@app.route('/hod_kostky/<pocet_kostek>')
def hod_kostky(pocet_kostek):
    pocet_kostek2 = []
    skore_hrac = []
    skore_bot = []
    celkove_skore_hrac = 0
    celkove_skore_bot = 0
    for i in range(int(pocet_kostek)):
        pocet_kostek2.append(i)
        skore_hrac.append(randint(1,6))
        skore_bot.append(randint(1,6))
        celkove_skore_hrac += skore_hrac[i]
        celkove_skore_bot += skore_bot[i]
    if celkove_skore_bot== celkove_skore_hrac:
        vyhra = "remíza"
        vyhry.pridej(2)
    elif celkove_skore_bot >= celkove_skore_hrac:
        vyhra = "počítač"
        vyhry.pridej(1)
    elif celkove_skore_bot <= celkove_skore_hrac:
        vyhra = "hráč"
        vyhry.pridej(0)
    
    return render_template('hod_kostky.html', pocet_kostek=pocet_kostek2, celkove_skore_hrac=celkove_skore_hrac, celkove_skore_bot=celkove_skore_bot, vyhra=vyhra, skore_hrac=skore_hrac, skore_bot=skore_bot)

@app.route('/vyber_pocet_hodu_kostky', methods=['POST'])
def prejdi_do_hodu_kostky():
    pocet_hodu = 1
    

@app.route('/', methods=['POST','GET'])
def zacatek():
    form=pocet_kostek_form()
    
    if form.validate_on_submit():
        
            
        if form.pocet.data.isnumeric():
            if int(form.pocet.data) > 0:
                return redirect(f'/hod_kostky/{form.pocet.data}')

        form.pocet.data = "špatně zadaná hodnota!"
        return render_template('index.html', vyhry=vyhry.vrat_pocet(), form=form)
        
    form.pocet.data = 0
    return render_template('index.html', vyhry=vyhry.vrat_pocet(), form=form)
#
if __name__ == '__main__':
    app.run()
#