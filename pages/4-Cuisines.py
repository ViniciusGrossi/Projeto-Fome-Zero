import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go

st.set_page_config(page_title='Cuisines', layout='wide')

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
def sidebar (df1):
    worsts = st.sidebar.toggle('The Worts')
    num_cuisines = st.sidebar.slider(
            "Number of cuisines", 1, 50, 5
        )
    return worsts, num_cuisines
def help_text(df1):

    help_text = f"""
            Restaurant: {df_aux['Restaurant Name'].min()}
            \nCity: {df_aux['City'].min()}
            \nCountry: {df_aux['Country Name'].min()}
            \nCost_in_Dollar: {df_aux['Cost_in_Dollar'].min()}
            """
    return help_text
def cheapest_cuisines(df1):

    df_aux = df1.loc[:,['Cuisines','Cost_in_Dollar']].groupby('Cuisines').max().sort_values(['Cost_in_Dollar'], ascending= True).reset_index()
    df_aux = df_aux[df_aux['Cost_in_Dollar'] > 0]
    fig = px.bar(df_aux.head(num_cuisines), x='Cuisines', y='Cost_in_Dollar')
    return fig
def lowest_average_rating(df1):
    df_aux = df1.loc[:,['Cuisines','Aggregate rating']].groupby('Cuisines').max().sort_values(['Aggregate rating'], ascending= True).reset_index()
    df_aux = df_aux[df_aux['Aggregate rating'] > 0]
    fig = px.bar(df_aux.head(num_cuisines), x='Cuisines', y='Aggregate rating')
    return fig
def cuisines_least_online_deliveries(df1):
    double = df1[(df1['Has Online delivery'] == 1) & (df1['Has Table booking'] == 1)]
    df_aux = double.loc[:,['Cuisines','Restaurant Name']].groupby('Cuisines').count().sort_values(['Restaurant Name'], ascending= True).reset_index()
    fig = px.bar(df_aux.head(num_cuisines), x='Cuisines', y= 'Restaurant Name')
    return fig
def expensive_cuisines(df1):
        df_aux = df1.loc[:,['Cuisines','Cost_in_Dollar']].groupby('Cuisines').max().sort_values(['Cost_in_Dollar'], ascending= False).reset_index()
        fig = px.bar(df_aux.head(num_cuisines), x='Cuisines', y='Cost_in_Dollar')
        return fig
def highest_average_rating(df1):
        df_aux = df1.loc[:,['Cuisines','Aggregate rating']].groupby('Cuisines').max().sort_values(['Aggregate rating'], ascending= False).reset_index()
        fig = px.bar(df_aux.head(num_cuisines), x='Cuisines', y='Aggregate rating')
        return fig
def cuisines_most_online_delivery(df1):
        double = df1[(df1['Has Online delivery'] == 1) & (df1['Has Table booking'] == 1)]
        df_aux = double.loc[:,['Cuisines','Restaurant Name']].groupby('Cuisines').count().sort_values(['Restaurant Name'], ascending= False).reset_index() 
        fig = px.bar(df_aux.head(num_cuisines), x='Cuisines', y= 'Restaurant Name')
        return fig 

df = pd.read_csv('C:/Users/vinic/Documents/Data Science/Data Analysis/Comunidade DS/Projeto-Final/dataset/zomato.csv')
df1 = clean_code(df)

#------------------Sidebar----------------------
worsts, num_cuisines = sidebar (df1)
#------------------Layout----------------------

st.title('Cuisines')

if worsts:   
    with st.container():
        st.markdown('### The Worths')
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.markdown('#### Italian')
            italian = df1[(df1['Cuisines'].str.contains('Italian', case=False, na=False)) & ((df1['Aggregate rating'])!= 0 )& ((df1['Cost_in_Dollar'])!= 0) ]    
            df_aux = italian.loc[:,['Restaurant Name','Aggregate rating', 'City','Country Name','Cost_in_Dollar']].groupby(['Restaurant Name', 'City','Country Name','Cost_in_Dollar']).mean().sort_values(['Aggregate rating'], ascending = False).reset_index()
            
            st.metric(label='Italian: ' + df_aux['Restaurant Name'].min(), value=df_aux['Aggregate rating'].min(), help= help_text(df1))
        with col2:
            st.markdown('#### American')
            italian = df1[(df1['Cuisines'].str.contains('American', case=False, na=False)) & ((df1['Aggregate rating'])!= 0 )& ((df1['Cost_in_Dollar'])!= 0) ]
            df_aux = italian.loc[:,['Restaurant Name','Aggregate rating', 'City','Country Name','Cost_in_Dollar']].groupby(['Restaurant Name', 'City','Country Name','Cost_in_Dollar']).mean().sort_values(['Aggregate rating'], ascending = False).reset_index()
            
            st.metric(label='American: ' + df_aux['Restaurant Name'].min(), value=df_aux['Aggregate rating'].min(), help=help_text(df1))
        with col3:
            st.markdown('#### Arabian')
            italian = df1[(df1['Cuisines'].str.contains('Arabian', case=False, na=False)) & ((df1['Aggregate rating'])!= 0 )& ((df1['Cost_in_Dollar'])!= 0) ]
            df_aux = italian.loc[:,['Restaurant Name','Aggregate rating', 'City','Country Name','Cost_in_Dollar']].groupby(['Restaurant Name', 'City','Country Name','Cost_in_Dollar']).mean().sort_values(['Aggregate rating'], ascending = False).reset_index()

            st.metric(label='Arabian: ' + df_aux['Restaurant Name'].min(), value=df_aux['Aggregate rating'].min(), help=help_text(df1))
        with col4:
            st.markdown('#### Japanese')
            italian = df1[(df1['Cuisines'].str.contains('Japanese', case=False, na=False)) & ((df1['Aggregate rating'])!= 0 )& ((df1['Cost_in_Dollar'])!= 0) ]
            df_aux = italian.loc[:,['Restaurant Name','Aggregate rating', 'City','Country Name','Cost_in_Dollar']].groupby(['Restaurant Name', 'City','Country Name','Cost_in_Dollar']).mean().sort_values(['Aggregate rating'], ascending = False).reset_index()
        
            st.metric(label='Japanese: ' + df_aux['Restaurant Name'].min(), value=df_aux['Aggregate rating'].min(), help=help_text(df1))
        with col5:
            st.markdown('#### Home-made')
            italian = df1[(df1['Cuisines'].str.contains('Home-made', case=False, na=False)) & ((df1['Aggregate rating'])!= 0 )& ((df1['Cost_in_Dollar'])!= 0) ]
            df_aux = italian.loc[:,['Restaurant Name','Aggregate rating', 'City','Country Name','Cost_in_Dollar']].groupby(['Restaurant Name', 'City','Country Name','Cost_in_Dollar']).mean().sort_values(['Aggregate rating'], ascending = False).reset_index()
            
            st.metric(label='Home-made: ' + df_aux['Restaurant Name'].min(), value=df_aux['Aggregate rating'].min(), help=help_text(df1))
    with st.container():
        st.markdown('## Cheapest Cuisines')
        fig = cheapest_cuisines(df1)
        st.plotly_chart(fig, use_container_width=True)

        st.markdown('## Lowest Average Rating')
        fig = lowest_average_rating(df1)
        st.plotly_chart(fig, use_container_width=True)

        st.markdown('## Cuisines with least Online Deliveries')
        fig = cuisines_least_online_deliveries(df1)
        st.plotly_chart(fig, use_container_width=True)
else:
        with st.container():
            st.markdown('### The Bests')
            col1, col2, col3, col4, col5 = st.columns(5)
            
            with col1:
                st.markdown('#### Italian')
                italian = df1[(df1['Cuisines'].str.contains('Italian', case=False, na=False)) & (df1['Aggregate rating'])!= 0]
                df_aux = italian.loc[:,['Restaurant Name','Aggregate rating', 'City','Country Name','Cost_in_Dollar']].groupby(['Restaurant Name', 'City','Country Name','Cost_in_Dollar']).mean().sort_values(['Aggregate rating'], ascending = False).reset_index()

                st.metric(label='Italian: ' + df_aux['Restaurant Name'].max(), value=df_aux['Aggregate rating'].max(), help=help_text(df1))
            with col2:
                st.markdown('#### American')
                italian = df1[(df1['Cuisines'].str.contains('American', case=False, na=False)) & (df1['Aggregate rating'])!= 0]
                df_aux = italian.loc[:,['Restaurant Name','Aggregate rating', 'City','Country Name','Cost_in_Dollar']].groupby(['Restaurant Name', 'City','Country Name','Cost_in_Dollar']).mean().sort_values(['Aggregate rating'], ascending = False).reset_index()
                
                st.metric(label='American: ' + df_aux['Restaurant Name'].max(), value=df_aux['Aggregate rating'].max(), help=help_text(df1))
            with col3:
                st.markdown('#### Arabian')
                italian = df1[(df1['Cuisines'].str.contains('Arabian', case=False, na=False)) & (df1['Aggregate rating'])!= 0]
                df_aux = italian.loc[:,['Restaurant Name','Aggregate rating', 'City','Country Name','Cost_in_Dollar']].groupby(['Restaurant Name', 'City','Country Name','Cost_in_Dollar']).mean().sort_values(['Aggregate rating'], ascending = False).reset_index()

                st.metric(label='Arabian: ' + df_aux['Restaurant Name'].max(), value=df_aux['Aggregate rating'].max(), help=help_text(df1))
            with col4:
                st.markdown('#### Japanese')
                italian = df1[(df1['Cuisines'].str.contains('Japanese', case=False, na=False)) & (df1['Aggregate rating'])!= 0]
                df_aux = italian.loc[:,['Restaurant Name','Aggregate rating', 'City','Country Name','Cost_in_Dollar']].groupby(['Restaurant Name', 'City','Country Name','Cost_in_Dollar']).mean().sort_values(['Aggregate rating'], ascending = False).reset_index()
        
                st.metric(label='Japanese: ' + df_aux['Restaurant Name'].max(), value=df_aux['Aggregate rating'].max(), help=help_text(df1))
            with col5:
                st.markdown('#### Home-made')
                italian = df1[(df1['Cuisines'].str.contains('Home-made', case=False, na=False)) & (df1['Aggregate rating'])!= 0]
                df_aux = italian.loc[:,['Restaurant Name','Aggregate rating', 'City','Country Name','Cost_in_Dollar']].groupby(['Restaurant Name', 'City','Country Name','Cost_in_Dollar']).mean().sort_values(['Aggregate rating'], ascending = False).reset_index()
               
                st.metric(label='Home-made: ' + df_aux['Restaurant Name'].max(), value=df_aux['Aggregate rating'].max(), help=help_text(df1))

        with st.container():
            st.markdown('## Most Expensive Cuisines')
            fig = expensive_cuisines(df1)
            st.plotly_chart(fig, use_container_width=True)

            st.markdown('## Highest Average Rating')
            fig = highest_average_rating(df1)
            st.plotly_chart(fig, use_container_width=True)

            st.markdown('## Cuisines with most Online Deliver')
            fig = cuisines_most_online_delivery(df1)
            st.plotly_chart(fig, use_container_width=True)
