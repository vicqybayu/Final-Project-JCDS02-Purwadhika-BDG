import pandas as pd

states = ['IN', 'CT', 'FL', 'NC', 'IL', 'OK', 'AR', 'MN', 'CA', 'SC', 'TX',
       'LA', 'IA', 'TN', 'MS', 'OH', 'MD', 'VA', 'MA', 'PA', 'OR', 'ME',
       'KS', 'MI', 'AK', 'WA', 'CO', 'WY', 'UT', 'MO', 'AZ', 'ID', 'RI',
       'NJ', 'NH', 'NM', 'NV', 'NY', 'ND', 'VT', 'WI', 'MT', 'AL', 'GA',
       'KY', 'NE', 'WV', 'SD', 'DE', 'DC', 'HI']

naics = ['Retail_trade', 'Accom/Food_serv', 'Healthcare/Social_assist',
       'Manufacturing', 'Other_no_pub', 'Construction', 'Wholesale_trade',
       'Educational', 'RE/Rental/Lease', 'Prof/Science/Tech',
       'Information', 'Arts/Entertain/Rec', 'Finance/Insurance',
       'Min/Quar/Oil_Gas_ext', 'Admin_sup/Waste_Mgmt_Rem', 'Trans/Ware',
       'Ag/For/Fish/Hunt', 'Public_Admin', 'Utilities', 'Mgmt_comp']

def data_clean():
    clean_data = pd.read_csv('df_for_visualization_rev_fix.csv').head(100)
    return clean_data