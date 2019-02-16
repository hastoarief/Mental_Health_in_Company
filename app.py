import os
import plotly.graph_objs as go
import plotly.plotly as py
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output, State
import pickle
from components.predictionModel import predictionModel
from components.Table import renderTable

loadModel = pickle.load(open('rfc_mentahHealth.sav', 'rb'))
df = pd.read_csv('dataCSV.csv')

app = dash.Dash(__name__)

server = app.server

app.title = 'Dashboard Mental Health'

app.layout = html.Div(children=[
    html.H1(children='Dashboard Mental Health',className='titleDashboard'),
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Mental Health Dataset', value='tab-1',children=[
            renderTable(df)
        ]),
        dcc.Tab(label='Pie Chart', value='tab-2',children=[
            html.Div([
                html.H1('Pie Chart Mental Health', className='h1'),
                html.Div(children=[
                    html.Div([
                        html.P('Category :'),
                        dcc.Dropdown(
                            id='catFilterPie',
                            options=[{'label': i.capitalize(), 'value': i} for i in ['Work Interfere','Family History', 'Benefits']],
                            value='Work Interfere'
                        )
                    ],className='col-4'),
                ],className='row'),
                html.Div([
                html.Div([
                    html.H3('Treatment = Yes'),
                    dcc.Graph(
                    id='pieChart'
                    )
                ], className='col-6'),
                html.Div([
                    html.H3('Treatment = No'),
                    dcc.Graph(
                    id='pieChart2'
                    )
                ], className='col-6'),
            ], className="row")
            ])
        ]),
        dcc.Tab(label='Test Predict', value='tab-3',children=[
            predictionModel()
        ]),
    ], style={
        'fontFamily': 'system-ui'
    }, content_style={
        'fontFamily': 'Arial',
        'borderBottom': '1px solid #d6d6d6',
        'borderLeft': '1px solid #d6d6d6',
        'borderRight': '1px solid #d6d6d6',
        'padding': '44px'
    })
], style={
    'maxWidth': '1200px',
    'margin': '0 auto'
})

@app.callback(
    Output(component_id='pieChart', component_property='figure'),
    [Input(component_id='catFilterPie', component_property='value')]
)
def update_graph_pie(cat):
    kol = {
        'Work Interfere': 'work_interfere',
        'Family History': 'family_history',
        'Benefits': 'benefits'
    }
    listLabel = list(df[kol[cat]].unique())
    listLabel.sort()
    return {
        'data': [
            go.Pie(
                labels=listLabel,
                values=[len(df[(df[kol[cat]] == item) & (df['treatment']==1)][kol[cat]]) for item in listLabel],
                textinfo='value',
                hoverinfo='label+percent',
                marker=dict(
                    # colors=color_set[hue], 
                    line=dict(color='black', width=2)
                ),
                sort=False
            ),
        ],
        'layout': go.Layout(
            showlegend=False,
        ),
    }

@app.callback(
    Output(component_id='pieChart2', component_property='figure'),
    [Input(component_id='catFilterPie', component_property='value')]
)
def update_graph_pie2(cat):
    kol = {
        'Work Interfere': 'work_interfere',
        'Family History': 'family_history',
        'Benefits': 'benefits'
    }
    listLabel = list(df[kol[cat]].unique())
    listLabel.sort()
    return {
        'data': [
            go.Pie(
                labels=listLabel,
                values=[len(df[(df[kol[cat]] == item) & (df['treatment']==0)][kol[cat]]) for item in listLabel],
                textinfo='value',
                hoverinfo='label+percent',
                marker=dict(
                    # colors=color_set[hue], 
                    line=dict(color='black', width=2)
                ),
                sort=False
            ),
        ],
        # 'layout': go.Layout(
        #     margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
        #     legend={'x': 0, 'y': 1}
        # ),
    }


@app.callback(
    Output('table-multicol-sorting', "data"),
    [Input('table-multicol-sorting', "pagination_settings"),
     Input('table-multicol-sorting', "sorting_settings")])
def update_graph(pagination_settings, sorting_settings):
    # print(sorting_settings)
    if len(sorting_settings):
        dff = df.head(500).sort_values(
            [col['column_id'] for col in sorting_settings],
            ascending=[
                col['direction'] == 'asc'
                for col in sorting_settings
            ],
            inplace=False
        )
    else:
        # No sort is applied
        dff = df.head(500)

    return dff.iloc[
        pagination_settings['current_page']*pagination_settings['page_size']:
        (pagination_settings['current_page'] + 1)*pagination_settings['page_size']
    ].to_dict('rows')



@app.callback(
    Output('outputPredict', 'children'),
    [Input('buttonPredict', 'n_clicks')],
    [State('inputAge', 'value'), 
    State('inputGender', 'value'),
    State('inputSelfEmployed', 'value'),
    State('inputFamily', 'value'),
    State('inputWorkInterfers', 'value'),
    State('inputNoEmploy', 'value'),
    State('inputRemote', 'value'),
    State('inputTechComp', 'value'),
    State('inputBenefit', 'value'),
    State('inputCareOpt', 'value'),
    State('inputWellness', 'value'),
    State('inputSeekHelp', 'value'),
    State('inputAnonymity', 'value'),
    State('inputLeave', 'value'),
    State('inputMHConsq', 'value'),
    State('inputPHConsq', 'value'),
    State('inputCoworker', 'value'),
    State('inputSpv', 'value'),
    State('inputIntMH', 'value'),
    State('inputIntPH', 'value'),
    State('inputMvP', 'value'),
    State('inputObs', 'value'),
    State('inputContinent', 'value')
    ])
def update_output(n_clicks, Age, Gender, self_employed, family_history, work_interfere, no_employees, remote, tech_comp, benefits, care_options, 
                    wellness_program, seek_help, anonymity, leave, mental_health_consequence, phys_health_consequence,coworkers, supervisor, mental_health_interview, 
                    phys_health_interview, mental_vs_physical, obs_consequence, Continent):
    data = np.array([[Age, Gender, self_employed, family_history, work_interfere, no_employees, remote, tech_comp, benefits, care_options, 
                    wellness_program, seek_help, anonymity, leave, mental_health_consequence, phys_health_consequence,coworkers, supervisor, mental_health_interview, 
                    phys_health_interview, mental_vs_physical, obs_consequence, Continent]])
    prediction = loadModel.predict(data)
    predictProba = loadModel.predict_proba(data)
    hasil = ''
    if(prediction[0] == 1) :
        hasil = 'You need a Mental Health Treatment'
        return 'Prediction : ' + hasil + ' with Probability : ' + str(round(predictProba[0,1]))
    else :
        hasil = "You don't need a Mental Health Treatment"
        return 'Prediction : ' + hasil


if __name__ == '__main__':
    app.run_server(debug=True,port=1997)