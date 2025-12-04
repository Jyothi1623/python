import pandas as pd

doctors_data = {
    'd_id': [101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116],
    'd_name': ['Dr. Ramesh','Dr. Priya','Dr.Anil','Dr  Sunitha','Dr. Raju','Dr John','Dr. Meena',
               'Dr. Ramesh','Dr. Sneha','Dr Ross','Dr. Ramesh','Dr. Priya','Dr.Anil',
               'Dr  Sunitha','Dr. Raju','Dr John'],
    'specialization': ['Cardiology','Neurology','Orthopedic','Dermatology','General','Cardiology',
                       'ENT','Orthopedic','General Physcian','Cardio','Cardiology','Neurology',
                       'Orthopedic','Dermatology','General','Cardiology'],
    'phone': ['9876543210','98 88 554',None,'88997766','78945612',None,'985623147','954412365',
              '98 44 36',None,'9876543210','98 88 554',None,'88997766','78945612',None]
}

patients_data = {
    'p_id': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
    'p_name': ['Aarav Kumar','Meena Sharma','Rajesh Patel','Sita Devi','Vikram Singh',
               'Neha Verma','Anil Kumar','Pooja Sharma','Ravi Teja','Lakshmi Rao',
               'Suresh Reddy','Ananya Gupta','Deepak Yadav','Kavya Nair','Mohit Jain',
               'Nisha Patel','Harish Kumar','Sneha Kapoor','Ajay Rana','Divya Sharma'],
    'age': [45,32,56,28,50,38,60,30,42,26,47,34,52,29,39,41,48,31,55,37],
    'gender': ['Male','Female','Male','Female','Male','Female','Male','Female','Male',
               'Female','Male','Female','Male','Female','Male','Female','Male','Female','Male','Female'],
    'problem': ['Chest Pain','Migraine','Joint Pain','Skin Allergy','Fever & Cold',
                'Heart Discomfort','Hearing Issue','Knee Swelling','High BP','Skin Rash',
                'Chest Tightness','Memory Loss','Joint stiffness','Weakness','Ear Infection',
                'Breathing Issue','Skin Itching','Vertigo','Knee Pain','Fever & Cold'],
    'assigned_doctor': ['Dr. Ramesh','Dr. Priya','Dr.Anil','Dr  Sunitha','Dr. Raju',
                        'Dr John','Dr. Meena','Dr.Anil','Dr Ross','Dr  Sunitha','Dr. Ramesh',
                        'Dr. Priya','Dr.Anil','Dr  Sunitha','Dr. Raju','Dr John',
                        'Dr  Sunitha','Dr. Priya','Dr.Anil','Dr. Raju']
}

appointment_data = {
    'app_id': [201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216],
    'p_id': [1,6,7,2,9,5,8,4,3,10,11,12,13,14,15,16],
    'd_id': [101,101,101,102,102,103,103,105,104,106,101,102,104,105,103,106],
    'date': ['2024-08-12','2024-09-10','2024-10-11','2024-09-05','2024-10-20',
             '2024-07-25','2024-08-22','2024-11-07','2024-10-15','2024-11-13',
             '2024-08-18','2024-09-12','2024-10-20','2024-11-10','2024-07-28','2024-11-22'],
    'diagnosis': ['Chest pain','Severe heart ache','BP & heart issue','Headack & stress',
                  'Migrain & dizzy','Knee Swelling','Joint pain','High Sugr',
                  'Rash & Itching','Chest tightness','Chest discomfort','Memory loss',
                  'Skin allergy','Weakness','Joint stiffness','Heavy breathing']
}


df_doctors = pd.DataFrame(doctors_data)
df_patients = pd.DataFrame(patients_data)
df_appointment = pd.DataFrame(appointment_data)


df_doctors.drop_duplicates(inplace=True)

df_doctors['d_name'] = df_doctors['d_name'].str.replace(r"\s+", " ", regex=True).str.strip()

df_doctors['specialization'] = df_doctors['specialization'].replace({
    'Cardio': 'Cardiology',
    'General Physcian': 'General Physician'
})
df_appointment['diagnosis'] = df_appointment['diagnosis'].replace({
    "High Sugr": "High Sugar"
})

df_doctors['phone'] = df_doctors['phone'].astype(str)
df_doctors['phone'] = df_doctors['phone'].str.replace(" ", "")
df_doctors['phone'] = df_doctors['phone'].replace(['None', 'nan', 'NaN'], '')
df_doctors['phone'] = df_doctors['phone'].str.replace(r"\D", "", regex=True)
df_doctors.loc[df_doctors['phone'].str.len() != 10, 'phone'] = "Not Available"


df_patients['assigned_doctor'] = df_patients['assigned_doctor'].str.replace(r"\s+", " ", regex=True).str.strip()
df_patients['problem'] = df_patients['problem'].str.title()


df_appointment['date'] = pd.to_datetime(df_appointment['date'])
df_appointment['diagnosis'] = df_appointment['diagnosis'].str.title()
df_appointment['diagnosis'] = df_appointment['diagnosis'].str.replace(r"\s+", " ", regex=True)


print("\nCLEAN DOCTORS DATA:\n", df_doctors)
print("\nCLEAN PATIENTS DATA:\n", df_patients)
print("\nCLEAN APPOINTMENTS DATA:\n", df_appointment)
