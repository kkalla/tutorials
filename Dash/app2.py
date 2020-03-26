# Basic callbacks
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv') # noqa
df2 = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')
all_options = {
    'America': ['New York City', 'San Francisco', 'Cincinnati'],
    'Canada': [u'Montréal', 'Toronto', 'Ottawa']
}

available_indicators = df2['Indicator Name'].unique()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='my-id', value='initial value', type='text'),
    html.Div(id='my-div'),
    dcc.Markdown('---'),

    html.H2("Graph example"),
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    ),
    dcc.Markdown('---'),

    # Multiple inputs
    html.H2("Multiple inputs"),
    html.Div([
        dcc.Dropdown(
            id='xaxis-column',
            options=[{'label': i, 'value': i} for i in available_indicators],
            value='Fertility rate, total (births per woman)'
        ),
        dcc.RadioItems(
            id='xaxis-type',
            options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
            value='Linear',
            labelStyle={'display': 'inline-block'}
        )
    ], style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        dcc.Dropdown(
            id='yaxis-column',
            options=[{'label': i, 'value': i} for i in available_indicators],
            value='Life expectancy at birth, total (years)'
        ),
        dcc.RadioItems(
            id='yaxis-type',
            options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
            value='Linear',
            labelStyle={'display': 'inline-block'}
        )
    ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),

    dcc.Graph(id='indicator-graphic'),
    dcc.Slider(
        id='year--slider',
        min=df2['Year'].min(),
        max=df2['Year'].max(),
        value=df2['Year'].max(),
        marks={str(year): str(year) for year in df2['Year'].unique()},
        step=None
    ),
    dcc.Markdown('---'),

    # Multiple Outputs
    html.H2('Multiple Outputs'),
    dcc.Input(
        id='num-multi',
        type='number',
        value=5
    ),
    html.Table([
        html.Tr([html.Td(['x', html.Sup(2)]), html.Td(id='square')]),
        html.Tr([html.Td(['x', html.Sup(3)]), html.Td(id='cube')]),
        html.Tr([html.Td(['2', html.Sup('x')]), html.Td(id='twos')]),
        html.Tr([html.Td(['3', html.Sup('x')]), html.Td(id='threes')]),
        html.Tr([html.Td(['4', html.Sup('x')]), html.Td(id='fours')]),
        html.Tr([html.Td(['x', html.Sup('x')]), html.Td(id='x^x')])
    ]),
    dcc.Markdown('---'),

    # chained callbacks
    html.H2('Chained Callbacks'),
    dcc.RadioItems(
        id='countries-radio',
        options=[{'label': k, 'value': k} for k in all_options.keys()],
        value='America'
    ),
    html.Hr(),
    dcc.RadioItems(id='cities-radio'),
    html.Hr(),
    html.Div(id='display-selected-values')
])


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)


@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')]
)
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]
    traces = []
    for i in filtered_df.continent.unique():
        df_by_continent = filtered_df[filtered_df['continent'] == i]
        traces.append(dict(
            x=df_by_continent['gdpPercap'],
            y=df_by_continent['lifeExp'],
            text=df_by_continent['country'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
        ))

    return {
        'data': traces,
        'layout': dict(
            xaxis={'type': 'log', 'title': 'GDP Per Capita',
                   'range': [2.3, 4.8]},
            yaxis={'title': 'Life Expectancy', 'range': [20, 90]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest',
            transition={'duration': 500}
        )
    }


@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-column', 'value'),
     Input('xaxis-type', 'value'),
     Input('yaxis-type', 'value'),
     Input('year--slider', 'value')]
)
def update_graph(xaxis_col, yaxis_col, xaxis_type, yaxis_type, year_value):
    dff = df2[df2['Year'] == year_value]

    return {
        'data': [dict(
            x=dff[dff['Indicator Name'] == xaxis_col]['Value'],
            y=dff[dff['Indicator Name'] == yaxis_col]['Value'],
            text=dff[dff['Indicator Name'] == yaxis_col]['Country Name'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'blue'}
            }
        )],
        'layout': dict(
            xaxis={
                'title': xaxis_col,
                'type': 'linear' if xaxis_type == 'Linear' else 'log'
            },
            yaxis={
                'title': yaxis_col,
                'type': 'linear' if yaxis_type == 'Linear' else 'log'
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }


@app.callback(
    [Output('square', 'children'),
     Output('cube', 'children'),
     Output('twos', 'children'),
     Output('threes', 'children'),
     Output('fours', 'children'),
     Output('x^x', 'children')],
    [Input('num-multi', 'value')]
)
def update_table(n):
    return n**2, n**3, 2**n, 3**n, 4**n, n**n


@app.callback(
    Output('cities-radio', 'options'),
    [Input('countries-radio', 'value')]
)
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]


@app.callback(
    Output('cities-radio', 'value'),
    [Input('cities-radio', 'options')]
)
def set_cities_value(available_options):
    return available_options[0]['value']


@app.callback(
    Output('display-selected-values', 'children'),
    [Input('countries-radio', 'value'),
     Input('cities-radio', 'value')]
)
def set_display_children(selected_country, selected_city):
    return u'{} is a city in {}'.format(
        selected_city, selected_country
    )


if __name__ == '__main__':
    app.run_server(debug=True)