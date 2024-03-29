from flask import Flask, send_from_directory
from flask_restful import Api
from flask_jwt_extended import JWTManager
from user_resource import UserResource, UsersResource, UserLoginResource
from authorization_resource import AuthorizationResource, AuthorizationsResource
from doctor_resource import DoctorResource, DoctorsResource
from patient_resource import PatientResource, PatientsResource
from disease_resource import DiseaseResource, DiseasesResource
from appointment_resource import AppointmentResource, AppointmentsResource
from symptom_resource import SymptomResource, SymptomsResource
from models import db, User, Authorization, Doctor, Patient, Symptom, Disease, Appointment
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

app = Flask(
    __name__,
    static_url_path='/static',
    static_folder='client/my-app/dist',
    template_folder='client/my-app/dist'
)

# Load environment variables from .env file
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///health_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'default_secret_key')
jwt = JWTManager(app)
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)
CORS(app, origins=["*"])

# Add API resources here using the resource classes
api.add_resource(UserResource, '/user/<int:user_id>')
api.add_resource(UsersResource, '/users')
api.add_resource(UserLoginResource, '/login')

api.add_resource(AuthorizationResource, '/authorization/<int:authorization_id>')
api.add_resource(AuthorizationsResource, '/authorizations')

api.add_resource(DoctorResource, '/doctor/<int:doctor_id>')
api.add_resource(DoctorsResource, '/doctors')

api.add_resource(PatientResource, '/patient/<int:patient_id>')
api.add_resource(PatientsResource, '/patients')

api.add_resource(SymptomResource, '/symptom/<int:symptom_id>')
api.add_resource(SymptomsResource, '/symptoms')

api.add_resource(DiseaseResource, '/disease/<int:disease_id>')
api.add_resource(DiseasesResource, '/diseases')

api.add_resource(AppointmentResource, '/appointment/<int:appointment_id>')
api.add_resource(AppointmentsResource, '/appointments')


# Serve the index.html file
@app.route('/')
@app.route('/<int:id>')
def index(id=0):
    return ("index.html")

if __name__ == '__main__':
    app.run()
