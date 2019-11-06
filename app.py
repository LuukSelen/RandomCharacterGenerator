import random
import names
from flask import Flask, render_template, request

import sys
sys.path.insert(0, 'char-attributes')
from countries import country as countries_attr
from races import race as races_attr
from genders import gender as genders_attr
from occupations import occupation as occupations_attr
from fantasy_names import town as towns_attr
from fantasy_names import fantasy_name as fantasy_names_attr
from titles import title as titles_attr
from hair_colours import hair_colour as hair_colours_attr
from backstories import backstory as backstories_attr
from traits import trait as traits_attr
from skin_colours import skin_colour as skin_colours_attr
from eye_colours import eye_colour as eye_colours_attr

app = Flask(__name__)
link_cell = True

@app.route('/', methods=['GET', 'POST'])
def home():
    
    if request.method == 'POST':
        searchword = request.form['text']
    else:
        searchword = request.args.get('name', '')
    if searchword:
        first_name = searchword
    else:
        first_name = random.choice(fantasy_names_attr)
    attributes = {
        'First Name': first_name,
        'Last Name': random.choice(fantasy_names_attr),
        'Title': random.choice(titles_attr),
        'Class': random.choice(occupations_attr),
        'Age': random.randint(18, 300),
        'Gender': random.choice(genders_attr),
        'Race': random.choice(races_attr),
        'Country': random.choice(countries_attr),
        'Hair Colour': random.choice(hair_colours_attr),
        'Skin Colour': random.choice(skin_colours_attr),
        'Eye Colour': random.choice(eye_colours_attr),
        'Trait 1': random.choice(traits_attr),
        'Trait 2': random.choice(traits_attr),
        'Trait 3': random.choice(traits_attr),
        'Flavour 1': random.choice(backstories_attr),
        'Flavour 2': random.choice(backstories_attr),
        'Flavour 3': random.choice(backstories_attr),
    }
    return render_template('home.html', attributes = attributes.items())

# @app.route('/', methods=['POST'])
# def my_form_post():
#     text = request.form['text']
#     processed_text = text.upper()
#     return processed_text

@app.route('/all-categories')
def all_categories():
    return render_template('archive_categories.html')

@app.route('/races')
def races():
    return render_template('single_category.html', name="Races", link_cell=link_cell, attr = races_attr)

@app.route('/ages')
def age():
    ages_attr = list(range(18, 300))
    return render_template('single_category.html', name="Ages", attr = ages_attr)

@app.route('/countries')
def countries():
    return render_template('single_category.html', name="Countries", link_cell=link_cell, attr = countries_attr)

@app.route('/classes')
def occupations():
    return render_template('single_category.html', name="Classes", link_cell=link_cell, attr = occupations_attr)

@app.route('/titles')
def titles():
    return render_template('single_category.html', name="Titles", attr = titles_attr)

@app.route('/backstories')
def backstories():
    return render_template('single_category.html', name="Backstories", attr = backstories_attr)
    
# @app.route('/secrets')
# def traits():
#     return render_template('single_category.html', name="Secrets", attr = secrets_attr)
    
@app.route('/traits')
def traits():
    return render_template('single_category.html', name="Traits", attr = traits_attr)