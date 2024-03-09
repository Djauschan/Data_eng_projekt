import plotly.express as px
import plotly.graph_objects as go
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt



def week_plot(df:pd.DataFrame): 
    df['start_time']=df['start_time'].apply(str)
    df['end_time']=df['end_time'].apply(str)
    df['start_time']=pd.to_datetime(df['start_time'])
    df['end_time']=pd.to_datetime(df['end_time'])

    # Adjusting the new column creation for x-axis labels to handle datetime objects
    df['Time Range'] = df['start_time'].dt.strftime('%H:%M') + '-' + df['end_time'].dt.strftime('%H:%M')
    
    colors = px.colors.qualitative.Vivid[:len(df)] 
    
    # Creating the bar plot using Plotly Graph Objects with datetime adjustments
    fig = go.Figure(data=[go.Bar(x=df['Time Range'],y=df['Amount of dislikes'],marker_color=colors  # Apply unique colors to each bar
    )])
    fig.update_layout(title_text='Amount of dislikes', xaxis_title='Time Range', yaxis_title='Amount of dislikes')
    return fig


def overall_plot(df:pd.DataFrame):

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    values=df.drop(['start_time','end_time'],axis=1).copy()

    df['start_time']=df['start_time'].apply(str)
    df['end_time']=df['end_time'].apply(str)
    df['start_time']=pd.to_datetime(df['start_time'])
    df['end_time']=pd.to_datetime(df['end_time'])

    # Adjusting the new column creation for x-axis labels to handle datetime objects
    df['Time Range'] = df['start_time'].dt.strftime('%H:%M') + '-' + df['end_time'].dt.strftime('%H:%M')
    

    plot=go.Figure(data=[go.Bar(
        name=df.iloc[0]['Time Range'],
        x=weekdays,
        y=values.iloc[0].values.flatten().tolist()
        ),
        go.Bar(
        name=df.iloc[1]['Time Range'],
        x=weekdays,
        y=values.iloc[1].values.flatten().tolist()
        ),
        go.Bar(
        name=df.iloc[2]['Time Range'],
        x=weekdays,
        y=values.iloc[2].values.flatten().tolist()
        ),
        go.Bar(
        name=df.iloc[3]['Time Range'],
        x=weekdays,
        y=values.iloc[3].values.flatten().tolist()
        ),
        go.Bar(
        name=df.iloc[4]['Time Range'],
        x=weekdays,
        y=values.iloc[4].values.flatten().tolist()
        ),
        go.Bar(
        name=df.iloc[5]['Time Range'],
        x=weekdays,
        y=values.iloc[5].values.flatten().tolist()
        ),
        go.Bar(
        name=df.iloc[6]['Time Range'],
        x=weekdays,
        y=values.iloc[6].values.flatten().tolist()
        )
    ])
    plot.update_layout(
    title="Unpopular Timeslots of each Weekday",
    xaxis_title="Weekday",
    yaxis_title="Number of dislikes" 
    )
    return plot


def aufstehen_viz(df:pd.DataFrame):
    # Erstellen von Figure und Spur
    fig = go.Figure()
    fig.add_trace(go.Pie(labels=df.columns, values=df.iloc[0], hole=.3))

    # Anpassen des Layouts
    fig.update_layout(title="Wie viele Dozenten mögen/mögen nicht um 8:00 aufstehen?", 
                    legend_title="Auswertung", 
                    font=dict(size=14))

    # Anzeigen des Diagramms
    return fig    


def weekday_plot(df:pd.DataFrame):
    colors = px.colors.qualitative.Vivid[:len(df)] 
    
    # Creating the bar plot using Plotly Graph Objects with datetime adjustments
    fig = go.Figure(data=[go.Bar(x=df.index,y=df['Anzahl der dislikes'],marker_color=colors  # Apply unique colors to each bar
    )])
    fig.update_layout(title_text='Amount of dislikes', xaxis_title='Weekday', yaxis_title='Amount of dislikes')
    return fig


def week_plot_like(df:pd.DataFrame): 
    df['start_time']=df['start_time'].apply(str)
    df['end_time']=df['end_time'].apply(str)
    df['start_time']=pd.to_datetime(df['start_time'])
    df['end_time']=pd.to_datetime(df['end_time'])

    # Adjusting the new column creation for x-axis labels to handle datetime objects
    df['Time Range'] = df['start_time'].dt.strftime('%H:%M') + '-' + df['end_time'].dt.strftime('%H:%M')
    df.sort_values(by=['start_time'],inplace=True)
    colors = px.colors.qualitative.Vivid[:len(df)] 
    
    # Creating the bar plot using Plotly Graph Objects with datetime adjustments
    fig = go.Figure(data=[go.Bar(x=df['Time Range'],y=df['Amount of wishes'],marker_color=colors  # Apply unique colors to each bar
    )])
    fig.update_layout(title_text='Wanted Timeslots', xaxis_title='Time Range', yaxis_title='Amount of wishes')
    return fig

def overall_plot_liked(df:pd.DataFrame):

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    values=df.drop(['start_time','end_time'],axis=1).copy()

    df['start_time']=df['start_time'].apply(str)
    df['end_time']=df['end_time'].apply(str)
    df['start_time']=pd.to_datetime(df['start_time'])
    df['end_time']=pd.to_datetime(df['end_time'])

    # Adjusting the new column creation for x-axis labels to handle datetime objects
    df['Time Range'] = df['start_time'].dt.strftime('%H:%M') + '-' + df['end_time'].dt.strftime('%H:%M')
    

    plot=go.Figure(data=[go.Bar(
        name=df.iloc[0]['Time Range'],
        x=weekdays,
        y=values.iloc[0].values.flatten().tolist()
        ),
        go.Bar(
        name=df.iloc[1]['Time Range'],
        x=weekdays,
        y=values.iloc[1].values.flatten().tolist()
        ),
        go.Bar(
        name=df.iloc[2]['Time Range'],
        x=weekdays,
        y=values.iloc[2].values.flatten().tolist()
        ),
        go.Bar(
        name=df.iloc[3]['Time Range'],
        x=weekdays,
        y=values.iloc[3].values.flatten().tolist()
        ),
        go.Bar(
        name=df.iloc[4]['Time Range'],
        x=weekdays,
        y=values.iloc[4].values.flatten().tolist()
        ),
        go.Bar(
        name=df.iloc[5]['Time Range'],
        x=weekdays,
        y=values.iloc[5].values.flatten().tolist()
        ),
        go.Bar(
        name=df.iloc[6]['Time Range'],
        x=weekdays,
        y=values.iloc[6].values.flatten().tolist()
        )
    ])
    plot.update_layout(
    title="Most Wanted Timeslots of each Weekday",
    xaxis_title="Weekday",
    yaxis_title="Amount of wishes" 
    )
    return plot