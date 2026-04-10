# Jai Hanuman 🙏🙏🙏🙏🙏

import streamlit as st
import pickle
import pandas as pd
import numpy as np
import sklearn

# st.set_page_config(page_title='Price_prediction',layout='wide')

st.set_page_config(layout='wide')
# ---------------import flats data------------------
with open('App/data/flats_x_df.pkl', 'rb') as file:
    flats_df = pickle.load(file)
    
with open('App/data/flats_pipeline.pkl', 'rb') as file1:
    flats_pipeline = pickle.load(file1)
    
# --------------import independent house data ---------------------

with open('App/data/independent_house_x_df.pkl', 'rb') as ifile:
    house_df = pickle.load(ifile)

with open('App/data/independent_house_pipeline.pkl', 'rb') as ifile1:
    house_pipeline = pickle.load(ifile1)
    
# --------------import Plot data
with open('App/data/plot_x_df.pkl','rb') as pfile:
    plot_df = pickle.load(pfile)

with open('App/data/plot_pipeline.pkl','rb') as pfile1:
    plot_pipeline = pickle.load(pfile1)

    
# ----------------- Price Prediction Class --------------------
class price_predict:
    def __init__(self, property_type):
        self.property_type = property_type
    
    def PropertyType(self):
        if self.property_type == '🏢 Flat / Builder Floor':
            return (st.selectbox("🏠 Property Type", ['Flat', "Builder Floor"])).lower()
        
        elif self.property_type == "🏠 Independent House / Villa":
            return (st.selectbox("🏠 Property Type", ['House', 'Villa'])).lower()
        
    def Location(self):
        if self.property_type == '🏢 Flat / Builder Floor':
            flats_df['location_area'].unique()
            priority_location = ['Central Jaipur']
            rest_location = ['Ajmer road', 'Pratap Nagar', 'Mansarovar', 'Jagatpura',
                'Dholai', 'Ramnagariya', 'Vaishali Nagar', 'Gandhi path',
                'Patrakar Colony', 'Girdharipura', 'Gokulpura',
                'Sanganer', 'Sirsi road', 'Anand Nagar', 'Shri Kishanpura',
                'Jeerota', 'Muhana', 'Jhotwara', 'Nirman Nagar', 'Bhakrota',
                'Sodala', 'Gurjar Ki Thadi', 'Civil Lines', 'Shyam Nagar',
                'Bhapura']
            rest_location = sorted(rest_location)
            location_area = priority_location + rest_location + ['Other']
            
            return (st.selectbox('Location', location_area)).lower()

        elif self.property_type == "🏠 Independent House / Villa":
            priority_location = ['Central Jaipur']
            rest_location = ['Gokulpura', 'Nirman Nagar','Pratap Nagar', 
                'Jhotwara', 'Muralipura', 'Sanganer', 'Mansarovar', 'Jagatpura',
                'Hanuman Nagar', 'Vaishali Nagar', 'Agra road', 'Sirsi road',
                'Ajmer road', 'Kalwar road', 'Kishorpura', 'Govindpura',
                'Chitrakoot', 'Sodala', 'Gandhi Path', 'Dhawas', 'Shri Kishanpura']
            rest_location = sorted(rest_location)
            location_area = priority_location + rest_location + ['Other']
            
            return (st.selectbox('Location', location_area)).lower()

        elif self.property_type == '🌍Plot':
            priority_location = ['Pratap Nagar', 'Other']
            rest_location = ['Bhapura', 'Jagatpura', 'Ajmer road', 'Central Jaipur',
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
        
    def BuiltupArea(self):
        if self.property_type in ['🏢 Flat / Builder Floor', "🏠 Independent House / Villa"]:
            return float(st.number_input("📐 Built-up Area (sqft)", min_value = 50, value=1000))
        elif self.property_type == '🌍Plot':
            return float(st.number_input("📐 Plot Area (sqft)", min_value = 50, value=1000))
        
    def BHK(self):
        if self.property_type == '🏢 Flat / Builder Floor':
            return (st.select_slider('🛏 BHK',[1.0, 2.0, 3.0, 4.0 ,5.0]))
        elif self.property_type == "🏠 Independent House / Villa":
            return float(st.select_slider('🛏 BHK',[1.0, 2.0, 3.0,  4.0 ,5.0]))
    
    def Bath(self):
        if self.property_type == '🏢 Flat / Builder Floor':
            return float(st.select_slider('🚿 Bathrooms',sorted(flats_df['bath'].unique().tolist())))
        elif self.property_type == "🏠 Independent House / Villa":
            return float(st.select_slider('🚿 Bathrooms',sorted(flats_df['bath'].unique().tolist())))
    
    def FurnishedStatus(self):
        if self.property_type == '🏢 Flat / Builder Floor':
            user_choice = st.selectbox(
                '🪑 Furnished Status',
                ["Unfurnished", "Semi-furnished", "Furnished"]
                )

            mapping = {
                "Unfurnished": "semifurnished",
                "Semi-furnished": "unfurnished",
                "Furnished": "furnished"
                }

            return mapping[user_choice]
            # return (st.selectbox('🪑 Furnished Status', ["UnFurnished", "SemiFurnished", "Furnished"])).lower()
        elif self.property_type == "🏠 Independent House / Villa":
                user_choice = st.selectbox(
                    '🪑 Furnished Status',
                    ["Unfurnished", "Semi-furnished", "Furnished"]
                    )

                mapping = {
                    "Unfurnished": "furnished",
                    "Semi-furnished": "unfurnished",
                    "Furnished":  "semifurnished"
                    }
                
                return mapping[user_choice]
#                 return (st.selectbox('🪑 Furnished Status', ["UnFurnished", "SemiFurnished", "Furnished"])).lower()
        
    def CoveredParking(self):
        if self.property_type == '🏢 Flat / Builder Floor':
            return float(st.slider("🚗 Covered Parking", 0, 2, 0))
        elif self.property_type == "🏠 Independent House / Villa":
            return float(st.slider("🚗 Covered Parking", 0, 5, 0))
    
    def OpenParking(self):
        if self.property_type == '🏢 Flat / Builder Floor':
            return float(st.slider("🅿 Open Parking", 0, 2, 0))
        elif self.property_type == "🏠 Independent House / Villa":
            return float(st.slider("🚗 Open Parking", 0, 6, 0))
    
    def PoojaRoom(self):
        if self.property_type in ['🏢 Flat / Builder Floor', "🏠 Independent House / Villa"]:
            return float(st.selectbox("🙏 Pooja Room", [0, 1]))
    
    def ServantRoom(self):
        if self.property_type in ['🏢 Flat / Builder Floor', "🏠 Independent House / Villa"]:
            return float(st.selectbox('Servant Room', [0, 1]))
    
    def ExtraRooms(self):
        if self.property_type in ['🏢 Flat / Builder Floor', "🏠 Independent House / Villa"]:
            return float(st.selectbox('Extra Room', [0, 1, 2, 3]))    
    
    def Face(self):
        if self.property_type == '🌍Plot':
            return st.selectbox('Plot Face',sorted(plot_df['face'].unique().tolist()))
    
    def OutsideView(self):
        if self.property_type == '🌍Plot':
            return st.selectbox('Outside View',sorted(plot_df['outside_view'].unique().tolist()))
    

class InputForm:
    def __init__(self, property_type):
        self.property_type = property_type
        self.pp = price_predict(property_type)
        self.property_type1 = None
        self.location_area = None
        self.builtup_area = None
        self.bhk = None
        self.bath = None
        self.furnished_status = None
        self.covered_parking = None
        self.open_parking = None
        self.pooja_room = None
        self.servant_room = None
        self.extra_rooms = None
        self.face = None
        self.outside_view = None
        
    def row_one(self):
        if self.property_type in ['🏢 Flat / Builder Floor', "🏠 Independent House / Villa"]:
            col1, col2, col3 = st.columns(3)
            with col1:
                # Property_type
                self.property_type1 = self.pp.PropertyType()
            with col2:
                #location_area
                self.location_area = self.pp.Location()   
            with col3:
                # Built up area
                self.builtup_area = self.pp.BuiltupArea()
        
        elif self.property_type == '🌍Plot':
            col1, col2, col3 = st.columns(3)
            with col1:
                #location_area
                self.location_area = self.pp.Location() 
            with col2:
                #Built up area
                self.builtup_area = self.pp.BuiltupArea()
            with col3:
                self.outside_view = self.pp.OutsideView()

            
    def second_row(self):
        if self.property_type in ['🏢 Flat / Builder Floor', "🏠 Independent House / Villa"]:
            col21, col22, col23 = st.columns(3)
            with col21:
                # BHK
                self.bhk = self.pp.BHK()
            with col22:
                # Bathroom
                self.bath = self.pp.Bath()
            with col23:
                # furnished_status
                self.furnished_status = self.pp.FurnishedStatus()

        elif self.property_type == '🌍Plot':
            col1, col2, col3 = st.columns(3)
            with col1:
                #location_area
                st.markdown("") 
            with col2:
                #Built up area
                self.face = self.pp.Face()
            with col3:
                st.markdown("")
            
    def third_row(self):
        if self.property_type in ['🏢 Flat / Builder Floor', "🏠 Independent House / Villa"]:
            col31, col32, col33 = st.columns(3)
            with col31:
                # covered parking
                self.covered_parking = self.pp.CoveredParking()
            with col32:
                # open parking
                self.open_parking = self.pp.OpenParking()
      
    def fourth_row(self):
        if self.property_type in ['🏢 Flat / Builder Floor', "🏠 Independent House / Villa"]:
            col41, col42, col43 = st.columns(3)
            with col41:
                # Pooja Room
                self.pooja_room = self.pp.PoojaRoom() 
            with col42:
                # servant room
                self.servant_room = self.pp.ServantRoom()
            with col43:
                # Extra rooms
                self.extra_rooms = self.pp.ExtraRooms()
    
    def predict(self):
        if self.property_type in ['🏢 Flat / Builder Floor', "🏠 Independent House / Villa"]:
            st.subheader('📊 Prediction Result')  
            input_df = pd.DataFrame({
                'property_type': [self.property_type1],
                'location_area': [self.location_area],
                'builtup_area': [self.builtup_area],
                'bhk': [self.bhk],
                'bath' : [self.bath],
                'furnished_status': [self.furnished_status],
                'covered_parking': [self.covered_parking],
                'open_parking': [self.open_parking],
                'pooja_room': [self.pooja_room],
                'servant_room': [self.servant_room],
                'extra_rooms': [self.extra_rooms]
            })
            
            if self.property_type == "🏢 Flat / Builder Floor":
                base_price = (np.expm1(flats_pipeline.predict(input_df)[0]) / 100000)
                self.low = base_price - 1.60
                self.high = base_price + 1.60
            elif self.property_type == "🏠 Independent House / Villa":
                base_price = (np.expm1(house_pipeline.predict(input_df)[0]) / 10000000)
                self.low = base_price - 0.07
                self.high = base_price + 0.07
            
        elif self.property_type == '🌍Plot':
            input_df = pd.DataFrame({
                'location_area' : [self.location_area],
                'area' : [self.builtup_area],
                'outside_view' : [self.outside_view],
                'face' : [self.face]
            })
            base_price = (np.expm1(plot_pipeline.predict(input_df)[0]) / 100000)
            self.low = base_price - 3.0
            self.high = base_price + 3.0
        
        st.session_state['base_price'] = base_price
        st.session_state['original_input'] = input_df.iloc[0].to_dict()
        
        if __name__ == "__main__":
            if self.property_type == '🌍Plot' or self.property_type == "🏢 Flat / Builder Floor":
                st.markdown(f"""
                <div style="background:#111;padding:40px;border-radius:20px;text-align:center;">
                    <h2 style="color:white;">Estimated Property Price is Between</h2>
                    <h1 style="color:#00FFAA;">₹ {round(self.low,2):,} - {round(self.high,2):,} Lakhs</h1>
                </div>
                """, unsafe_allow_html=True)   
            elif self.property_type == "🏠 Independent House / Villa":
                st.markdown(f"""
                <div style="background:#111;padding:40px;border-radius:20px;text-align:center;">
                    <h2 style="color:white;">Estimated Property Price is Between</h2>
                    <h1 style="color:#00FFAA;">₹ {round(self.low,2):,} - {round(self.high,2):,} Cr.</h1>
                </div>
                """, unsafe_allow_html=True)  
        else:
            return base_price



# ------------------Price Prediction UI --------------------
# -----------Title -----------------
st.markdown("""
<h1 style='text-align:center;'>💰Price Prediction</h1>
""", unsafe_allow_html=True)

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
    
    # --------------Third row columns -----------------
    input.third_row()
    st.subheader('')
    
    # --------------Fourth row columns
    input.fourth_row()
    st.subheader('')

elif property_type == '🌍Plot':
    # st.subheader('📝 Please Enter Property Details')
    # ---------------First row columns ---------------
    input.row_one()
    st.subheader("")
    
    #---------------Second row columns-------------- 
    input.second_row()
    st.subheader("")
    
    
# -----------Prediction button ------------------
if property_type == '🏢 Flat / Builder Floor':
    predict_btn = st.button(f'🚀 Predict 🏢 {(input.property_type1).capitalize()} Price')
elif property_type == '🏠 Independent House / Villa':
    predict_btn = st.button(f'🚀 Predict 🏠 {(input.property_type1).capitalize()} Price')
elif property_type == '🌍Plot':
    predict_btn = st.button(f'🚀 Predict Plot Price')
    
    
if predict_btn:
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