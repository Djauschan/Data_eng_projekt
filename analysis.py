import numpy as np
import pandas as pd 
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.cluster import KMeans
from sklearn.compose import ColumnTransformer
import matplotlib.pyplot as plt 
from sklearn.decomposition import PCA
import seaborn as sns
import plotly.graph_objects as go


#die unbeliebteste Uhrzeit über die Woche
def timeslot_week_disklike(df:pd.DataFrame):
    df=df[df['constraint_value']=='NOT_WANTED']
    counts = df.groupby('timeslot_index')['timeslot_index'].count()
    if len(counts.index) !=7:
        a=set(range(7))
        b=set(counts.index)
        diff=a-b
        for index in diff:
            counts.loc[index] = 0

    timeslots=append_timeslots(df)
    counts=pd.concat([counts,timeslots],axis=1)
    counts.columns=['Amount of dislikes', 'start_time','end_time']

    counts=counts.sort_index()
   
    return counts

#Timeslots rauselesen, um es abzuhängen im finalen Data Frame
def append_timeslots (df):
    startzeit=pd.Series(df['start_time'].unique())
    endzeit=pd.Series(df['end_time'].unique())

    startzeit=startzeit.sort_values()
    endzeit=endzeit.sort_values()
    result=pd.concat([startzeit,endzeit],axis=1)
    return result




#die beliebteste Uhrzeit über die Woche
#Nutze die Funktion für Average Frage -> Timeslot generell über Week
def timeslot_week_popular(df:pd.DataFrame):
    time_df=df.copy()
    df= df[df['constraint_value']=='WANTED']
    counts = df.groupby('timeslot_index')['timeslot_index'].count()
    if len(counts.index) !=7:
        a=set(range(7))
        b=set(counts.index)
        diff=a-b
        for index in diff:
            counts.loc[index] = 0

    counts=counts.sort_index()
    timeslots=append_timeslots(time_df)
    counts=pd.concat([counts,timeslots],axis=1)
    counts.columns=['Amount of wishes', 'start_time','end_time']

    return counts

#die unbeliebteste Uhrzeit absolut
def timeslot_overall_dislike(df):
    time_df=df.copy()
    df=df[df['constraint_value']=='NOT_WANTED']
    weekdays=df['weekday'].unique()
    overall= pd.DataFrame()
    
    for weekday in weekdays:
        fill=pd.DataFrame()
        fill[weekday]=pd.Series(df[df['weekday']==weekday]['timeslot_index'])

        counts = fill.groupby(weekday)[weekday].count()
        overall=pd.concat([overall,counts],axis=1)
        

    if len(overall.index) !=7:
        a=set(range(7))
        b=set(overall.index)
        diff=a-b
        for index in diff:
            counts.loc[index] = 0

     
    overall=overall.sort_index() 
    timeslots=append_timeslots(time_df)
    overall=pd.concat([overall,timeslots],axis=1)

    # Letzte zwei Spalten ermitteln
    n_cols = len(overall.columns)
    last_two_cols = overall.columns[n_cols-2:]

    # Neue Spaltennamen festlegen
    new_names = ['start_time', 'end_time']

    # Spaltennamen ändern
    overall.rename(columns=dict(zip(last_two_cols, new_names)), inplace=True)

    # Define the custom order for weekdays
    custom_weekday_order = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY']

    # Sort the columns based on the custom order
    sorted_columns = custom_weekday_order + ['start_time', 'end_time']
    overall = overall.reindex(columns=sorted_columns)

   
    overall.fillna(0, inplace=True) 
    return overall


#die beliebteste Uhrzeit absolut
#Für die Average Frage -> Tag + Timeslot
def timeslot_overall_popular(df):
    time_df=df.copy()
    df=df[df['constraint_value']=='WANTED']
    weekdays=df['weekday'].unique()
    overall= pd.DataFrame()
    
    for weekday in weekdays:
        fill=pd.DataFrame()
        fill[weekday]=pd.Series(df[df['weekday']==weekday]['timeslot_index'])

        counts = fill.groupby(weekday)[weekday].count()
        overall=pd.concat([overall,counts],axis=1)
        

    if len(overall.index) !=7:
        a=set(range(7))
        b=set(overall.index)
        diff=a-b
        for index in diff:
            counts.loc[index] = 0


    overall=overall.sort_index() 
    timeslots=append_timeslots(time_df)
    overall=pd.concat([overall,timeslots],axis=1)

    # Letzte zwei Spalten ermitteln
    n_cols = len(overall.columns)
    last_two_cols = overall.columns[n_cols-2:]

    # Neue Spaltennamen festlegen
    new_names = ['start_time', 'end_time']

    # Spaltennamen ändern
    overall.rename(columns=dict(zip(last_two_cols, new_names)), inplace=True)

    # Define the custom order for weekdays
    custom_weekday_order = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY']

    # Sort the columns based on the custom order
    sorted_columns = custom_weekday_order + ['start_time', 'end_time']
    overall = overall.reindex(columns=sorted_columns)

    
    overall.fillna(0, inplace=True)  
    return overall

def timeslot_workday_popular(df:pd.DataFrame):
    time_df=df.copy()
    df=df[df['constraint_value']=='WANTED']
    new_df= df.groupby('weekday')['timeslot_index'].count()
    all_weekdays = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY']
    new_df = new_df.reindex(all_weekdays, fill_value=0)

    return new_df



def timeslot_workday_dislike(df:pd.DataFrame):
    time_df=df.copy()
    df=df[df['constraint_value']=='NOT_WANTED']
    new_df=pd.DataFrame()
    new_df['Anzahl der dislikes']= df.groupby('weekday')['timeslot_index'].count()
    all_weekdays = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY']
    new_df = new_df.reindex(all_weekdays, fill_value=0)
    return new_df
   

######################################################################################
#Wie viele Dozenten mögen/mögen nicht um 08:00 aufstehen

def timeslot_eight_opinion(df:pd.DataFrame):
    df_not_wanted=df[df['constraint_value']=='NOT_WANTED'].copy()
    dislike_counter=np.array([(df_not_wanted['timeslot_index']==0).sum()])
    

    df_wanted=df[df['constraint_value']=='WANTED'].copy()
    like_counter=np.array([(df_wanted['timeslot_index']==0).sum()])

    
    df_opinion=pd.DataFrame({'dislike': dislike_counter, 'like': like_counter})
    return df_opinion

##########################################################################################

def k_means_clus_combination_weekday_index_wanted(df:pd.DataFrame):
    """
    Clustering der Dozentenwünsche
    clustering auf Basis von Weekday in Kombination mit timeslot_index
    Nur wanteds werden berücksichtigt
    """  

    df=df[df['constraint_value']=='WANTED']
    # One-Hot Encoding für 'weekday'
    dfc = pd.get_dummies(df, columns=['weekday']).copy()
    
    # Auswahl der Features für das Clustering
    X = dfc.drop(['constraint_value', 'start_time', 'end_time'], axis=1)
    
    # Ausführen von k-Means Clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    dfc['Cluster'] = kmeans.fit_predict(X)
    dfc['weekday']=df['weekday']
    
    # Visualisierung der Cluster
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='timeslot_index', y='weekday', hue='Cluster', data=dfc, palette='viridis', s=100)
    plt.title('Cluster Visualization based on Weekday and timeslot_index')
    plt.show()




def cluster_timeslots_based_on_index_wanted(df, n_clusters=3):
    """
    Führt k-Means Clustering basierend auf den 'timeslot_index' Werten durch.
    Nur Wanteds werden berücksichtigt
    
    Args:
    df (pd.DataFrame): DataFrame, der die Spalte 'timeslot_index' enthält.
    n_clusters (int): Die Anzahl der zu bildenden Cluster.
    
    Returns:
    None: Diese Funktion visualisiert das Ergebnis des Clusterings.
    """
    df=df[df['constraint_value']=='WANTED']
    
    # Auswahl der 'timeslot_index' Spalte für das Clustering
    X = df[['timeslot_index']].values
    
    # k-Means Clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['TimeslotCluster'] = kmeans.fit_predict(X)
    
    
    # Visualisierung der Cluster mit Plotly Go
    fig = go.Figure()

    # Scatterplot für die Punkte
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['timeslot_index'],
        mode='markers',
        marker=dict(
            size=20,
            color=df['TimeslotCluster'],
            colorscale='Viridis',
            opacity=0.9
        ),
        text=df['TimeslotCluster']
    ))

    # Layout-Einstellungen
    fig.update_layout(
        title='Clustering der Timeslots basierend auf timeslot_index',
        xaxis=dict(title='Index'),
        yaxis=dict(title='Timeslot Index'),
        coloraxis_colorbar=dict(title='Cluster')
    )

    return fig
 

def cluster_timeslots_based_on_index_unwanted(df, n_clusters=3):
    """
    Führt k-Means Clustering basierend auf den 'timeslot_index' Werten durch.
    
    Args:
    df (pd.DataFrame): DataFrame, der die Spalte 'timeslot_index' enthält.
    n_clusters (int): Die Anzahl der zu bildenden Cluster.
    
    Returns:
    None: Diese Funktion visualisiert das Ergebnis des Clusterings.
    """
    df=df[df['constraint_value']=='NOT_WANTED']
    
    # Auswahl der 'timeslot_index' Spalte für das Clustering
    X = df[['timeslot_index']].values
    
    # k-Means Clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['TimeslotCluster'] = kmeans.fit_predict(X)

    
    # Visualisierung der Cluster mit Plotly Go
    fig = go.Figure()

    # Scatterplot für die Punkte
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['timeslot_index'],
        mode='markers',
        marker=dict(
            size=20,
            color=df['TimeslotCluster'],
            colorscale='Viridis',
            opacity=0.9
        ),
        text=df['TimeslotCluster']
    ))

    # Layout-Einstellungen
    fig.update_layout(
        title='Clustering der Timeslots basierend auf timeslot_index',
        xaxis=dict(title='Index'),
        yaxis=dict(title='Timeslot Index'),
        coloraxis_colorbar=dict(title='Cluster')
    )

    return fig


def timeslot_index_weekday_unwanted_cluster(df:pd.DataFrame, n_clusters=3):
    """
    Clustering der Dozentenwünsche
    clustering auf Basis von Weekday in Kombination mit timeslot_index
    Nur un_wanted werden berücksichtigt
    """  

    df=df[df['constraint_value']=='NOT_WANTED']
    # One-Hot Encoding für 'weekday'
    df = pd.get_dummies(df, columns=['weekday'])
    
    # Auswahl der Features für das Clustering
    X = df.drop(['constraint_value', 'start_time', 'end_time'], axis=1)
    
    # Ausführen von k-Means Clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X)
    
    # Ausgabe der ersten paar Zeilen des DataFrames mit Cluster-Zuweisung
    print(df.head())








###############################################################################################################
# Average wish

def average_preference_timeslot(df:pd.DataFrame):
    """

    """
    df['preferences'] = df['constraint_value'].map({'WANTED': 1, 'NOT_WANTED': 0})

    weekdays_order = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY']
    df['weekday'] = pd.Categorical(df['weekday'], categories=weekdays_order, ordered=True)

    average_preferences=df.groupby(['weekday','timeslot_index'])['preferences'].mean().reset_index()
    
     # Pivot für die Heatmap
    preference_pivot = average_preferences.pivot(index='weekday', columns='timeslot_index', values='preferences')

    # Visualisierung der durchschnittlichen Präferenzen mit einer Heatmap
    plt.figure(figsize=(12, 6))
    sns.heatmap(preference_pivot, annot=True, cmap="YlGnBu", cbar_kws={'label': 'Durchschnittliche Präferenz'})
    plt.title('Durchschnittliche Dozentenpräferenz pro Timeslot und Wochentag')
    plt.xlabel('Timeslot Index')
    plt.ylabel('Wochentag')
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    return plt