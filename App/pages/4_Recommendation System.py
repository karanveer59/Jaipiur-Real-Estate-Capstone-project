# Jai Hanuman 🙏🙏🙏🙏🙏

import streamlit as st
import pickle
import pandas as pd
import numpy as np
import sklearn
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler


st.set_page_config(layout="wide")

# ------------ import file data-----------------------
# with open("G:/My Drive/Data Science/Projects/CapStone Project Final Sem BCA/pickle files/flats_recommendation_bundle.pkl",'rb') as flats_file:
#     flats_bundle = pickle.load(flats_file)

flats_df = pd.read_csv('App/data/flats_recommendation.csv')
house_df = pd.read_csv('App/data/independent_house_recommendation.csv')
plot_df = pd.read_csv('App/data/plot_recommendation.csv')

class recommendation_system:
    def __init__(self, property_type):
        self.property_type = property_type
    
    def Property_Type(self):
        if self.property_type == '🏢 Flat / Builder Floor':
            return (st.selectbox("🏠 Property Type", ['Flat', "Builder Floor"])).lower()
        
        elif self.property_type == "🏠 Independent House / Villa":
            return (st.selectbox("🏠 Property Type", ['House', 'Villa'])).lower()
    
    def Location(self):
        if self.property_type == '🏢 Flat / Builder Floor':
            priority_location = ['Pratap Nagar', 'Central Jaipur', 'Other']
            rest_location = ['Ajmer road', 'Pratap Nagar', 'Mansarovar', 'Jagatpura',
                'Dholai', 'Ramnagariya', 'Vaishali Nagar', 'Gandhi path',
                'Patrakar Colony', 'Girdharipura', 'Gokulpura',
                'Sanganer', 'Sirsi road', 'Anand Nagar', 'Shri Kishanpura',
                'Jeerota', 'Muhana', 'Jhotwara', 'Nirman Nagar', 'Bhakrota',
                'Sodala', 'Gurjar Ki Thadi', 'Civil Lines', 'Shyam Nagar',
                'Bhapura']
            
            rest_location = sorted(rest_location)
            location_area = priority_location + rest_location
            
            return (st.selectbox('Location', location_area)).lower()

        elif self.property_type == "🏠 Independent House / Villa":
            priority_location = ['Pratap Nagar', 'Central Jaipur','Other']
            rest_location = ['Gokulpura', 'Nirman Nagar',
                'Jhotwara', 'Muralipura', 'Sanganer', 'Mansarovar', 'Jagatpura',
                'Hanuman Nagar', 'Vaishali Nagar', 'Agra road', 'Sirsi road',
                'Ajmer road', 'Kalwar road', 'Kishorpura', 'Govindpura',
                'Chitrakoot', 'Sodala', 'Gandhi Path', 'Dhawas', 'Shri Kishanpura']
            
            rest_location = sorted(rest_location)
            location_area = priority_location + rest_location
            
            return (st.selectbox('Location', location_area)).lower()

        elif self.property_type == '🌍Plot':
            priority_location = ['Central Jaipur','Other']
            rest_location = ['Bhapura', 'Jagatpura', 'Ajmer road','Pratap Nagar',
                'Kishorpura', 'Neota', 'Kalwara', 'Mansarovar',
                'Sirsi road', 'Shivdaspura', 'Tonk Road', 'Diggi Road', 'Sanganer',
                'Delhi Jaipur Expressway', 'Renwal Manji', 'Vatika/Vatika Road',
                'Kalwar Road', 'Jaisinghpura', 'Bhakrota',
                'Mahaveer Nagar', 'Hardhyanpura', 'Vaishali Nagar', 'Sikar Road',
                'Sitapura', 'Phagi Road', 'Khatipura', 'Agra Road', 'Gandhi Path',
                'Mohanpura', 'Jhai', 'Sodala', 'Ramchandpura']
            rest_location = sorted(rest_location)
            location_area = priority_location + rest_location
            
            return (st.selectbox('Location', location_area)).lower()

    def BHK(self):
        if self.property_type == '🏢 Flat / Builder Floor':
            return (st.select_slider('🛏 BHK',[1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0]))
        elif self.property_type == "🏠 Independent House / Villa":
            return float(st.select_slider('🛏 BHK',sorted(house_df['bhk'].unique().tolist())))
    
    def Bath(self):
        if self.property_type == '🏢 Flat / Builder Floor':
            return float(st.select_slider('🚿 Bathrooms',sorted(flats_df['bath'].unique().tolist())))
        elif self.property_type == "🏠 Independent House / Villa":
            return float(st.select_slider('🚿 Bathrooms',sorted(house_df['bath'].unique().tolist())))
    
    def BuiltupArea(self):
        if self.property_type in ['🏢 Flat / Builder Floor', "🏠 Independent House / Villa"]:
            return float(st.number_input("📐 Built-up Area (sqft)", min_value = 50, value=1200))
        elif self.property_type == '🌍Plot':
            return float(st.number_input("📐 Plot Area (sqft)", min_value = 50, value=1000))
    
    def TotalPrice(self):
        unit = st.radio("Select Unit", ["Lakhs", "Crores"], horizontal=True)

        if unit == "Lakhs":
            amount = st.number_input("💰 Budget (in Lakhs)", min_value=1, max_value=1000, value=50)
            total_price = amount * 100000
            
        else:
            amount = st.number_input("💰 Budget (in Crores)", min_value=1, max_value=100, value=2)
            total_price = amount * 10000000

        st.write("Final Budget in ₹:", total_price)
        return total_price

    def OutsideView(self):
        if self.property_type == '🌍Plot':
            return st.selectbox('Outside View',(plot_df['outside_view'].unique().tolist()))


class InputForm:
    def __init__(self, property_type):
        self.property_type = property_type
        self.rs = recommendation_system(property_type)
        self.property_type1 = None
        self.location_area = None
        self.builtup_area = None
        self.bhk = None
        self.bath = None
        self.total_price = None
        self.outside_view = None
        
    def row_one(self):
        if self.property_type in ['🏢 Flat / Builder Floor', "🏠 Independent House / Villa"]:
            col1, col2, col3 = st.columns(3)
            with col1:
                # Property_type
                self.property_type1 = self.rs.Property_Type()
            with col2:
                #location_area
                self.location_area = self.rs.Location()   
            with col3:
                # Built up area
                self.builtup_area = self.rs.BuiltupArea()
                
        elif self.property_type == '🌍Plot':
            col1, col2, col3 = st.columns(3)
            with col1:
                #location_area
                self.location_area = self.rs.Location() 
            with col2:
                #Built up area
                self.builtup_area = self.rs.BuiltupArea()
            with col3:
                self.outside_view = self.rs.OutsideView()
    
    def second_row(self):
        if self.property_type in ['🏢 Flat / Builder Floor', "🏠 Independent House / Villa"]:
            col21, col22, col23 = st.columns(3)
            with col21:
                # BHK
                self.bhk = self.rs.BHK()
            with col22:
                # Bathroom
                self.bath = self.rs.Bath()
            with col23:
                # furnished_status
                self.total_price = self.rs.TotalPrice()
                
        elif self.property_type == '🌍Plot':
            col1, col2, col3 = st.columns(3)
            with col1:
                #location_area
                st.markdown("") 
            with col2:
                #Built up area
                self.total_price = self.rs.TotalPrice()
            with col3:
                st.markdown("")
             
                
    # ------------------------ Flats Reccomendation data----------------------
    def flats_and_house_similarity(self, location, total_price, builtup_area, bhk, bath, property_type_en):
        weights = np.array([
            1.0,  # total_price
            1.5,  # builtup_area
            3.0,  # bhk       ← zyada important dete hai isko
            1.0,  # bath
            1.0,  # property_type_enc
            ])
        if self.property_type == '🏢 Flat / Builder Floor':
            filtered_df = flats_df[(flats_df['location_area'] == location)]
        elif self.property_type == "🏠 Independent House / Villa":
            filtered_df = house_df[(flats_df['location_area'] == location)]

        features = filtered_df[['property_type','total_price','builtup_area','bhk','bath']]

        le_property = LabelEncoder()
        features['property_type_en'] = le_property.fit_transform(features['property_type'])
        
        num_cols = ['total_price','builtup_area','bhk','bath','property_type_en']

   
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(features[num_cols])

        user_inputs = [[total_price, builtup_area, bhk, bath, le_property.transform([property_type_en])[0]]]
        user_scaled = scaler.transform(user_inputs)

        user_weighted = user_scaled * weights
        data_weighted = scaled_data * weights
        
        user_score = cosine_similarity(user_weighted, data_weighted)[0]
        
        top_idx = user_score.argsort()[::-1]
        if top_idx.shape[0] >= 5:
            return filtered_df.iloc[top_idx][:5]
        else:
            return filtered_df.iloc[top_idx]
        
    def plot_similarity(self, location, total_price, builtup_area, outside_view_en):
        weights = np.array([
            1.0,  # total_price
            1.5,  # builtup_area
            1.0,  # outside_view_enc
            ])

        filtered_df = plot_df[(plot_df['location_area'] == location)]

        features = filtered_df[['total_price','area_sqft','outside_view']]

        le_property = LabelEncoder()
        features['outside_view_en'] = le_property.fit_transform(features['outside_view'])
        
        num_cols = ['total_price','area_sqft','outside_view_en']
   
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(features[num_cols])

        user_inputs = [[total_price, builtup_area, le_property.transform([outside_view_en])[0]]]
        user_scaled = scaler.transform(user_inputs)

        user_weighted = user_scaled * weights
        data_weighted = scaled_data * weights
        
        user_score = cosine_similarity(user_weighted, data_weighted)[0]
        
        top_idx = user_score.argsort()[::-1]
        if top_idx.shape[0] >= 5:
            return filtered_df.iloc[top_idx][:5]
        else:
            return filtered_df.iloc[top_idx]

    def predict(self):
        if self.property_type in ['🏢 Flat / Builder Floor', "🏠 Independent House / Villa"]:
            st.subheader('📊 Recommended Properties')

            new_df = self.flats_and_house_similarity(location=self.location_area, bhk=self.bhk, bath=self.bath, builtup_area=self.builtup_area, total_price=self.total_price, property_type_en=self.property_type1)
            # st.dataframe(new_df)
            
            for rank, (i, row) in enumerate(new_df.iterrows(), 1):   #target="_self"
                
                price_fmt = (
                    f"₹ {int(row['total_price'])/10000000:.2f} Cr." if int(row['total_price']) >= 10000000
                    else f"₹ {int(row['total_price'])/100000:.2f} L" )
                
                bhk_fmt = "Studio" if row['bhk'] == 0 else f"{row['bhk']} BHK"
                st.markdown(f"""
                <a href="{row['property_link']}" target="_blank" style="text-decoration:none;">
                <div style="
                    background: white; border-radius: 14px; padding: 20px 24px;
                    margin-bottom: 12px; border: 1px solid #e8e4dc; border-left: 5px solid #e07b39;
                    transition: box-shadow 0.2s;
                ">
                    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
                        <div style="font-size:1rem;font-weight:700;color:#1a1a2e;">
                            🏠 {row['property_type'].title()} — {bhk_fmt}
                        </div>
                        <div style="background:#fff3ec;color:#c45e20;font-weight:700;
                                    padding:4px 14px;border-radius:20px;font-size:0.9rem;
                                    border:1px solid #f0c4a8;">
                            #{rank} Match
                        </div>
                    </div>
                    <div style="color:#555;font-size:0.9rem;margin-bottom:10px;">
                        📍 {row['location'].title()} — {row['location_area'].title()}
                    </div>
                    <div style="display:flex;gap:10px;flex-wrap:wrap;">
                        <span style="background:#f7f5f0;border:1px solid #e8e4dc;
                                     border-radius:8px;padding:4px 12px;font-size:0.82rem;color:#444;">
                            🛏 {bhk_fmt}
                        </span>
                        <span style="background:#f7f5f0;border:1px solid #e8e4dc;
                                     border-radius:8px;padding:4px 12px;font-size:0.82rem;color:#444;">
                            🚿 {row['bath']} Bath
                        </span>
                        <span style="background:#f7f5f0;border:1px solid #e8e4dc;
                                     border-radius:8px;padding:4px 12px;font-size:0.82rem;color:#444;">
                            📐 {row['builtup_area']} sqft
                        </span>
                        <span style="background:#fff3ec;border:1px solid #f0c4a8;
                                     border-radius:8px;padding:4px 12px;font-size:0.82rem;
                                     color:#c45e20;font-weight:600;">
                            💰 {price_fmt}
                        </span>
                    </div>
                    <div style="margin-top:10px;font-size:0.8rem;color:#aaa;">
                        🔗 Click to view property details
                    </div>
                </div>
                </a>
                """, unsafe_allow_html=True)
            
            
        elif self.property_type == '🌍Plot':
            st.subheader('📊 Recommended Properties')
            new_df = self.plot_similarity(location=self.location_area, builtup_area=self.builtup_area, total_price=self.total_price, outside_view_en=self.outside_view)
            # st.dataframe(new_df)
            
            for rank, (i, row) in enumerate(new_df.iterrows(), 1):
                price_fmt = (
                    f"₹ {int(row['total_price'])/10000000:.2f} Cr." if int(row['total_price']) >= 10000000
                    else f"₹ {int(row['total_price'])/100000:.2f} L" )
                st.markdown(f"""
                <a href="{row['property_link']}" target="_blank" style="text-decoration:none;">
                <div style=" background: white; border-radius: 14px; padding: 20px 24px;
                    margin-bottom: 12px; border: 1px solid #e8e4dc; border-left: 5px solid #1D9E75;
                    ">
                    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
                        <div style="font-size:1rem;font-weight:700;color:#1a1a2e;">
                            🌍 Plot
                        </div>
                        <div style="background:#e1f5ee;color:#0F6E56;font-weight:700;
                                    padding:4px 14px;border-radius:20px;font-size:0.9rem;
                                    border:1px solid #9FE1CB;">
                            #{rank} Match
                        </div>
                    </div>
                    <div style="color:#555;font-size:0.9rem;margin-bottom:10px;">
                        📍 {row['property_location'].title()} — {row['location_area'].title()}
                    </div>
                    <div style="display:flex;gap:10px;flex-wrap:wrap;">
                        <span style="background:#f7f5f0;border:1px solid #e8e4dc;
                                     border-radius:8px;padding:4px 12px;font-size:0.82rem;color:#444;">
                            📐 {row['area_sqft']} sqft
                        </span>
                        <span style="background:#f7f5f0;border:1px solid #e8e4dc;
                                     border-radius:8px;padding:4px 12px;font-size:0.82rem;color:#444;">
                            🏞️ {row['outside_view'].title()}
                        </span>
                        <span style="background:#e1f5ee;border:1px solid #9FE1CB;
                                     border-radius:8px;padding:4px 12px;font-size:0.82rem;
                                     color:#0F6E56;font-weight:600;">
                            💰 {price_fmt}
                        </span>
                    </div>
                    <div style="margin-top:10px;font-size:0.8rem;color:#aaa;">
                        🔗 Click to view property details
                    </div>
                </div>
                </a>
                """, unsafe_allow_html=True)

    def generate_insights(old, new, original_price, new_price):

        insights = []

        diff = new_price - original_price
        percent = (diff / original_price) * 100

        # overall
        if percent > 0:
            insights.append(f"📈 Price increased by {percent:.2f}%")
        else:
            insights.append(f"📉 Price decreased by {abs(percent):.2f}%")

        # -------- BHK --------
        if old['bhk'] != new['bhk']:
            if new['builtup_area'] == old['builtup_area']:
                insights.append("⚠️ BHK increased but area same → space reduced")
                insights.append("💡 Increase area by 250–300 sqft")

        # -------- BATH --------
        if old['bath'] != new['bath']:
            insights.append("🚿 Bathrooms affect usability")
            insights.append("💡 Add 40–60 sqft for proper spacing")

        # -------- AREA --------
        if old['builtup_area'] != new['builtup_area']:
            insights.append("📏 Area directly impacts price")

        # -------- PARKING --------
        if old['covered_parking'] != new['covered_parking']:
            insights.append("🚗 Covered parking adds premium value")

        if old['open_parking'] != new['open_parking']:
            insights.append("🚘 Open parking slightly increases value")

        # -------- POOJA --------
        if old['pooja_room'] != new['pooja_room']:
            insights.append("🛕 Pooja room adds comfort")
            insights.append("💡 Add 30–50 sqft")

        # -------- EXTRA --------
        if old['extra_rooms'] != new['extra_rooms']:
            insights.append("🧑‍🔧 Extra room increases functionality")
            insights.append("💡 Add 100–130 sqft")

        # -------- LOCATION --------
        if old['location_area'] != new['location_area']:
            insights.append("📍 Location changed")
            if percent > 0:
                insights.append("💡 New location is more expensive")
            else:
                insights.append("💡 New location is more affordable")

        return insights 




# ------------- built interface ------------------
st.markdown("""<h1 style='text-align:center;'>🏠 Smart Recommendation System</h1>""", unsafe_allow_html=True)
st.markdown("---")

st.subheader('Please Select Property Type')
st.markdown("""
<style>
div[role="radiogroup"] > label {
    transition: 0.3s;
    padding: 20px;
    border-radius: 8px;
}
div[role="radiogroup"] > label:hover {
    background-color: #f0f0f0;
    transform: scale(1.05);
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)
property_type = st.radio("",
    options=["🏢 Flat / Builder Floor", "🏠 Independent House / Villa", "🌍Plot"],
    horizontal=True
)
st.markdown("---")

st.subheader('📝 Please Enter Property Details')
    
input = InputForm(property_type)
      
# ------------Flats / Builder Floor --------------------
if property_type in ['🏢 Flat / Builder Floor', "🏠 Independent House / Villa"]:
    # ------------Input------------------       

    # ---------------First row columns ---------------
    input.row_one()
    st.subheader("")
    
    #---------------Second row columns-------------- 
    input.second_row()
    st.subheader("")
elif property_type == '🌍Plot':
    # st.subheader('📝 Please Enter Property Details')
    # ---------------First row columns ---------------
    input.row_one()
    st.subheader("")
    
    #---------------Second row columns-------------- 
    input.second_row()
    st.subheader("")
    
    
if property_type == '🏢 Flat / Builder Floor':
    recommend_btn = st.button(f'🚀 Get Recommendations 🏢 {(input.property_type1).capitalize()} Price')
elif property_type == '🏠 Independent House / Villa':
    recommend_btn = st.button(f'🚀 Get Recommendations 🏠 {(input.property_type1).capitalize()} Price')
elif property_type == '🌍Plot':
    recommend_btn = st.button(f'🚀 Get Recommendations')
    
if recommend_btn:
    input.predict()

st.markdown('---')
    
st.markdown("""
<style>
div.stButton > button {
    width: 100%;
    height: 50px;
    font-size: 18px;
    border-radius: 10px;
    background-color: white;
    color: black;
}
</style>
""", unsafe_allow_html=True)



