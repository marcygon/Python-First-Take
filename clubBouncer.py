min_age_limit = 18
max_age_limit = 30
actual_year = 2023

def club_entry (min_age, max_age):
    user_input = int(input('How old are you?'))

    if user_input >= min_age and user_input <= max_age:
        print('You can pass')
    else:
        print('Out of the line, you are not allowed to enter')

def rude_club_entry (min_age, max_age, year):
    user_age = int(input('How old are you?'))

    if not (min_age <= user_age <= max_age):
        print('Get the hell out of my sight')
        return

    user_id_year = int(input('According to your ID, in which year were you born?'))

    if user_id_year != year - user_age:
        print('Are you joking? OUT!')
        return

    is_true = input('Are you telling me the truth? y/n ')

    if is_true.lower() != 'y':
        print('Don\'t make me waste my time kicking your ass out, and I don\'t want to see you here again')
        return

    print('You can pass')

#club_entry(min_age_limit, max_age_limit)
rude_club_entry(min_age_limit, max_age_limit, actual_year)