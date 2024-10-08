from models import User, session

users = [
    User(first_name='Ahmed', last_name='Almaliki', salary=60000.0, education_level='Master', age=35),
    User(first_name='Layla', last_name='Alhasni', salary=45000.0, education_level='Bachelor', age=28),
    User(first_name='Ali', last_name='Bensalem', salary=52000.0, education_level='PhD', age=40),
    User(first_name='Fatima', last_name='Alali', salary=47000.0, education_level='Bachelor', age=26),
    User(first_name='Youssef', last_name='Alrefai', salary=62000.0, education_level='Master', age=33),
]

# Add the users to the session
session.add_all(users)

# Commit the session to save the new users in the database
session.commit()

print("New users added successfully!")
