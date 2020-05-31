import plotly
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import json

def usa_choropleth():

    df = pd.read_csv('df_for_visualization_rev_fix.csv')

    df_state_default_rate = df.groupby(['State', 'MIS_Status'])['State'].count().unstack('MIS_Status')
    df_state_default_rate['default_rate'] = df_state_default_rate['CHGOFF'] / (df_state_default_rate['CHGOFF'] + df_state_default_rate['P I F'])

    fig = go.Figure(data=go.Choropleth(
        locations=df_state_default_rate.index,
        z = df_state_default_rate.default_rate, # Data to be color-coded
        locationmode = 'USA-states', # set of locations match entries in `locations`
        colorscale = 'Reds',
        colorbar_title = "Default Rate",
    ))

    fig.update_layout(
        title_text = 'SBA Default Rate per State',
        geo_scope='usa', # limite map scope to USA
    )
    return fig

def default_per_year():
    df = pd.read_csv('df_for_visualization_rev_fix.csv')

    default_disbursement_year = pd.DataFrame(
        {
            'DisbursementYear':pd.to_datetime(df.DisbursementDate).dt.year, 
            'MIS_Status':df.MIS_Status
        }
    ).groupby(['DisbursementYear', 'MIS_Status'])['DisbursementYear'].count().unstack('MIS_Status')

    fig = go.Figure()
    fig.add_trace(go.Bar(x=default_disbursement_year.index,
                    y=default_disbursement_year['P I F'],
                    name='Paid in Full',
                    marker_color='rgb(55, 83, 109)'
                    ))
    fig.add_trace(go.Bar(x=default_disbursement_year.index,
                    y=default_disbursement_year['CHGOFF'],
                    name='Default',
                    marker_color='rgb(26, 118, 255)'
                    ))

    fig.update_layout(
        title='Default and Paid in Full Loan by Year',
        xaxis_tickfont_size=14,
        yaxis=dict(
            title='Count',
            titlefont_size=16,
            tickfont_size=14,
        ),
        legend=dict(
            x=0,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        barmode='overlay',
        bargap=0, # gap between bars of adjacent location coordinates.
        bargroupgap=0 # gap between bars of the same location coordinate.
    )

    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def default_per_ind():
    df = pd.read_csv('df_for_visualization_rev_fix.csv')
    df_default_per_ind = df.groupby(['NAICS', 'MIS_Status'])['NAICS'].count().unstack('MIS_Status')
    df_default_per_ind['default_rate'] = df_default_per_ind['CHGOFF']/(df_default_per_ind['CHGOFF'] + df_default_per_ind['P I F'])
    df_default_per_ind.sort_values('default_rate', ascending=False)

    fig = go.Figure()
    fig.add_trace(go.Bar(x=df_default_per_ind.index,
                    y=df_default_per_ind['P I F'],
                    name='Paid in Full',
                    marker_color='rgb(55, 83, 109)'
                    ))
    fig.add_trace(go.Bar(x=df_default_per_ind.index,
                    y=df_default_per_ind['CHGOFF'],
                    name='Default',
                    marker_color='rgb(26, 118, 255)'
                    ))

    fig.update_layout(
        title='Default and Paid in Full Count per Industry',
        xaxis_tickfont_size=14,
        yaxis=dict(
            title='Count',
            titlefont_size=16,
            tickfont_size=14,
        ),
        legend=dict(
            x=0,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        barmode='group',
        bargap=0.2, # gap between bars of adjacent location coordinates.
        bargroupgap=0 # gap between bars of the same location coordinate.
    )
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def default_per_state():
    df = pd.read_csv('df_for_visualization_rev_fix.csv')
    df_state_default_rate = df.groupby(['State', 'MIS_Status'])['State'].count().unstack('MIS_Status')
    df_state_default_rate['default_rate'] = df_state_default_rate['CHGOFF'] / (df_state_default_rate['CHGOFF'] + df_state_default_rate['P I F'])
    df_state_default_rate.sort_values('default_rate', ascending=False)

    fig = go.Figure()
    fig.add_trace(go.Bar(x=df_state_default_rate.index,
                    y=df_state_default_rate['P I F'],
                    name='Paid in Full',
                    marker_color='rgb(55, 83, 109)'
                    ))
    fig.add_trace(go.Bar(x=df_state_default_rate.index,
                    y=df_state_default_rate['CHGOFF'],
                    name='Default',
                    marker_color='rgb(26, 118, 255)'
                    ))

    fig.update_layout(
        title='Default and Paid in Full Count per Industry',
        xaxis_tickfont_size=14,
        yaxis=dict(
            title='Count',
            titlefont_size=16,
            tickfont_size=14,
        ),
        legend=dict(
            x=0.75,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        barmode='group',
        bargap=0.2, # gap between bars of adjacent location coordinates.
        bargroupgap=0 # gap between bars of the same location coordinate.
    )
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json