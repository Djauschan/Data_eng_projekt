import numpy as np 
import pandas as pd 
import os
from dotenv import load_dotenv
from database import Database
from datacleaning import delete_hard
from analysis import timeslot_week_disklike,timeslot_week_popular,timeslot_overall_dislike,timeslot_overall_popular,timeslot_workday_popular,timeslot_workday_dislike,timeslot_eight_opinion, k_means_clus_combination_weekday_index_wanted,cluster_timeslots_based_on_index_wanted,average_preference_timeslot,cluster_timeslots_based_on_index_unwanted,timeslot_index_weekday_unwanted_cluster
from visualization import week_plot, overall_plot,aufstehen_viz,weekday_plot,week_plot_like,overall_plot_liked



load_dotenv()


db_config = {
    'database': os.getenv("DB_DATABASE"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'host': os.getenv("DB_HOST"),
    'port': os.getenv("DB_PORT") 
    }



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



x=timeslot_week_disklike(preferences_without_hard)
y=timeslot_overall_dislike(preferences_without_hard)
z=timeslot_workday_dislike(preferences_without_hard)

#Für Frage 4
xx=timeslot_week_popular(preferences_dozenten_without_hard)
yy=timeslot_overall_popular(preferences_dozenten_without_hard)

# b=timeslot_overall_popular(preferences_without_hard)
# print(b)


# c=timeslot_workday_popular(preferences_without_hard)

# d=timeslot_workday_dislike(preferences_without_hard)




#Viz Was sind die unbeliebtesten Zeitslots im Stundenplan
unpopular_week_plot=week_plot(x) #Timslots allgemein
unpopular_week_overall_plot=overall_plot(y) #overall viz
unpopular_weekday=weekday_plot(z)



#Viz Wie viele Dozenten mögen/mögen nicht um 08:00 aufstehen? 
früh_aufstehen_df=timeslot_eight_opinion(preferences_dozenten_without_hard)
eight_wake_up_plot=aufstehen_viz(früh_aufstehen_df)

#Clustering auf Basis der Dozenten Wünsche
wanted_cluster=cluster_timeslots_based_on_index_wanted(preferences_dozenten_without_hard)
unwanted_cluster=cluster_timeslots_based_on_index_unwanted(preferences_dozenten_without_hard)


#Heatmap für durchschnittlichen Wunsch
heatmap_plot=average_preference_timeslot(preferences_dozenten_without_hard)
print(xx)
liked_plot=week_plot_like(xx)
liked_plot_overall=overall_plot_liked(yy)
#alle Plots returnen
