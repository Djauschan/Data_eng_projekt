import streamlit as st
import pandas as pd
from main import all_plots


unpopular_week_plot,unpopular_week_overall_plot,unpopular_weekday,eight_wake_up_plot,wanted_cluster,unwanted_cluster,heatmap_plot,liked_plot,liked_plot_overall=all_plots()



def main():
    # add Picture
    st.title("FH Wedel Stundenplan Auswertung")

    st.sidebar.image("Fh_wedel_logo.svg.png")
    user_menu = st.sidebar.radio(
    'Select an Option',['Unbeliebteste Zeitslots','Wie viel Dozenten mögen/mögen nicht um 08:00 aufstehen?', 'Clustering auf Basis der Dozenten-Wünsche','Was ist der durchschnittliche Dozentenwunsch'])

    if user_menu == 'Unbeliebteste Zeitslots':
        value = st.select_slider('Wählen Sie den Plot', options=['unbeliebtester Zeitslot','unbeliebtester Zeitslot pro Tag','unbeliebtester Wochentag'])
        if value == 'unbeliebtester Zeitslot':
            st.plotly_chart(unpopular_week_plot)
        elif value=='unbeliebtester Zeitslot pro Tag':
            st.plotly_chart(unpopular_week_overall_plot)
        else: 
            st.plotly_chart(unpopular_weekday)
    elif user_menu == 'Wie viel Dozenten mögen/mögen nicht um 08:00 aufstehen?':
        st.plotly_chart(eight_wake_up_plot)
    elif user_menu == 'Clustering auf Basis der Dozenten-Wünsche':
        value = st.select_slider('Wählen Sie den Plot', options=['Clustering Wanted','Clustering Unwanted'])
        if value == "Clustering Wanted":
            st.plotly_chart(wanted_cluster)
        else:
            st.plotly_chart(unwanted_cluster)
    else:
        value = st.select_slider('Wählen Sie den Plot', options=['Heatmap','beliebtester Zeitslot','beliebtester Zeitslot pro Tag'])
        if value=="Heatmap":
            st.pyplot(heatmap_plot)
        elif value=="beliebtester Zeitslot":
            st.plotly_chart(liked_plot)
        else: 
            st.plotly_chart(liked_plot_overall)
   






















if __name__ == "__main__":
    main()