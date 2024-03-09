import numpy as np 
import pandas as pd 
import os
from dotenv import load_dotenv
from database import Database
from datacleaning import delete_hard
from analysis import timeslot_week_disklike,timeslot_week_popular,timeslot_overall_dislike,timeslot_overall_popular,timeslot_workday_popular,timeslot_workday_dislike,timeslot_eight_opinion, k_means_clus_combination_weekday_index_wanted,cluster_timeslots_based_on_index_wanted,average_preference_timeslot
from visualization import visualize_unpopular, test



load_dotenv()


db_config = {
    'database': os.getenv("DB_DATABASE"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'host': os.getenv("DB_HOST"),
    'port': os.getenv("DB_PORT") 
    }

print(db_config)    

postgres=Database(**db_config)
postgres.connect()
#SQL Statements geschrieben
preferences=postgres.execute_and_fetchall("SELECT constraint_type, constraint_value, start_time, end_time, weekday,timeslot_index  FROM public.employee_timeslot_constraints")
preferences_dozenten=postgres.execute_and_fetchall("SELECT constraint_type, constraint_value,start_time, end_time,weekday,timeslot_index FROM public.employee_timeslot_constraints AS et JOIN employees ON employee_abbreviation = employees.abbreviation JOIN employee_types ON employees.fk_employee_type_id = employee_types.id where employee_types.name='Dozierende' group by et.id,employee_types.name")

#schließen der Verbindung
postgres.close()

#Preprocessing
preferences_without_hard=delete_hard(preferences)

preferences_dozenten_without_hard= delete_hard(preferences_dozenten)
#default
print(preferences_without_hard.head())
print(preferences_dozenten_without_hard.head())

#week_timeslot_dislike
print(timeslot_week_disklike(preferences_without_hard))
print(timeslot_week_disklike(preferences_dozenten_without_hard))

#timeslot_week_popular
print(timeslot_week_popular(preferences_without_hard))
print(timeslot_week_popular(preferences_dozenten_without_hard))


# timeslot_overall_dislike
print(timeslot_overall_dislike(preferences_without_hard))
print(timeslot_overall_dislike(preferences_dozenten_without_hard))

#preferences_dozenten_without_hard
print(timeslot_overall_popular(preferences_without_hard))
print(timeslot_overall_popular(preferences_dozenten_without_hard))

# timeslot_workday_popular
print(timeslot_workday_popular(preferences_without_hard))
print(timeslot_workday_popular(preferences_dozenten_without_hard))


# timeslot_workday_dislike
print(':)')
print(timeslot_workday_dislike(preferences_without_hard))
print(timeslot_workday_dislike(preferences_dozenten_without_hard))