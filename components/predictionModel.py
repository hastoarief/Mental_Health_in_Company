import dash_core_components as dcc
import dash_html_components as html

def predictionModel() :
    return html.Div([
                html.H1('Test Predict Mental Health', className='h1'),
                html.Div(children=[
                    html.Div([
                        html.P('Age : ')
                    ],className='col-12'),
                    html.Div([
                        dcc.Input(id='inputAge', type='number')
                    ],className='col-12'),
                    html.Div([
                        html.P('Gender : ')
                    ],className='col-12'),
                    html.Div([
                        dcc.Dropdown(id='inputGender', 
                        options=[
                            {'label': 'Male', 'value': 'male'},
                            {'label': 'Female', 'value': 'female'},
                            {'label': 'Others', 'value': 'others'}
                        ])
                    ],className='col-12'),
                    html.Div([
                        html.P('Are you self employed? ')
                    ],className='col-12'),
                    html.Div([
                        dcc.Dropdown(id='inputSelfEmployed', 
                        options=[
                            {'label': 'Yes', 'value': 'Yes'},
                            {'label': 'No', 'value': 'No'}
                        ])
                    ],className='col-12'),
                    html.Div([
                        html.P('Do you have relatives who have mental health? ')
                    ],className='col-12'),
                    html.Div([
                        dcc.Dropdown(id='inputFamily', 
                        options=[
                            {'label': 'Yes', 'value': 'Yes'},
                            {'label': 'No', 'value': 'No'},
                        ])
                    ],className='col-12'),
                    html.Div([
                        html.P('Do you think your work interferes your mental health?')
                    ],className='col-12'),
                    html.Div([
                        dcc.Dropdown(id='inputWorkInterfers', 
                        options=[
                            {'label': 'Often', 'value': 'Often'},
                            {'label': 'Sometimes', 'value': 'Sometimes'},
                            {'label': 'Rarely', 'value': 'Rarely'},
                            {'label': 'Never', 'value': 'Never'},
                            {'label': "Don't Know", 'value': "Don't Know"}
                        ])
                    ],className='col-12'),
                    html.Div([
                        html.P('Number of employees in your company? ')
                    ],className='col-12'),
                    html.Div([
                        dcc.Dropdown(id='inputNoEmploy', 
                        options=[
                            {'label': '1-5', 'value': '1-5'},
                            {'label': '6-25', 'value': '6-25'},
                            {'label': '26-100', 'value': '26-100'},
                            {'label': '100-500', 'value': '100-500'},
                            {'label': "500-1000", 'value': '500-1000'},
                            {'label': "More than 1000", 'value': 'More than 1000'}
                        ])
                    ],className='col-12'),
                    html.Div([
                        html.P('Do you work remotely (outside of an office) at least 50percent of the time? ')
                    ],className='col-12'),
                    html.Div([
                        dcc.Dropdown(id='inputRemote', 
                        options=[
                            {'label': 'Yes', 'value': 'Yes'},
                            {'label': 'No', 'value': 'No'}
                        ])
                    ],className='col-12'),
                    html.Div([
                        html.P('Is your employer primarily a tech company/organization?')
                    ],className='col-12'),
                    html.Div([
                        dcc.Dropdown(id='inputTechComp', 
                        options=[
                            {'label': 'Yes', 'value': 'Yes'},
                            {'label': 'No', 'value': 'No'}
                        ])
                    ],className='col-12'),
                    html.Div([
                        html.P('Does your company provide mental health benefits? ')
                    ],className='col-12'),
                    html.Div([
                        dcc.Dropdown(id='inputBenefit', 
                        options=[
                            {'label': 'Yes', 'value': 'Yes'},
                            {'label': 'No', 'value': 'No'},
                            {'label': 'Dont Know', 'value': "Don't know"},
                        ])
                    ],className='col-12'),
                    html.Div([
                        html.P('Do you know the options for mental health care your company provides? (if any)')
                    ],className='col-12'),
                    html.Div([
                        dcc.Dropdown(id='inputCareOpt', 
                        options=[
                            {'label': 'Yes', 'value': 'Yes'},
                            {'label': 'No', 'value': 'No'},
                            {'label': 'Not Sure', 'value': 'Not sure'},
                        ])
                    ],className='col-12'),
                    html.Div([
                        html.P('Has your employer ever discussed mental health as part of an employee wellness program?')
                    ],className='col-12'),
                    html.Div([
                        dcc.Dropdown(id='inputWellness', 
                        options=[
                            {'label': 'Yes', 'value': 'Yes'},
                            {'label': 'No', 'value': 'No'},
                            {'label': 'Dont Know', 'value': "Don't know"},
                        ])
                    ],className='col-12'),
                    html.Div([
                        html.P('Does your employer provide resources to learn more about mental health issues and how to seek help?')
                    ],className='col-12'),
                    html.Div([
                        dcc.Dropdown(id='inputSeekHelp', 
                        options=[
                            {'label': 'Yes', 'value': 'Yes'},
                            {'label': 'No', 'value': 'No'},
                            {'label': 'Dont Know', 'value': "Don't know"},
                        ])
                    ],className='col-12'),
                    html.Div([
                        html.P('Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources?')
                    ],className='col-12'),
                    html.Div([
                        dcc.Dropdown(id='inputAnonymity', 
                        options=[
                            {'label': 'Yes', 'value': 'Yes'},
                            {'label': 'No', 'value': 'No'},
                            {'label': 'Dont Know', 'value': "Don't know"},
                        ])
                    ],className='col-12'),
                    html.Div([
                        html.P('How easy is it for you to take medical leave for a mental health condition?')
                    ],className='col-12'),
                    html.Div([
                        dcc.Dropdown(id='inputLeave', 
                        options=[
                            {'label': 'Somewhat easy', 'value': 'Somewhat easy'},
                            {'label': "Don't know", 'value': "Don't know"},
                            {'label': 'Somewhat difficult', 'value': "Somewhat difficult"},
                            {'label': 'Very difficult', 'value': 'Very difficult'},
                            {'label': "Very easy", 'value': "Very easy"}
                        ])
                    ],className='col-12'),
                    html.Div([
                        html.P('Do you think that discussing a mental health issue with your employer would have negative consequences?')
                    ],className='col-12'),
                    html.Div([
                        dcc.Dropdown(id='inputMHConsq', 
                        options=[
                            {'label': 'Yes', 'value': 'Yes'},
                            {'label': 'No', 'value': 'No'},
                            {'label': 'Maybe', 'value': 'Maybe'},
                        ])
                    ],className='col-12'),
                    html.Div([
                        html.P('Do you think that discussing a physical health issue with your employer would have negative consequences?')
                    ],className='col-12'),
                    html.Div([
                        dcc.Dropdown(id='inputPHConsq', 
                        options=[
                            {'label': 'Yes', 'value': 'Yes'},
                            {'label': 'No', 'value': 'No'},
                            {'label': 'Maybe', 'value': 'Maybe'},
                        ])
                    ],className='col-12'),
                    html.Div([
                        html.P('Would you be willing to discuss a mental health issue with your coworkers?')
                    ],className='col-12'),
                    html.Div([
                        dcc.Dropdown(id='inputCoworker', 
                        options=[
                            {'label': 'Yes', 'value': 'Yes'},
                            {'label': 'No', 'value': 'No'},
                            {'label': 'Some of Them', 'value': 'Some of them'},
                        ])
                    ],className='col-12'),
                    html.Div([
                        html.P('Would you be willing to discuss a mental health issue with your direct supervisor(s)?')
                    ],className='col-12'),
                    html.Div([
                        dcc.Dropdown(id='inputSpv', 
                        options=[
                            {'label': 'Yes', 'value': 'Yes'},
                            {'label': 'No', 'value': 'No'},
                            {'label': 'Some of Them', 'value': 'Some of them'},
                        ])
                    ],className='col-12'),
                    html.Div([
                        html.P('Would you bring up a mental health issue with a potential employer in an interview?')
                    ],className='col-12'),
                    html.Div([
                        dcc.Dropdown(id='inputIntMH', 
                        options=[
                            {'label': 'Yes', 'value': 'Yes'},
                            {'label': 'No', 'value': 'No'},
                            {'label': 'Maybe', 'value': 'Maybe'},
                        ])
                    ],className='col-12'),
                    html.Div([
                        html.P('Would you bring up a physical health issue with a potential employer in an interview?')
                    ],className='col-12'),
                    html.Div([
                        dcc.Dropdown(id='inputIntPH', 
                        options=[
                            {'label': 'Yes', 'value': 'Yes'},
                            {'label': 'No', 'value': 'No'},
                            {'label': 'Maybe', 'value': 'Maybe'},
                        ])
                    ],className='col-12'),
                    html.Div([
                        html.P('Do you feel that your employer takes mental health as seriously as physical health?')
                    ],className='col-12'),
                    html.Div([
                        dcc.Dropdown(id='inputMvP', 
                        options=[
                            {'label': 'Yes', 'value': 'Yes'},
                            {'label': 'No', 'value': 'No'},
                            {'label': 'Dont Know', 'value': "Don't know"},
                        ])
                    ],className='col-12'),
                    html.Div([
                        html.P('Have you heard of or observed negative consequences for coworkers with mental health conditions in your workplace?')
                    ],className='col-12'),
                    html.Div([
                        dcc.Dropdown(id='inputObs', 
                        options=[
                            {'label': 'Yes', 'value': 'Yes'},
                            {'label': 'No', 'value': 'No'}
                        ])
                    ],className='col-12'),
                    html.Div([
                        html.P('On which continent do you currently working at?')
                    ],className='col-12'),
                    html.Div([
                        dcc.Dropdown(id='inputContinent', 
                        options=[
                            {'label': 'America', 'value': 'America'},
                            {'label': 'Europe', 'value': 'Europe'},
                            {'label': 'Others', 'value': 'Others'}
                        ])
                    ],className='col-12'),
                    html.Div([
                        html.Button('Predict', id='buttonPredict', className='btn btn-primary')
                    ],className='mx-auto', style={ 'paddingTop': '20px', 'paddingBottom': '20px' })
                ],className='row'),
                html.Div([
                    html.H2('', id='outputPredict', className='mx-auto')
                ], className='row')
            ])