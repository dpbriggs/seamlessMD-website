from flask import Flask, render_template
import json

# Ideally the patient data should come from
# a database or a more serious storage.

patient_data_file = 'patient[3]_fixed.json'


def get_patient_data():
    with open(patient_data_file, 'rb') as f:
        return json.load(f)


def format_patient_data(patient_data):
    organization_name = patient_data\
                        .get('managingOrganization', {})\
                        .get('display', '?')
    conditions = patient_data.get('conditions', [])
    return {
        'given_name': patient_data.get('name', [{}])[0].get('given', '?')[0],
        'family_name': patient_data.get('name', [{}])[0].get('family', '?')[0],
        'organization_name': organization_name,
        'gender': patient_data.get('gender', '').title(),
        'number_condition': len(conditions),
        'conditions': conditions
    }


seamlessMDWebsite = Flask(__name__)

# As we serve the same data over and over again, we can just
# store it.

patient_data = get_patient_data()
formatted_patient_data = format_patient_data(patient_data)


@seamlessMDWebsite.route('/')
def root_page():
    return render_template('main.html', context=formatted_patient_data)


if __name__ == "__main__":
    seamlessMDWebsite.run(host="0.0.0.0", port=8080)
