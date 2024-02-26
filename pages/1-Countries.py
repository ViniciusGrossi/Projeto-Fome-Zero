#Libraries
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go

st.set_page_config(page_title='Countries', layout='wide')
#Functions
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

    st.sidebar.markdown("""___""")
    return df_filtered
def country_cities(df1):

    df_aux = df_filtered.loc[:,['Country Name','City']].groupby('Country Name').nunique().sort_values(['City'], ascending = False).reset_index()
    fig = px.bar(df_aux.head(), x='Country Name', y='City', color='Country Name')
    return fig
def higher_lower_ratings(df1):

    df_aux_higher = df_filtered.loc[:,['Country Name','Aggregate rating']].groupby('Country Name').mean().sort_values(by=['Aggregate rating'], ascending=False).reset_index()
    df_aux = pd.merge(df_aux_higher.head(), df_aux_higher.tail(), on= 'Country Name', how='outer')
    df_aux.columns = ['Country Name', 'Higher Rating', 'Lower Rating']
    fig = px.bar(df_aux, x='Country Name', y=['Higher Rating', 'Lower Rating'], barmode='group',
        color_discrete_sequence=['blue', 'orange'],
        labels={'Higher Rating': 'Higher Rating', 'Lower Rating': 'Lower Rating'})
    return fig
def countries_restaurants(df1):
            
    df_aux = df_filtered.loc[:, ['Country Name','Restaurant ID']].groupby(['Country Name']).count().sort_values(by=['Restaurant ID'], ascending=False).reset_index()
    fig = px.bar(df_aux.head(), x='Country Name', y='Restaurant ID', color='Country Name' )
    return fig 
def countries_cuisines(df1):
            
    df_aux = df_filtered.loc[:,['Country Name','Cuisines']].groupby('Country Name').nunique().sort_values(['Cuisines'], ascending=False).reset_index()
    fig = px.bar(df_aux.head(), x='Country Name', y='Cuisines', color='Country Name' )
    return fig
def countries_votes(df1):
            
    df_aux = df_filtered.loc[:,['Country Name','Votes']].groupby('Country Name').sum().sort_values(by=['Votes'], ascending=False).reset_index()
    fig = px.bar(df_aux.head(), x='Country Name', y='Votes',color='Country Name' )
    return fig
def countries_cost_in_dollar(df1):

    df_aux = df_filtered.loc[:,['Country Name','Cost_in_Dollar']].groupby('Country Name').mean().sort_values(by=['Cost_in_Dollar'], ascending=False).reset_index()
    fig = px.bar(df_aux, x='Country Name', y='Cost_in_Dollar', color='Country Name' )
    return fig
def countries_goumert_restaurants(df1):
            
    restaurants_4_price = df_filtered[df_filtered['Price Type'] == 'gourmet']
    df_aux = restaurants_4_price.loc[:, ['Restaurant ID', 'Country Name']].groupby('Country Name').count().sort_values(by=['Restaurant ID'], ascending=False).reset_index()
    fig = px.bar(df_aux.head(), x='Country Name', y='Restaurant ID', color='Country Name' )
    return fig
def countries_restaurants_deliver(df1):
            
    delivering = df_filtered[df_filtered['Is delivering now'] == 1]
    df_aux = delivering.loc[:,['Country Name','Restaurant ID']].groupby('Country Name').count().sort_values(by=['Restaurant ID'], ascending= False).reset_index()
    fig = px.bar(df_aux.head(), x='Country Name', y='Restaurant ID', color='Country Name' )
    return fig
def countries_restaurants_table_booking(df1):

    table_booking = df_filtered[df_filtered['Has Table booking'] == 1]
    df_aux = table_booking.loc[:,['Country Name','Restaurant ID']].groupby('Country Name').count().sort_values(by=['Restaurant ID'], ascending= False).reset_index()
    fig = px.bar(df_aux.head(), x='Country Name', y='Restaurant ID', color='Country Name' )
    return fig
def countries_average_votes(df1):

    df_aux = df_filtered.loc[:,['Country Name','Votes']].groupby('Country Name').mean().sort_values(by=['Votes'], ascending=False).reset_index()
    fig = px.bar(df_aux.head(), x='Country Name', y='Votes', color='Country Name' )
    return fig


df = pd.read_csv('C:/Users/vinic/Documents/Data Science/Data Analysis/Comunidade DS/Projeto-Final/dataset/zomato.csv')
df1 = clean_code(df)

#------------------Sidebar----------------------
df_filtered = sidebar(df1)
#------------------Layout----------------------
st.title('Countries')

tab1, tab2 = st.tabs(['Visão Geral', 'Visão Específica'])
with tab1:
    with st.container():
        st.markdown('# Countries with most Cities')
        fig = country_cities(df1)
        st.plotly_chart(fig, use_container_width=True)

    with st.container():
        st.markdown('# Countries with most Restaurants')
        fig = countries_restaurants(df1)
        st.plotly_chart(fig, use_container_width=True)

    with st.container():
        st.markdown('# Countries with most Cuisines types')
        fig = countries_cuisines(df1)
        st.plotly_chart(fig, use_container_width=True)
        
    with st.container():
        st.markdown('# Countries with most Votes')
        fig = countries_votes(df1)
        st.plotly_chart(fig, use_container_width=True)

    with st.container():
        st.markdown('# Higher and Lower Ratings ')
        
        fig = higher_lower_ratings(df1)
        st.plotly_chart(fig, use_container_width=True)

    with st.container():
        st.markdown('# Average Cost for two by Country ')
        fig = countries_cost_in_dollar(df1)
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    with st.container():
        st.markdown('# Countries with most Gourmets Restaurants')
        fig = countries_goumert_restaurants(df1)
        st.plotly_chart(fig, use_container_width=True)

    with st.container():
        st.markdown('# Countries with most Restaurants that deliver')
        fig = countries_restaurants_deliver(df1)
        st.plotly_chart(fig, use_container_width=True)

    with st.container():
        st.markdown('# Countries with most Restaurants that accepts Table Bookings')
        fig = countries_restaurants_table_booking(df1)
        st.plotly_chart(fig, use_container_width=True)

    with st.container():
        st.markdown('# Countries with most Average Votes')
        fig = countries_average_votes(df1)
        st.plotly_chart(fig, use_container_width=True)