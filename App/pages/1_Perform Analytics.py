# Jai Hanuman 🙏🙏🙏🙏🙏

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="Property Analytics")

st.markdown("""
<h1 style='text-align:center;'>📊 Property Analytics Dashboard</h1>
<p style='text-align:center;color:gray;font-size:1.1rem;'>
    Jaipur Real Estate — Deep Insights
</p>
""", unsafe_allow_html=True)

st.markdown("---")

st.subheader("Please Select Property Type")
property_type = st.radio(
    "",
    options=["🏢 Flat / Builder Floor", "🏠 Independent House / Villa", "🌍 Plot"],
    horizontal=True
)

def load_data(property_type):
    if property_type == "🏢 Flat / Builder Floor":
        df = pd.read_csv('App/data/flats_for_insight.csv')
        df = df.drop(columns=['Unnamed: 0'], errors='ignore')
        df['property_type'] = df['property_type'].str.strip().str.lower()
        df['furnished_status'] = df['furnished_status'].str.strip().str.lower()
        df['furnished_status'] = df['furnished_status'].replace({
            'semi-furnished': 'Semi-Furnished',
            'unfurnished':    'Unfurnished',
            'furnished':      'Furnished'
        })
        df['bhk_display'] = df['bhk']
        df['bhk_num'] = pd.to_numeric(
            df['bhk'].replace({'Studio': '0.5'}), errors='coerce'
        )

        df['price_L'] = df['total_price'] / 100000
        df['location_area'] = df['location_area'].str.title()
    elif property_type == "🏠 Independent House / Villa":
        df = pd.read_csv('App/data/house_insights (1).csv')
        df['property_type'] = df['property_type'].str.strip().str.lower()
        df['furnished_status'] = df['furnished_status'].str.strip().str.lower()
        df['furnished_status'] = df['furnished_status'].replace({
            'semi-furnished': 'Semi-Furnished',
            'unfurnished':    'Unfurnished',
            'furnished':      'Furnished'
        })
        df['bhk_display'] = df['bhk']
        df['bhk_num'] = pd.to_numeric(df['bhk'])
        df['price_L'] = df['total_price'] / 100000
        df['location_area'] = df['location_area'].str.title()
    
    elif property_type == "🌍 Plot":
        df = pd.read_csv('App/data/plot_insights.csv')
        
        df['price_L'] = df['total_price'] / 100000
        # df['location_area'] = df['location_area'].str.title()
        
    return df

    
df_view = load_data(property_type)


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@400;500;600&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
h1, h2, h3 { font-family: 'DM Serif Display', serif !important; }
.stApp { background-color: #f7f5f0; }

.metric-card {
    background: white;
    border-radius: 12px;
    padding: 20px 24px;
    border: 1px solid #e8e4dc;
    text-align: center;
}
.metric-num {
    font-family: 'DM Serif Display', serif;
    font-size: 1.8rem;
    color: #1a1a2e;
}
.metric-label {
    font-size: 0.78rem;
    color: #6b6b6b;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-top: 4px;
}
.section-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.4rem;
    color: #1a1a2e;
    margin: 1.5rem 0 0.5rem;
    padding-bottom: 6px;
    border-bottom: 2px solid #e8e4dc;
}
</style>
""", unsafe_allow_html=True)



def plot_map(property_type):
    if property_type == "🏢 Flat / Builder Floor":
        flats_grouped = df_view.groupby("location").agg({
            'total_price' : 'mean',
            "price_sqft": "mean",
            "builtup_area": "mean",
            "lat": "first",
            "long_": "first"
            }).reset_index()
        
        flats_grouped.loc[13, 'lat'] = 26.9059311
        flats_grouped.loc[13, 'long_']= 75.7844383
        flats_grouped.loc[2, 'lat'] = 28.7939
        flats_grouped.loc[2, 'long_'] = 77.4083
        flats_grouped.loc[8, 'lat'] = 26.871458
        flats_grouped.loc[8, 'long_'] = 75.695869
        flats_grouped.loc[16, 'lat'] = 26.8850
        flats_grouped.loc[16, 'long_'] = 75.7800
        flats_grouped.loc[22, 'lat'] = 26.9657
        flats_grouped.loc[22, 'long_'] = 75.6865
        flats_grouped.loc[32, 'lat'] = 26.809721547924
        flats_grouped.loc[32, 'long_'] = 75.7612646242177
        flats_grouped.loc[33, 'lat'] = 26.9196
        flats_grouped.loc[33, 'long_'] = 75.7878
        flats_grouped.loc[34, 'lat'] = 26.7978684551392
        flats_grouped.loc[34, 'long_'] = 75.8816005745316
        flats_grouped.loc[38, 'lat'] = 26.9196
        flats_grouped.loc[38, 'long_'] = 75.7878
        flats_grouped.loc[75, 'lat'] = 26.712042627914137
        flats_grouped.loc[75, 'long_'] = 75.80349410503298
        flats_grouped.loc[74, 'lat'] = 26.9196
        flats_grouped.loc[74, 'long_'] = 75.7878
        flats_grouped.loc[72, 'lat'] = 26.165730
        flats_grouped.loc[72, 'long_'] = 75.795769
        flats_grouped.loc[71, 'lat'] = 26.8795
        flats_grouped.loc[71, 'long_'] = 75.7925
        flats_grouped.loc[69, 'lat'] = 26.8531901116199
        flats_grouped.loc[69, 'long_'] = 75.6297128203814
        flats_grouped.loc[63, 'lat'] = 26.9196
        flats_grouped.loc[63, 'long_'] = 75.7878
        flats_grouped.loc[46, 'lat'] = 26.823767
        flats_grouped.loc[46, 'long_'] = 75.740056
        flats_grouped.loc[9, 'lat'] = 26.871458
        flats_grouped.loc[9, 'long_'] = 75.695869
        flats_grouped.drop(24, inplace=True) 
        
        min = flats_grouped['price_sqft'].quantile(0.25)
        max = flats_grouped['price_sqft'].quantile(0.75)     
        
        flats_map = px.scatter_mapbox(flats_grouped, lat='lat', lon='long_', color = 'price_sqft', size='builtup_area',
                            color_continuous_scale = [(0, "blue"), (0.5, "orange"), (1, "red")] , zoom=10,
                            hover_name = 'location', hover_data={'price_sqft' : True, 'builtup_area' : True, 'lat': False, 'long_': False, 'location': False},
                            mapbox_style= "carto-positron" , text= 'location', range_color= [min,max], labels={"price_sqft": "Price per Sqft (₹)"})
        flats_map.update_layout(autosize= True, height= 700)
        st.plotly_chart(flats_map, use_container_width=True)

    elif property_type == "🏠 Independent House / Villa":
        df_grouped1 = df_view.groupby("location").agg({
            'total_price' : 'mean',
            "price_sqft": "mean",
            "builtup_area": "mean",
            "lat": "first",
            "long_": "first"
            }).reset_index()

        df_grouped1.loc[72, 'lat'] = 26.7958
        df_grouped1.loc[72, 'long_'] = 75.8621
        df_grouped1.loc[67, 'lat'] = 26.7728
        df_grouped1.loc[67, 'long_'] = 75.8621
        df_grouped1.loc[65, 'lat'] = 26.8038
        df_grouped1.loc[65, 'long_'] = 75.8272
        df_grouped1 = df_grouped1.drop(60)
        min = df_grouped1['price_sqft'].quantile(0.25)
        max = df_grouped1['price_sqft'].quantile(0.75)     
        # df_grouped1
        flats_map = px.scatter_mapbox(df_grouped1, lat='lat', lon='long_', color = 'price_sqft', size='builtup_area',
                            color_continuous_scale = [(0, "blue"), (0.5, "orange"), (1, "red")] , zoom=10,
                            hover_name = 'location', hover_data={'price_sqft' : True, 'builtup_area' : True,
                            'lat': False, 'long_': False, 'location': False}, mapbox_style= "carto-positron" ,
                            text= 'location', range_color= [min,max], labels={"price_sqft": "Price per Sqft (₹)"})
        flats_map.update_layout(autosize= True, height= 700)
        st.plotly_chart(flats_map)
    
    elif property_type == "🌍 Plot":
        df_grouped = df_view.groupby("property_location").agg({
            'total_price' : 'mean',
            "price(sqft)": "mean",
            "area_sqft": "mean",
            "lat": "first",
            "long_": "first"
            }).reset_index()

        min = df_grouped['price(sqft)'].quantile(0.25)
        max = df_grouped['price(sqft)'].quantile(0.75)    

        df_grouped.loc[53, 'lat'] = 26.8571
        df_grouped.loc[53, 'long_'] =  75.8127
        df_grouped.loc[34, 'lat'] =26.8353
        df_grouped.loc[34, 'long_'] =  75.8243

        df_grouped.loc[97, 'lat'] = 26.8752
        df_grouped.loc[97, 'long_'] =  75.7924

        df_grouped.loc[77, 'lat'] = 26.7728
        df_grouped.loc[77, 'long_'] =  75.8621

        df_grouped.loc[90, 'lat'] = 26.7728
        df_grouped.loc[90, 'long_'] =  75.8621
        # df_grouped.loc[98, 'lat'] = 26.8763
        # df_grouped.loc[98, 'long_'] =  75.798

        plot_map = px.scatter_mapbox(df_grouped, lat='lat', lon='long_', color = 'price(sqft)', size='area_sqft',
                            color_continuous_scale = [(0, "blue"), (0.5, "orange"), (1, "red")] , zoom=10,
                            hover_name = 'property_location', hover_data={'price(sqft)' : True, 'area_sqft' : True,
                            'lat': False, 'long_': False, 'property_location': False},
                            mapbox_style= "carto-positron" , text= 'property_location', range_color= [min,max], labels={"price(sqft)": "Price per Sqft (₹)"})
        plot_map.update_layout(autosize= True, height= 700)
        st.plotly_chart(plot_map)

        
def top10(property_type):
    if property_type == "🏢 Flat / Builder Floor" or property_type == "🏠 Independent House / Villa":
        if property_type == "🏢 Flat / Builder Floor":
            df_view1 = df_view.drop(df_view[df_view['price_sqft'] > 13500].index)
            df_view1 = df_view.drop(df_view[df_view['builtup_area'] > 4000].index )
            top_loc = df_view1.groupby('location_area')['price_L'].median().sort_values(ascending=False).head(10).reset_index()
            top_loc.columns = ['Location', 'Avg Price (L)']
            top_loc['Avg Price (L)'] = top_loc['Avg Price (L)'].round(1)
            x_col = "Avg Price (L)"
            title = "Top 10 — Most Expensive Locations (Lakhs)"
        
        elif property_type == "🏠 Independent House / Villa":
            df_view['price_Crore'] = df_view['total_price'] / 10000000
            df_view1 = df_view.drop(df_view[df_view['price_sqft'] > 30000].index)
            df_view1 = df_view.drop(df_view[df_view['builtup_area'] > 6000].index )
            top_loc = df_view1.groupby('location_area')['price_Crore'].median().sort_values(ascending=False).head(10).reset_index()
            top_loc.columns = ['Location', 'Avg Price (Crore)']
            top_loc['Avg Price (Crore)'] = top_loc['Avg Price (Crore)'].round(1)
            x_col = "Avg Price (Crore)"
            title = "Top 10 — Most Expensive Locations (Crore)"
        
        tdf = top_loc.sort_values(by = x_col)

        fig_top = px.bar(tdf, x=x_col, y='Location', orientation='h', color=x_col, color_continuous_scale='RdYlGn', title= title )
        fig_top.update_layout(height=400, showlegend=False, coloraxis_showscale=False, plot_bgcolor='white', paper_bgcolor='white',dragmode=False)
        st.plotly_chart(fig_top, use_container_width=True, key='top chart')
    
    
    elif property_type == "🌍 Plot":
        df_view['price_l'] = df_view['total_price'] / 100000
        top_loc = df_view.groupby('location_area')['price_l'].median().sort_values(ascending=False).head(10).reset_index()
        top_loc.columns = ['Location', 'Avg Price (Lakhs)']
        top_loc['Avg Price (Lakhs)'] = top_loc['Avg Price (Lakhs)'].round(1)
        x_col = "Avg Price (Lakhs)"
        title = "Top 10 — Most Expensive Locations (Lakhs)"

        tdf = top_loc.sort_values(by = x_col)

        fig_t = px.bar( tdf, x=x_col, y='Location', orientation='h', color=x_col, color_continuous_scale='RdYlGn',
            title= title )
        fig_t.update_layout(height=400, showlegend=False, coloraxis_showscale=False, plot_bgcolor='white', paper_bgcolor='white',dragmode=False)
        st.plotly_chart(fig_t, use_container_width=True, key='plot chart')
    

def least10(property_type):

    if property_type == "🏢 Flat / Builder Floor" or property_type == "🏠 Independent House / Villa":
        if property_type == "🏢 Flat / Builder Floor":
            df_view1 = df_view.drop(df_view[df_view['price_sqft'] > 13500].index)
            df_view1 = df_view.drop(df_view[df_view['builtup_area'] > 4000].index)
            bot_loc = df_view1.groupby('location_area')['price_L'].mean().sort_values().head(10).reset_index()
            bot_loc.columns = ['Location', 'Avg Price (Lakhs)']
            bot_loc['Avg Price (Lakhs)'] = bot_loc['Avg Price (Lakhs)'].round(1)
            x_col = "Avg Price (Lakhs)"
            title = "Top 10 — Most Affordable Locations (Lakhs)"
        
        elif property_type == "🏠 Independent House / Villa":
            df_view['price_Crore'] = df_view['total_price'] / 10000000
            df_view1 = df_view.drop(df_view[df_view['price_sqft'] > 30000].index)
            df_view1 = df_view.drop(df_view[df_view['builtup_area'] > 6000].index)
            bot_loc = df_view1.groupby('location_area')['price_Crore'].mean().sort_values().head(10).reset_index()
            bot_loc.columns = ['Location', 'Avg Price (Crore)']
            bot_loc['Avg Price (Crore)'] = bot_loc['Avg Price (Crore)'].round(1)
            x_col = "Avg Price (Crore)"
            title = "Top 10 — Most Affordable Locations (Crore)"
            
        tdf1 = bot_loc.sort_values(by=x_col, ascending=False)

        fig_bot = px.bar(tdf1, x=x_col, y='Location', orientation='h', color=x_col, color_continuous_scale='RdYlGn', title= title )
        fig_bot.update_layout(height=400, showlegend=False, coloraxis_showscale=False, plot_bgcolor='white', paper_bgcolor='white',dragmode=False)
        st.plotly_chart(fig_bot, use_container_width=True)
        
        
    elif property_type == "🌍 Plot":
        df_view['price_l'] = df_view['total_price'] / 100000
        bot_loc = df_view.groupby('location_area')['price_l'].mean().sort_values().head(10).reset_index()
        bot_loc.columns = ['Location', 'Avg Price (Lakhs)']
        bot_loc['Avg Price (Lakhs)'] = bot_loc['Avg Price (Lakhs)'].round(1)
        x_col = "Avg Price (Lakhs)"
        title = "Top 10 — Most Affordable Locations (Lakhs)"
                
        tdf1 = bot_loc.sort_values(by=x_col, ascending=False)

        fig_b = px.bar(tdf1, x=x_col, y='Location', orientation='h', color=x_col, color_continuous_scale='RdYlGn', title= title )
        fig_b.update_layout(height=400, showlegend=False, coloraxis_showscale=False, plot_bgcolor='white', paper_bgcolor='white',dragmode=False)
        st.plotly_chart(fig_b, use_container_width=True)
        

def areavsprice(property_type):
    if property_type == "🏢 Flat / Builder Floor" or property_type == "🏠 Independent House / Villa":
        if property_type == "🏢 Flat / Builder Floor":
            df_scatter = df_view[ (df_view['price_sqft'] <= 13500) & (df_view['builtup_area'] <= 4000)].copy()
        elif property_type == "🏠 Independent House / Villa":
            df_scatter = df_view[ (df_view['price_sqft'] <= 30000) & (df_view['builtup_area'] <= 6000)].copy()

        color_by = st.selectbox("Color by:", options=["bhk_display", "furnished_status", "location_area", "property_type"],
            format_func=lambda x: {
                "bhk_display":      "BHK",
                "furnished_status": "Furnished Status",
                "location_area":    "Location",
                "property_type":    "Property Type"
            }[x] )

        fig_scatter = px.scatter( df_scatter, x='builtup_area', y='price_sqft', color=color_by, hover_data=['price_L', 'location_area', 'bhk_display'],
            labels={ 'builtup_area': 'Built-up Area (sqft)',
                'price_sqft':   'Price per sqft (₹)',
                'price_L':      'Total Price (L)',
                'bhk_display':  'BHK' },
            opacity=0.7,color_continuous_scale='RdYlGn' )
        fig_scatter.update_layout(height=500, plot_bgcolor='white', paper_bgcolor='white', dragmode=False)
        st.plotly_chart(fig_scatter, use_container_width=True)
    
    elif property_type == "🌍 Plot":
        df_scatter = df_view[(df_view['area_sqft'] > 500) & (df_view['price(sqft)'] < 20000)].copy()
        df_scatter['price_L'] = df_scatter['total_price'] / 100000
        color_by = st.selectbox("Color by:", options=["location_area", "outside_view", 'face'],
            format_func=lambda x: {
                "location_area": "Location",
                "outside_view": "Outside View",
                "face":    "Plot Face", }[x] )
        
        plot_scatter = px.scatter(df_scatter, x='area_sqft', y='price(sqft)', color=color_by, hover_data=['price_L', 'location_area'],
            labels={ 'area_sqft': 'Plot Area (sqft)',
                'price(sqft)':   'Price per sqft (₹)',
                'price_L':      'Total Price (Lakhs)'},
            opacity=0.7,color_continuous_scale='RdYlGn' )
        plot_scatter.update_layout(height=500, plot_bgcolor='white', paper_bgcolor='white', dragmode=False)
        st.plotly_chart(plot_scatter, use_container_width=True)

def bhkdis(property_type):
    loc_options_pie = ["Overall"] + sorted(df_view['location_area'].unique().tolist())
    selected_loc_pie = st.selectbox("Select Location", loc_options_pie, key="pie_loc")

    if selected_loc_pie == "Overall":
        pie_data = df_view
    else:
        pie_data = df_view[df_view['location_area'] == selected_loc_pie]

    bhk_counts = pie_data['bhk_display'].value_counts().reset_index()
    bhk_counts.columns = ['BHK', 'Count']

    fig_pie = px.pie( bhk_counts, values='Count', names='BHK', color_discrete_sequence=px.colors.qualitative.Set2, hole=0.4 )
    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    fig_pie.update_layout(height=400, showlegend=True, plot_bgcolor='white', paper_bgcolor='white', dragmode=False)
    st.plotly_chart(fig_pie, use_container_width=True)

def price_range_bhk(property_type):
    if property_type == "🏢 Flat / Builder Floor":
        df_box = df_view[df_view['price_L'] <= 300]
        standard_bhk = ['1', '1.5', '2', '2.5', '3', '3.5', '4', '5']
        df_box = df_box[df_box['bhk_display'].isin(standard_bhk)]
        y_col = "price_L"
        y_label = "Price (Lakhs)"
    elif property_type == "🏠 Independent House / Villa":
        df_view['price_Crore'] = df_view['total_price'] / 10000000
        df_box = df_view[df_view['price_Crore'] <= 15] 
        standard_bhk = [1, 2, 2.5, 3, 3.5, 4, 5]
        df_box = df_box[df_box['bhk_display'].isin(standard_bhk)]
        y_col = "price_Crore"
        y_label = "Price (Crore)"
        
    fig_box = px.box(df_box, x='bhk_display', y= y_col, color='bhk_display', category_orders={"bhk_display": standard_bhk},
        labels={'bhk_display': 'BHK', y_col : y_label}, color_discrete_sequence=px.colors.qualitative.Set2)
    fig_box.update_layout(height=400, showlegend=False, plot_bgcolor='white', paper_bgcolor='white', dragmode=False)
    st.plotly_chart(fig_box, use_container_width=True)

def price_sqft_bhk(property_type):
    location_area = df_view['location_area'].unique().tolist()
    location_area.insert(0, "Overall")
    select_location = st.selectbox('Select Location Area', location_area)
    if property_type == "🏢 Flat / Builder Floor":
        standard_bhk = ['1', '1.5', '2', '2.5', '3', '3.5', '4', '5']
    elif property_type == "🏠 Independent House / Villa":
        standard_bhk = [1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6]
    if select_location == 'Overall': 
        df_sqft = df_view[df_view['bhk_display'].isin(standard_bhk)]
        sqft_by_bhk = df_sqft.groupby('bhk_display')['price_sqft'].mean().reset_index()
        sqft_by_bhk.columns = ['BHK', 'Avg Price/sqft']
        sqft_by_bhk['Avg Price/sqft'] = sqft_by_bhk['Avg Price/sqft'].round(0)
        sqft_by_bhk = sqft_by_bhk.set_index('BHK').reindex(
            [b for b in standard_bhk if b in sqft_by_bhk['BHK'].values]
        ).reset_index()
    else:
        df_view1 = df_view[df_view['location_area'] == select_location]
        df_sqft = df_view1[df_view1['bhk_display'].isin(standard_bhk)]
        sqft_by_bhk = df_sqft.groupby('bhk_display')['price_sqft'].mean().reset_index()
        sqft_by_bhk.columns = ['BHK', 'Avg Price/sqft']
        sqft_by_bhk['Avg Price/sqft'] = sqft_by_bhk['Avg Price/sqft'].round(0)
        sqft_by_bhk = sqft_by_bhk.set_index('BHK').reindex(
            [b for b in standard_bhk if b in sqft_by_bhk['BHK'].values]
        ).reset_index()
        
    fig_sqft = px.bar(sqft_by_bhk, x='BHK', y='Avg Price/sqft', color='Avg Price/sqft', color_continuous_scale='Blues',
                    text='Avg Price/sqft', labels={'Avg Price/sqft': 'Avg ₹/sqft'} )
    fig_sqft.update_traces(texttemplate='₹%{text:,.0f}', textposition='outside')
    fig_sqft.update_layout( height=400, showlegend=False, coloraxis_showscale=False, plot_bgcolor='white', paper_bgcolor='white', dragmode=False )
    st.plotly_chart(fig_sqft, use_container_width=True)

def typeanalysis(property_type):
    # df_view['price_lakhs_col'] = df_view['total_price'] / 100000
    if property_type == "🏢 Flat / Builder Floor":
        df_view['price_lakhs_col'] = df_view['total_price'] / 100000
        df_view['property_type']= df_view['property_type'].str.lower().str.strip()
        sideprice = plt.figure(figsize=(10,4))
        sns.distplot(df_view[df_view['property_type'] == 'builder floor']['price_lakhs_col'], label='Builder Floor')
        sns.distplot(df_view[df_view['property_type'] == 'flat']['price_lakhs_col'], label = 'Flat')
        plt.xlabel('Price (Lakhs)')
        plt.legend()
        st.pyplot(sideprice)
        
    elif property_type == "🏠 Independent House / Villa":
        df_view['price_Crore_col'] = df_view['total_price'] / 10000000
        df_view['property_type']= df_view['property_type'].str.lower().str.strip()
        sideprice = plt.figure(figsize=(10,4))
        sns.distplot(df_view[df_view['property_type'] == 'villa']['price_Crore_col'], label='villa')
        sns.distplot(df_view[df_view['property_type'] == 'house']['price_Crore_col'], label = 'house')
        plt.xlabel('Price (Cr.)')
        plt.legend()
        st.pyplot(sideprice)
        
def priceanalysis(property_type):
    if property_type == "🏢 Flat / Builder Floor" or "🌍 Plot" :
        df_view['price_lakhs_col'] = df_view['total_price'] / 100000
        y_col = 'price_lakhs_col'
        y_label = "Total Price (Lakhs)"
    elif property_type == "🏠 Independent House / Villa":
        df_view['price_Crore_col'] = df_view['total_price'] / 10000000
        y_col = 'price_Crore_col'
        y_label = "Total Price (Crore)"
        
    location_area = df_view['location_area'].unique().tolist()
    col1, col2 = st.columns(2)
    with col1:
        select_location1 = st.selectbox('Select Location Area', location_area, key='location1')
    with col2:
        select_location2 = st.selectbox('Select Location Area', location_area, key='location2')
        
    fig_price = px.box( df_view[df_view['location_area'].isin([select_location1, select_location2])],
        x='location_area', y=y_col, color='location_area',
        title="Property Price Distribution across Locations", color_discrete_sequence=px.colors.qualitative.Set2)
    fig_price.update_layout(yaxis_title=y_label, xaxis_title='Location Area')
    st.plotly_chart(fig_price)

def parkingimpact(property_type):
    df_park = df_view.copy()
    df_park['covered_parking'] = df_park['covered_parking'].fillna(0).astype(int)
    df_park = df_park[df_park['covered_parking'] <= 3]

    park_avg = df_park.groupby('covered_parking')['price_L'].mean().reset_index()
    park_avg.columns = ['Covered Parking', 'Avg Price (L)']
    park_avg['Avg Price (L)'] = park_avg['Avg Price (L)'].round(1)
    park_avg['Covered Parking'] = park_avg['Covered Parking'].astype(str)

    fig_park = px.bar(park_avg, x='Covered Parking', y='Avg Price (L)', color='Avg Price (L)',
            text='Avg Price (L)', color_continuous_scale='Blues', title="Avg Price vs Covered Parking",
            labels={'Covered Parking': 'No. of Covered Parking'} )
    fig_park.update_traces(texttemplate='₹%{text}L', textposition='outside')
    fig_park.update_layout(height=350, showlegend=False, coloraxis_showscale=False,
            plot_bgcolor='white', paper_bgcolor='white', dragmode=False)   
    st.plotly_chart(fig_park, use_container_width=True)

def pooja_room(property_type):
    df_park2 = df_view.copy()
    df_park2['pooja_room_label'] = df_park2['pooja_room'].map({0: 'No Pooja Room', 1: 'Has Pooja Room'})

    pooja_avg = df_park2.groupby('pooja_room_label')['price_L'].mean().reset_index()
    pooja_avg.columns = ['Pooja Room', 'Avg Price (L)']
    pooja_avg['Avg Price (L)'] = pooja_avg['Avg Price (L)'].round(1)

    fig_pooja = px.bar(pooja_avg, x='Pooja Room', y='Avg Price (L)', color='Pooja Room',
                text='Avg Price (L)', color_discrete_sequence=['#e07b39', '#1D9E75'], title="Pooja Room Impact on Price")
    fig_pooja.update_traces(texttemplate='₹%{text}L', textposition='outside')
    fig_pooja.update_layout(height=350, showlegend=False, plot_bgcolor='white', paper_bgcolor='white', dragmode=False)
    st.plotly_chart(fig_pooja, use_container_width=True)



st.markdown("---")

if property_type == "🏢 Flat / Builder Floor" or property_type == "🏠 Independent House / Villa":
    st.markdown('<div class="section-title">🗺️ Location Price Geomap</div>', unsafe_allow_html=True)
    # #  ---------plot map ---------------
    plot_map(property_type)
                
    # 2. TOP 10 LOCATIONS BY AVG PRICE
    st.markdown('<div class="section-title">🏆 Top Locations by Average Price</div>', unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    with col_a:
        top10(property_type)
    with col_b:
        least10(property_type)


    # 3. AREA VS PRICE SCATTER
    st.markdown('<div class="section-title">📐 Area vs Price</div>', unsafe_allow_html=True)
    areavsprice(property_type)


    # 4. BHK ANALYSIS
    st.markdown('<div class="section-title">🛏 BHK Analysis</div>', unsafe_allow_html=True)
    st.markdown("##### BHK Distribution")
    bhkdis(property_type)


    st.markdown("##### Price Range by BHK")
    price_range_bhk(property_type)


    # 5. PRICE PER SQFT BY BHK
    st.markdown('<div class="section-title">💰 Price per sqft by BHK</div>', unsafe_allow_html=True)
    price_sqft_bhk(property_type)


    #  Price by distribution
    st.markdown('<div class="section-title">🏢 Price Analysis by Location</div>', unsafe_allow_html=True)
        
    priceanalysis(property_type)

    # 8. PARKING IMPACT

    st.markdown('<div class="section-title">🚗 Parking Impact on Price</div>', unsafe_allow_html=True)

    col7, col8 = st.columns(2)

    with col7:
        parkingimpact(property_type)

    with col8:
        pooja_room(property_type)


     #  PROPERTY TYPE DISTRIBUTION

    st.markdown('<div class="section-title">🏢 Property Type Analysis</div>', unsafe_allow_html=True)
    typeanalysis(property_type)

elif property_type == "🌍 Plot":
    st.markdown('<div class="section-title">🗺️ Location Price Geomap</div>', unsafe_allow_html=True)
    # #  ---------plot map ---------------
    plot_map(property_type)
    
    # 2. TOP 10 LOCATIONS BY AVG PRICE
    st.markdown('<div class="section-title">🏆 Top Locations by Average Price</div>', unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    with col_a:
        top10(property_type)
    with col_b:
        least10(property_type)
        
    # 3. AREA VS PRICE SCATTER
    st.markdown('<div class="section-title">📐 Area vs Price</div>', unsafe_allow_html=True)
    areavsprice(property_type)
    
    #  Price by distribution
    st.markdown('<div class="section-title">🏢 Price Analysis by Location</div>', unsafe_allow_html=True) 
    priceanalysis(property_type)

st.markdown("---")
st.markdown("""
<p style='text-align:center;color:#aaa;font-size:0.85rem;'>
    Jaipur Real Estate Analytics Dashboard • Data: SquareYards
</p>
""", unsafe_allow_html=True)
