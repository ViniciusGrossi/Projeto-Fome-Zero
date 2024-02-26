import pandas as pd
import streamlit as st
import folium as folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

st.set_page_config(page_title='Home', layout='wide')

st.title('Fome Zero!')
st.markdown('## O Melhor lugar para encontrar seu mais novo restaurante favorito!')

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
    st.sidebar.header('Fome Zero')

    all_countries = st.sidebar.checkbox(
        'All Countries',      
    )
    if all_countries:

        filter_countries = df1['Country Name'].unique()

    if not all_countries:
        filter_countries = st.sidebar.multiselect(
            'Selecione os países que quer ver',
            df1['Country Name'].unique(),
            ['Philippines', 'Brazil', 'Australia', 'United States', 'South Africa', 'United Arab Emirates'] 
        )
    return filter_countries
def metrics(df1):
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            unique_restaurants = len(df1['Restaurant ID'].unique())
            col1.metric('Restaurantes Registrados',unique_restaurants)
        with col2:
            unique_countries = len(df1['Country Name'].unique())
            col2.metric('Países Registrados',unique_countries)
        with col3:
            unique_cities = len(df1['City'].unique())
            col3.metric('Cidades Registradas',unique_cities)
        with col4:
            total_ratings = df1.loc[:,'Votes'].sum()
            col4.metric('Total de votos',total_ratings)
        with col5:
            unique_cuisines = len(df1['Cuisines'].unique())
            col5.metric('Total de culinárias',unique_cuisines)
        return col1, col2, col3, col4, col5
def map(df1_filtered):
    df1_filtered = df1[df1['Country Name'].isin(filter_countries)]
    df_coordinates = pd.DataFrame(df1_filtered, columns=['Latitude', 'Longitude', 'City', 'Aggregate rating','Colors'])
    #map
    map = folium.Map()
    marker_cluster = MarkerCluster().add_to(map)

    for index, location_info in df_coordinates.iterrows():
        color = location_info['Colors']
        custom_icon = folium.Icon(color=color)

        folium.Marker( [location_info['Latitude'],
                        location_info['Longitude']],
                        popup=location_info['City'],
                        tooltip = 'Click here',
                        icon=custom_icon).add_to(marker_cluster)
    folium_static(map,width=1024,height=600)
    return index

df = pd.read_csv('dataset/zomato.csv')
df1 = clean_code(df)
#------------------Sidebar----------------------
filter_countries = sidebar(df1)
#------------------Layout----------------------
with st.container():
    col1, col2, col3, col4, col5 = metrics(df1)

index = map(df1)
