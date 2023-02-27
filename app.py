from flask import Flask,render_template,flash,redirect,url_for,request, jsonify
from models import db,connect_db,Pet
from forms import AddPetForm,EditPetForm
app = Flask(__name__)
app.config["SECRET_KEY"] = "shhh"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
from flask_debugtoolbar import DebugToolbarExtension
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLACLCHEMY_TRACK_MODIFICATIONS'] = False

debug = DebugToolbarExtension(app)

app.app_context().push()
connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    """Displays home page"""

    pets = Pet.query.all()

    return render_template('homepage.html',pets=pets)

@app.route('/add', methods=["GET","POST"])
def add_pet():
    """adds pet to database"""

    form = AddPetForm()

    if form.validate_on_submit():
        data = {k:v for k,v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} has been added!")
        return redirect(url_for('home_page'))
    else:
        return render_template('pet_add_form.html', form = form)
    
@app.route('/<int:pet_id>', methods = ["GET","POST"])
def edit_pet(pet_id):
    """Edits desired pet"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm()

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} has been updated!")
        return redirect(url_for('home_page'))
    else:
        return render_template('pet_edit_form.html',form=form, pet=pet)
    
@app.route('/api/pets/<int:pet_id>', methods=['GET'])
def get_pet_api(pet_id):
    """Returns info about pet with JSON"""
    pet = Pet.query.get_or_404(pet_id)
    info = {"name":pet.name, "age":pet.age}
    return jsonify(info)

