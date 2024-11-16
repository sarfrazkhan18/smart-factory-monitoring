import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random
import os

# Initialize the Dash app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # Needed for production deployment

# Simulate sensor data
def generate_sensor_data():
    current_time = datetime.now()
    times = [(current_time - timedelta(minutes=i)).strftime('%H:%M:%S') for i in range(30)]
    times.reverse()
    
    # Generate random data with some patterns
    temperature = [random.uniform(70, 75) + np.sin(i/5) * 2 for i in range(30)]
    vibration = [random.uniform(0.2, 0.3) + np.cos(i/5) * 0.1 for i in range(30)]
    pressure = [random.uniform(95, 105) + np.sin(i/7) * 3 for i in range(30)]
    
    return times, temperature, vibration, pressure

# Create the layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Smart Factory Monitoring System", className="text-center my-4"), width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Machine Status"),
                dbc.CardBody([
                    html.H3("Operating Normally", className="text-success"),
                    html.P("Last checked: Just now", id="last-checked")
                ])
            ], className="mb-4")
        ], width=12, lg=4),
        
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Current Metrics"),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H4("Temperature"),
                            html.H2("72.5°F", id="current-temp")
                        ]),
                        dbc.Col([
                            html.H4("Vibration"),
                            html.H2("0.25g", id="current-vib")
                        ]),
                        dbc.Col([
                            html.H4("Pressure"),
                            html.H2("100 PSI", id="current-press")
                        ])
                    ])
                ])
            ], className="mb-4")
        ], width=12, lg=8)
    ]),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Real-time Monitoring"),
                dbc.CardBody([
                    dcc.Graph(id='live-graph'),
                    dcc.Interval(
                        id='graph-update',
                        interval=1000,  # in milliseconds
                        n_intervals=0
                    )
                ])
            ])
        ], width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("System Controls"),
                dbc.CardBody([
                    dbc.Button("Start Monitoring", color="success", className="me-2"),
                    dbc.Button("Stop Monitoring", color="danger", className="me-2"),
                    dbc.Button("Reset System", color="warning")
                ])
            ], className="my-4")
        ], width=12)
    ])
], fluid=True)

@app.callback(
    [Output('live-graph', 'figure'),
     Output('current-temp', 'children'),
     Output('current-vib', 'children'),
     Output('current-press', 'children'),
     Output('last-checked', 'children')],
    [Input('graph-update', 'n_intervals')]
)
def update_graph(n):
    times, temperature, vibration, pressure = generate_sensor_data()
    
    fig = go.Figure()
    
    # Add traces
    fig.add_trace(go.Scatter(x=times, y=temperature, name="Temperature (°F)"))
    fig.add_trace(go.Scatter(x=times, y=vibration, name="Vibration (g)"))
    fig.add_trace(go.Scatter(x=times, y=pressure, name="Pressure (PSI)"))
    
    # Update layout
    fig.update_layout(
        title="Sensor Readings Over Time",
        xaxis_title="Time",
        yaxis_title="Value",
        height=500,
        margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    current_temp = f"{temperature[-1]:.1f}°F"
    current_vib = f"{vibration[-1]:.2f}g"
    current_press = f"{pressure[-1]:.1f} PSI"
    last_checked = f"Last checked: {datetime.now().strftime('%H:%M:%S')}"
    
    return fig, current_temp, current_vib, current_press, last_checked

if __name__ == '__main__':
    # Get port from environment variable or use 8050 as default
    port = int(os.environ.get('PORT', 8050))
    app.run_server(debug=False, host='0.0.0.0', port=port)
