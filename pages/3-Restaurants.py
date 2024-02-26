#Libraries
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go

st.set_page_config(page_title='Restaurants', layout='wide')

def clean_code (df1):

    df1 = df.copy()
    #Transforma o df1 em um dataframe
    df1 = pd.DataFrame(df)
    #Cria a coluna Cost_in_Dollar, que converte a coluna Average Cost for two de acordo com a coluna Currency em dolár. Cada moeda recebe sua conversão para dólar

    exchange_rates = {
        'Botswana Pula(P)': 0.021,
        'Brazilian Real(R$)': 0.19,
        'Dollar($)': 1.0,
        'Emirati Diram(AED)': 0.27,
        'Indian Rupees(Rs.)': 0.014,
        'Indonesian Rupiah(IDR)': 0.000071,
        'NewZealand($)': 0.69,
        'Pounds(£)': 1.39,
        'Qatari Rial(QR)': 0.27,
        'Rand(R)': 0.068,
        'Sri Lankan Rupee(LKR)': 0.0051,
        'Turkish Lira(TL)': 0.11
    }
    df1['Cost_in_Dollar'] = [df1['Average Cost for two'].iloc[i] * exchange_rates[currency]
                            if currency in exchange_rates else df1['Average Cost for two'].iloc[i]
                            for i, currency in enumerate(df1['Currency'])]
    #Elimina qualquer valor maior que 90000 da coluna Average Cost for two
    df1['Average Cost for two'] = df1['Average Cost for two'].apply(lambda x: 50 if x > 90000 else x)
    df1['Cost_in_Dollar'] = df1['Cost_in_Dollar'].apply(lambda x: 50 if x > 90000 else x)
    #Converte os códigos dos países em nomes
    new_list = [162, 30, 14, 1, 37, 94, 148, 216, 166, 184, 189, 191, 208, 214, 215]
    country_list = ['Philippines','Brazil','Australia','Indian','Canada','Indonesia','New Zealand','United States','Qatar','Singapore','South Africa','Sri Lanka','Turkey','United Arab Emirates','United Kingdom']
    country_mapping = dict(zip(new_list, country_list))
    df1['Country Name'] = df1['Country Code'].map(country_mapping)
    

    # Limpa a coluna Cuisines
    df1["Cuisines"] = df1["Cuisines"].apply(lambda x: str(x).split(",")[0] if isinstance(x, str) else x)

    # Atribuindo nome aos códigos de price range
    def create_price_type(price_range):
        if price_range == 1:
            return "cheap"
        elif price_range == 2:
            return "normal"
        elif price_range == 3:
            return "expensive"
        else:
            return "gourmet"
    df1['Price Type'] = df1['Price range'].apply(create_price_type)

    # Atribuindo nome aos códigos de rating colors

    COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred",
    }
    def color_name(color_code):
        return COLORS[color_code]
    df1['Colors'] = df1['Rating color'].apply(color_name)
    return df1
def sidebar(df1):
    all_countries = st.sidebar.toggle(
        'All Countries',      
    )
    if all_countries:
        filter_countries = df1['Country Name'].unique()
    if not all_countries:
        filter_countries = st.sidebar.multiselect(
            'Select Countries',
            df1['Country Name'].unique(),
            ['Philippines', 'Brazil', 'Australia', 'United States', 'South Africa', 'United Arab Emirates'] 
        )
    df_filtered = df1[df1['Country Name'].isin(filter_countries)]

    all_cuisines = st.sidebar.toggle(
        'All Cuisines',      
    )
    if all_cuisines:
        filter_cuisines = df1['Cuisines'].unique()
    if not all_cuisines:
        filter_cuisines = st.sidebar.multiselect(
            'Select Cuisines',
            df1['Cuisines'].unique(),
            ['Italian', 'American', 'Arabian', 'Japanese', 'Home-made', 'Indian'] 
        )
    df_filtered = df1[df1['Cuisines'].isin(filter_cuisines)]

    st.sidebar.markdown("""___""")
    all_cities = st.sidebar.toggle(
        'All Cities',      
    )
    total_cities = len(df1['City'])
    if all_cities:
        num_cities = total_cities
    else:
        num_cities = st.sidebar.slider(
            "Number of Cities", 1, 120, 10
        )
    return df_filtered, num_cities
def restaurants_votes(df1):

    df_aux = df_filtered.loc[:,['Restaurant Name','Votes','Country Name']].groupby(['Restaurant Name','Country Name']).sum().sort_values(['Votes'], ascending = False).reset_index()
    fig = px.bar(df_aux.head(num_cities), x= 'Restaurant Name', y= 'Votes', color = 'Country Name')
    return fig
def restaurants_votes(df1):
        
    df_aux = df_filtered.loc[:,['Restaurant Name','Aggregate rating','Country Name']].groupby(['Restaurant Name','Country Name']).mean().sort_values(['Aggregate rating'], ascending = False).reset_index()
    fig = px.bar(df_aux.head(num_cities), x='Restaurant Name', y ='Aggregate rating',color ='Country Name')
    return fig
def restaurants_cost_in_dollar(df1):
        df_aux = df_filtered.loc[:,['Restaurant Name','Cost_in_Dollar','Country Name']].groupby(['Restaurant Name','Country Name']).max().sort_values(['Cost_in_Dollar'], ascending = False).reset_index()
        fig = px.bar(df_aux.head(num_cities), x= 'Restaurant Name', y= 'Cost_in_Dollar')
        return fig
def brazilian_restaurants_hightest_rating(df1):
            
    brazilian = df1[(df1['Cuisines'] == 'Brazilian') & (df1['Country Name'] == 'Brazil')]
    df_aux = brazilian.loc[:,['Restaurant Name','Aggregate rating']].groupby('Restaurant Name').mean().sort_values(['Aggregate rating'], ascending = False).reset_index()
    fig = px.bar(df_aux.head(10), x='Restaurant Name', y='Aggregate rating')
    return fig
def brazilian_restaurants_lowest_rating(df1):

    brazilian = df1[(df1['Cuisines'] == 'Brazilian') & (df1['Aggregate rating'] != 0)]
    df_aux = brazilian.loc[:,['Restaurant Name','Aggregate rating']].groupby('Restaurant Name').mean().sort_values(['Aggregate rating'], ascending = True).reset_index()
    fig = px.bar(df_aux.head(10), x= 'Restaurant Name', y= 'Aggregate rating')
    return fig
def accept_table_booking(df1):
            
    table_booking = df_filtered[df_filtered['Has Table booking'] == 1]
    df_aux_table_booking = table_booking.loc[:,['Restaurant Name','Has Table booking', 'Cost_in_Dollar']].groupby(['Restaurant Name']).mean().sort_values(['Cost_in_Dollar'], ascending= False).reset_index()
    fig = px.bar(df_aux_table_booking.head(num_cities), x='Restaurant Name', y= 'Cost_in_Dollar' )
    metric_table_booking = round(df_aux_table_booking['Cost_in_Dollar'].mean())
    return fig, metric_table_booking
def dont_accept_table_booking(df1):
            
    not_table_booking = df_filtered[df_filtered['Has Table booking'] == 0]
    df_aux_not_table_booking = not_table_booking.loc[:,['Restaurant Name','Has Table booking', 'Cost_in_Dollar']].groupby(['Restaurant Name']).mean().sort_values(['Cost_in_Dollar'], ascending= False).reset_index()
    fig = px.bar(df_aux_not_table_booking.head(num_cities), x='Restaurant Name', y= 'Cost_in_Dollar' )
    metric_not_table_booking = round(df_aux_not_table_booking['Cost_in_Dollar'].mean())
    return fig, metric_not_table_booking

df = pd.read_csv('C:/Users/vinic/Documents/Data Science/Data Analysis/Comunidade DS/Projeto-Final/dataset/zomato.csv')
df1 = clean_code(df)

#------------------Sidebar----------------------
df_filtered, num_cities = sidebar(df1)
#------------------Layout----------------------
st.title('Restaurants')
with st.container():
    st.markdown('### Restaurantes with most Votes')
    fig = restaurants_votes(df1)
    st.plotly_chart(fig, use_container_width=True)
with st.container():
    st.markdown('### Restaurantes with Better Rating')
    fig = restaurants_votes(df1)
    st.plotly_chart(fig, use_container_width=True)
with st.container():
    st.markdown('### Restaurantes with Hightest Cost in Dollar')
    fig = restaurants_cost_in_dollar(df1)
    st.plotly_chart(fig, use_container_width=True)
with st.container():
    col1, col2 = st.columns(2)
    with col1: 
        st.markdown('### Brazilian Restaurants with Hightest Rating')
        fig = brazilian_restaurants_hightest_rating(df1)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.markdown('### Brazilian Restaurants with Lowest Rating')
        fig = brazilian_restaurants_lowest_rating(df1)
        st.plotly_chart(fig, use_container_width=True)
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('### Accept Table Booking')
        fig, metric_table_booking = accept_table_booking(df1)
        st.plotly_chart(fig, use_container_width=True)
        st.metric('Average Cost',metric_table_booking)
    with col2:
        st.markdown('### Dont  Accept Table Booking')
        fig, metric_not_table_booking = dont_accept_table_booking(df1)
        st.plotly_chart(fig, use_container_width=True)
        st.metric('Average Cost',metric_not_table_booking)