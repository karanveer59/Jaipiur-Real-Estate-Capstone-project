# Jai Hanuman 🙏🙏🙏🙏🙏

import streamlit as st
import pickle
import pandas as pd
import numpy as np

# st.set_page_config(page_title='Insights', layout='wide')
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


plot_df['predicted_price'] = np.expm1(plot_pipeline.predict(plot_df)) / 100000
AVG_PRICE_PER_SQFT = (plot_df['predicted_price'].sum() / plot_df['area'].sum()) * 100000

flats_df['predicted_price'] = np.expm1(flats_pipeline.predict(flats_df)) / 100000
AVG_PRICE_PER_SQFT_FLAT = (flats_df['predicted_price'].sum() / flats_df['builtup_area'].sum()) * 100000

house_df['predicted_price'] = np.expm1(house_pipeline.predict(house_df)) / 10000000
AVG_PRICE_PER_SQFT_HOUSE = (house_df['predicted_price'].sum() / house_df['builtup_area'].sum()) * 10000000


# ----------------------------- TITLE ---------------------------------
st.markdown("""
<h1 style='text-align:center;'>💡 Smart Insights Module</h1>
<p style='text-align:center; color:gray; font-size:1.2rem; margin-top:8px;'>
    See how property changes affect the predicted price
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# ------------------------------- SESSION STATE CHECK  If user lands here without predicting first -----------------

if "base_price" not in st.session_state:
    st.warning("⚠️ Please go to the Price Prediction page first and predict a price!")
    st.info("👈 Select 'Price Prediction' from the left sidebar")
    st.stop()


# LOAD DATA FROM SESSION STATE

base_price = st.session_state["base_price"]
original_input = st.session_state["original_input"]
property_type = original_input.get("property_type")
is_plot = "face" in original_input and "outside_view" in original_input

# st.markdown(property_type)
# SHOW ORIGINAL PROPERTY SUMMARY

st.subheader("📋 Your Original Property")

if is_plot:
    st.markdown(f"""
    <div style="background:#f8f9fa;border-radius:12px; padding:24px 28px; display:flex;gap:0;margin-bottom:8px;">
        <div style="flex:1;border-right:1px solid #dee2e6;padding-right:24px;">
            <div style="font-size:0.8rem;color:#6c757d;margin-bottom:6px;">📍 Location</div>
            <div style="font-size:1.3rem;font-weight:600;color:#1a1a2e;">  {original_input["location_area"].title()}
            </div>
        </div>
        <div style="flex:1;border-right:1px solid #dee2e6;padding:0 24px;">
            <div style="font-size:0.8rem;color:#6c757d;margin-bottom:6px;">📐 Plot Area</div>
            <div style="font-size:1.3rem;font-weight:600;color:#1a1a2e;"> {original_input["area"]} sqft
            </div>
        </div>
        <div style="flex:1;border-right:1px solid #dee2e6;padding:0 24px;">
            <div style="font-size:0.8rem;color:#6c757d;margin-bottom:6px;">🏞️ Outside View</div>
            <div style="font-size:1.3rem;font-weight:600;color:#1a1a2e;"> {original_input["outside_view"].title()}
            </div>
        </div>
        <div style="flex:1;border-right:1px solid #dee2e6;padding:0 24px;">
            <div style="font-size:0.8rem;color:#6c757d;margin-bottom:6px;">🧭 Face</div>
            <div style="font-size:1.3rem;font-weight:600;color:#1a1a2e;"> {original_input["face"].title()}
            </div>
        </div>
        <div style="flex:1;padding-left:24px;">
            <div style="font-size:0.8rem;color:#6c757d;margin-bottom:6px;">💰 Base Price</div>
            <div style="font-size:1.3rem;font-weight:600;color:#e07b39;"> ₹ {round(base_price, 2)} L
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"""
        <div style="background:#f8f9fa;border-radius:12px; padding:24px 28px;display:flex;gap:0;margin-bottom:8px;">
        <div style="flex:1;border-right:1px solid #dee2e6;padding-right:24px;">
            <div style="font-size:0.8rem;color:#6c757d;margin-bottom:6px;">📍 Location</div>
            <div style="font-size:1.3rem;font-weight:600;color:#1a1a2e;"> {original_input["location_area"].title()}
            </div>
        </div>
        <div style="flex:1;border-right:1px solid #dee2e6;padding:0 24px;">
            <div style="font-size:0.8rem;color:#6c757d;margin-bottom:6px;">🛏 BHK</div>
            <div style="font-size:1.3rem;font-weight:600;color:#1a1a2e;"> {original_input["bhk"]}
            </div>
        </div>
        <div style="flex:1;border-right:1px solid #dee2e6;padding:0 24px;">
            <div style="font-size:0.8rem;color:#6c757d;margin-bottom:6px;">📐 Area</div>
            <div style="font-size:1.3rem;font-weight:600;color:#1a1a2e;"> {original_input["builtup_area"]} sqft
            </div>
        </div>
        <div style="flex:1;padding-left:24px;">
            <div style="font-size:0.8rem;color:#6c757d;margin-bottom:6px;">💰 Base Price</div>
            <div style="font-size:1.3rem;font-weight:600;color:#e07b39;">
                ₹ {round(base_price, 2)} {"Cr." if "house" in property_type or "villa" in property_type else "L"}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")


# -----------user input verify property ---------------S
#
st.subheader("⚡ Modify Property")
st.markdown("Change the fields below and click **Show Insights** to see the price impact.")

if not is_plot:
    col1, col2, col3 = st.columns(3)

    # pp = Price_Prediction.price_predict
    # class new_inputs:
        

    with col1:
        if property_type in ['flat', 'builder floor']:
            all_locations = [
                'Ajmer road', 'Pratap Nagar','Central Jaipur','Mansarovar', 'Jagatpura',
                    'Dholai', 'Ramnagariya', 'Vaishali Nagar', 'Gandhi path',
                    'Patrakar Colony', 'Girdharipura', 'Gokulpura',
                    'Sanganer', 'Sirsi road', 'Anand Nagar', 'Shri Kishanpura',
                    'Jeerota', 'Muhana', 'Jhotwara', 'Nirman Nagar', 'Bhakrota',
                    'Sodala', 'Gurjar Ki Thadi', 'Civil Lines', 'Shyam Nagar',
                    'Bhapura'
            ]
        elif property_type in ['house', 'villa']:
            all_locations = ['Gokulpura', 'Central Jaipur', 'Nirman Nagar','Pratap Nagar', 
                'Jhotwara', 'Muralipura', 'Sanganer', 'Mansarovar', 'Jagatpura',
                'Hanuman Nagar', 'Vaishali Nagar', 'Agra road', 'Sirsi road',
                'Ajmer road', 'Kalwar road', 'Kishorpura', 'Govindpura',
                'Chitrakoot', 'Sodala', 'Gandhi Path', 'Dhawas', 'Shri Kishanpura']
            

        location_options = [original_input["location_area"]] + [l for l in sorted(all_locations) if l != original_input["location_area"]] + ['other']

        new_location = (st.selectbox("📍 Location", options=location_options)).lower()

    with col2:
        new_builtup = st.number_input(
            "📐 Built-up Area (sqft)",
            min_value=50,
            value=int(original_input["builtup_area"])
        )

    with col3:
        if property_type in ['flat', 'builder floor']:
            new_bhk = st.select_slider(
                "🛏 BHK",
                options=[1.0, 2.0,  3.0 , 4.0, 5.0],
                value=float(original_input["bhk"])
            )
        elif property_type in ['house', 'villa']:
            new_bhk = st.select_slider(
                "🛏 BHK",
                options=[1.0,  2.0,  3.0, 4.0 ,5.0],
                value=float(original_input["bhk"])
            )

    # Row 2 — Bath, Furnished, Covered Parking
    col4, col5, col6 = st.columns(3)

    with col4:
        new_bath = st.select_slider(
            "🚿 Bathrooms",
            options=[1.0, 2.0, 3.0, 4.0, 5.0],
            value=float(original_input["bath"])
        )

    with col5:
        if 'flat' in property_type or 'builder floor' in property_type:
            mapping = {
                "Unfurnished": "semifurnished",
                "Semi-furnished": "unfurnished",
                "Furnished": "furnished"
                }
        else:
            mapping = {
                "Unfurnished": "furnished",
                "Semi-furnished": "unfurnished",
                "Furnished":  "semifurnished"
                }
        # Match original furnished status for default
        
        reverse_map = {v: k for k, v in mapping.items()}
        original_furnished_label = reverse_map.get(
            original_input.get("furnished_status", "unfurnished"), "Unfurnished"
        )
        new_furnished = st.selectbox(
            "🪑 Furnished Status",
            options=list(mapping.keys()),
            index=list(mapping.keys()).index(original_furnished_label)
        )

    with col6:
        if 'flat' in property_type or 'builder floor' in property_type:
            new_covered = st.slider(
                "🚗 Covered Parking",
                min_value=0,
                max_value=3,
                value=int(original_input.get("covered_parking", 0))
            )
        else:
            new_covered = st.slider(
                "🚗 Covered Parking",
                min_value=0,
                max_value=5,
                value=int(original_input.get("covered_parking", 0))
            )

    # Row 3 — Open Parking, Pooja Room, Servant Room
    col7, col8, col9 = st.columns(3)

    with col7:
        if 'flat' in property_type or 'builder floor' in property_type:
            new_open = st.slider(
                "🅿️ Open Parking",
                min_value=0,
                max_value=3,
                value=int(original_input.get("open_parking", 0))
            )
        else:
            new_open = st.slider(
                "🅿️ Open Parking",
                min_value=0,
                max_value=5,
                value=int(original_input.get("open_parking", 0))
            )

    with col8:
        new_pooja = st.selectbox(
            "🙏 Pooja Room",
            options=[0, 1],
            index=int(original_input.get("pooja_room", 0))
        )

    with col9:
        new_servant = st.selectbox(
            "🧹 Servant Room",
            options=[0, 1],
            index=int(original_input.get("servant_room", 0))
        )
        
    col10, col11, col12 = st.columns(3)
    # Extra Rooms
    with col11:  
        new_extra = st.selectbox(
            "🚪 Extra Rooms",
            options=[0, 1, 2, 3],
            index=int(original_input.get("extra_rooms", 0))
        )

    st.markdown("---")


    # SHOW INSIGHTS BUTTON

    if st.button("🔍 Show Insights", use_container_width=True):

        # Build new input dataframe
        new_input_df = pd.DataFrame({
            "property_type":    [original_input["property_type"]],
            "location_area":    [new_location],
            "builtup_area":     [float(new_builtup)],
            "bhk":              [float(new_bhk)],
            "bath":             [float(new_bath)],
            "furnished_status": [mapping[new_furnished]],
            "covered_parking":  [float(new_covered)],
            "open_parking":     [float(new_open)],
            "pooja_room":       [float(new_pooja)],
            "servant_room":     [float(new_servant)],
            "extra_rooms":      [float(new_extra)]
        })

        # Predict new price based on property type
# Predict new price — smart logic
        if "house" in property_type or "villa" in property_type:
            model_new_price = np.expm1(house_pipeline.predict(new_input_df)[0]) / 10000000
            price_unit      = "Cr."
            avg_sqft        = AVG_PRICE_PER_SQFT_HOUSE
            unit_divisor    = 10000000
        else:
            model_new_price = np.expm1(flats_pipeline.predict(new_input_df)[0]) / 100000
            price_unit      = "L"
            avg_sqft        = AVG_PRICE_PER_SQFT_FLAT
            unit_divisor    = 100000

        # Area smart check
        area_diff_check = new_builtup - original_input["builtup_area"]

        if area_diff_check != 0:
            base_no_area = pd.DataFrame({
                "property_type":    [original_input["property_type"]],
                "location_area":    [new_location],
                "builtup_area":     [float(original_input["builtup_area"])],
                "bhk":              [float(new_bhk)],
                "bath":             [float(new_bath)],
                "furnished_status": [mapping[new_furnished]],
                "covered_parking":  [float(new_covered)],
                "open_parking":     [float(new_open)],
                "pooja_room":       [float(new_pooja)],
                "servant_room":     [float(new_servant)],
                "extra_rooms":      [float(new_extra)]
            })
            if "house" in property_type or "villa" in property_type:
                price_no_area = np.expm1(
                    house_pipeline.predict(base_no_area)[0]
                ) / 10000000
            else:
                price_no_area = np.expm1(
                    flats_pipeline.predict(base_no_area)[0]
                ) / 100000

            model_area_impact = model_new_price - price_no_area

            if area_diff_check > 0 and model_area_impact < 0:
                new_price = price_no_area + (area_diff_check * avg_sqft) / unit_divisor
            elif area_diff_check < 0 and model_area_impact > 0:
                new_price = price_no_area + (area_diff_check * avg_sqft) / unit_divisor
            else:
                new_price = model_new_price
        else:
            new_price = model_new_price

        change_pct = ((new_price - base_price) / base_price) * 100

        # ── Price Comparison ──
        st.subheader("📊 Price Comparison")

        r1, r2, r3 = st.columns(3)
        r1.metric("Original Price", f"₹ {round(base_price, 2)} {price_unit}")
        r2.metric("New Price",      f"₹ {round(new_price, 2)} {price_unit}")
        r3.metric(
            "Price Change",
            f"{change_pct:+.2f}%",
            delta=f"{change_pct:+.2f}%"
        )

        st.markdown("---")

        # -------------------------- Area suggestion constant Based on carpet area × 1.3 = built-up area

        AREA_SUGGESTIONS = {
            "bhk":            {"min": 250, "max": 300, "label": "BHK",           "icon": "🛏"},
            "bath":           {"min": 40,  "max": 60,  "label": "Bathroom",       "icon": "🚿"},
            "pooja_room":     {"min": 30,  "max": 50,  "label": "Pooja Room",     "icon": "🙏"},
            "extra_rooms":    {"min": 100, "max": 130, "label": "Extra Room",     "icon": "🚪"},
            "servant_room":   {"min": 100, "max": 130, "label": "Servant Room",   "icon": "🧹"},
            "covered_parking":{"min": 140, "max": 140, "label": "Covered Parking","icon": "🚗"},
            "open_parking":   {"min": 110, "max": 120, "label": "Open Parking",   "icon": "🅿️"},
        }

        # ---------------- Calculate all diffs --------
        area_diff = new_builtup - original_input["builtup_area"]
        bhk_diff = new_bhk - float(original_input["bhk"])
        bath_diff = new_bath - float(original_input["bath"])
        extra_diff = new_extra - int(original_input.get("extra_rooms", 0))
        servant_diff = new_servant - int(original_input.get("servant_room", 0))
        pooja_diff = new_pooja - int(original_input.get("pooja_room", 0))
        covered_diff = new_covered - int(original_input.get("covered_parking", 0))
        open_diff = new_open - int(original_input.get("open_parking", 0))
        
        
        def predict_price(input_dict):
            df_temp = pd.DataFrame([input_dict])
            if "house" in property_type or "villa" in property_type:
                return np.expm1(house_pipeline.predict(df_temp)[0]) / 10000000
            else:
                return np.expm1(flats_pipeline.predict(df_temp)[0]) / 100000
    
        def get_individual_impact(feature_key, new_value):
            # """Change only one feature and return price diff from base."""
            # temp = original_input.copy()
            # temp[feature_key] = new_value
            # return round(predict_price(temp) - base_price, 2)
            
            temp = original_input.copy()
            temp[feature_key] = new_value
            model_impact = round(predict_price(temp) - base_price, 2)

            if feature_key == "builtup_area":
                diff = new_value - original_input["builtup_area"]
                avg_sqft = AVG_PRICE_PER_SQFT_HOUSE if ( "house" in property_type or "villa" in property_type
                                ) else AVG_PRICE_PER_SQFT_FLAT
                divisor = 10000000 if ("house" in property_type or "villa" in property_type) else 100000
                if diff > 0 and model_impact < 0:
                    return round((diff * avg_sqft) / divisor, 2)
                elif diff < 0 and model_impact > 0:
                    return round((diff * avg_sqft) / divisor, 2)
                return model_impact

            elif feature_key == "bhk":
                diff = new_value - float(original_input["bhk"])
                if diff > 0 and model_impact < 0:
                    return round(base_price * 0.08 * diff, 2)
                elif diff < 0 and model_impact > 0:
                    return round(base_price * 0.08 * diff, 2)
                return model_impact

            elif feature_key == "bath":
                diff = new_value - float(original_input["bath"])
                if diff > 0 and model_impact < 0:
                    return round(base_price * 0.03 * diff, 2)
                elif diff < 0 and model_impact > 0:
                    return round(base_price * 0.03 * diff, 2)
                return model_impact

            return model_impact
  
        
        def show_insight_card(warning_msg, suggestion_sqft, reason, card_type="warning",price_impact=None):
            """
            Renders a styled 3-part insight card:
            ⚠️ / ✅ / 📉   warning_msg
            💡  Suggestion: suggestion_sqft
            📊  Reason:     reason
            card_type: 'warning' | 'success' | 'error'
            NOTE: Use <b>text</b> for bold inside strings — markdown ** won't work in HTML blocks
            """
            color_map = {
                "warning": ("#fff8e1", "#f9a825", "⚠️"),
                "success": ("#e8f5e9", "#2e7d32", "✅"),
                "error":   ("#ffebee", "#c62828", "📉"),
            }
            bg, border, icon = color_map.get(card_type, color_map["warning"])

            st.markdown(f"""
            <div style="
                background: {bg};
                border-left: 4px solid {border};
                border-radius: 8px;
                padding: 16px 20px;
                margin-bottom: 12px;
            ">
                <div style="display:flex;justify-content:space-between;
                                align-items:center;margin-bottom:10px;">
                        <div style="font-size:1rem;font-weight:600;">
                            {icon}&nbsp; {warning_msg}
                        </div>
                    </div>
                        <div style="font-size:0.92rem;margin-bottom:6px;
                        padding-left:4px;">
                💡      <b>Suggestion:</b>&nbsp; {suggestion_sqft}
                </div>
                <div style="font-size: 0.88rem; color: #555;">
                    📊 <b>Reason:</b>&nbsp; {reason}
                </div>
            </div>
            """, unsafe_allow_html=True)

        # ── Insights Section ──
        st.subheader("💡 Insights — Why Did the Price Change?")

        has_insights = False

        # ── 1. Location ──
        if new_location != original_input["location_area"]:
            has_insights = True
            if change_pct > 0:
                show_insight_card(
                    warning_msg   = f"Location changed to {new_location.title()}",
                    suggestion_sqft = "No area change needed for location switch.",
                    reason        = f"{new_location.title()} has higher demand and premium value "
                                    f"compared to {original_input['location_area'].title()}.",
                    card_type     = "success"
                )
            else:
                
                show_insight_card(
                    warning_msg   = f"Location changed to {new_location.title()}",
                    suggestion_sqft = "Consider a more central or high-demand location.",
                    reason        = f"{new_location.title()} has comparatively lower property "
                                    f"demand than {original_input['location_area'].title()}.",
                    card_type     = "error"
                )

        # ── 2. BHK increased but area same ──
        if bhk_diff > 0 and area_diff == 0:
            has_insights = True
            s = AREA_SUGGESTIONS["bhk"]
            needed = s["min"] * int(bhk_diff)
            needed_max = s["max"] * int(bhk_diff)
            show_insight_card(
                warning_msg    = f"You increased BHK by {bhk_diff:.0f} but area is the same",
                suggestion_sqft= f"Increase built-up area by approx "
                                f"<b>{needed} – {needed_max} sqft</b> per additional BHK",
                reason         = "Additional bedrooms require more space for proper layout, "
                                "comfort, and market value.",
                card_type      = "warning"
            )

        # ── 3. BHK increased with area ──
        elif bhk_diff > 0 and area_diff > 0:
            has_insights = True
            s = AREA_SUGGESTIONS["bhk"]
            needed = s["min"] * int(bhk_diff)
            if area_diff >= needed:
                show_insight_card(
                    warning_msg    = f"BHK increased by {bhk_diff:.0f} with sufficient area added",
                    suggestion_sqft= "Area increase looks adequate — good combination!",
                    reason         = "More BHK with proportional area directly boosts "
                                    "market value and buyer appeal.",
                    card_type      = "success"
                )
            else:
                show_insight_card(
                    warning_msg    = f"BHK increased by {bhk_diff:.0f} but area increase may be low",
                    suggestion_sqft= f"Recommended area increase: <b>{needed} – {s['max'] * int(bhk_diff)} sqft</b>. "
                                    f"You added only {area_diff} sqft.",
                    reason         = "Insufficient area for extra BHK leads to smaller rooms, "
                                    "reducing comfort and buyer interest.",
                    card_type      = "warning"
                )

        # ── 4. BHK decreased ──
        elif bhk_diff < 0:
            has_insights = True
            show_insight_card(
                warning_msg    = f"BHK decreased from {original_input['bhk']} to {new_bhk}",
                suggestion_sqft= "Consider keeping BHK same and reducing area instead.",
                reason         = "Fewer bedrooms lower the perceived value and buyer interest.",
                card_type      = "error"
            )

        # ── 5. Bath changed ──
        if bath_diff > 0:
            has_insights = True
            s = AREA_SUGGESTIONS["bath"]
            needed = s["min"] * int(bath_diff)
            show_insight_card(
                warning_msg    = f"Bathrooms increased by {bath_diff:.0f}",
                suggestion_sqft= f"Increase built-up area by approx <b>{needed} – {s['max'] * int(bath_diff)} sqft</b>",
                reason         = "Each additional bathroom needs dedicated space for "
                                "plumbing, fixtures, and ventilation.",
                card_type      = "success"
            )
        elif bath_diff < 0:
            has_insights = True
            show_insight_card(
                warning_msg    = f"Bathrooms decreased by {abs(bath_diff):.0f}",
                suggestion_sqft= "No area suggestion — reducing bathrooms saves space.",
                reason         = "Fewer bathrooms reduce convenience and slightly "
                                "lower the property value.",
                card_type = "error"
            )

        # ── 6. Pooja Room ──
        if pooja_diff == 1:
            has_insights = True
            s = AREA_SUGGESTIONS["pooja_room"]
            show_insight_card(
                warning_msg    = "Pooja room added",
                suggestion_sqft= f"Increase built-up area by approx <b>{s['min']} – {s['max']} sqft</b>",
                reason         = "A pooja room is a highly valued feature in Jaipur. "
                                "It requires dedicated space for proper layout.",
                card_type      = "success"
            )
        elif pooja_diff == -1:
            has_insights = True
            show_insight_card(
                warning_msg    = "Pooja room removed",
                suggestion_sqft= "No area change needed.",
                reason         = "Removing a pooja room may reduce buyer interest "
                                "in the Jaipur market.",
                card_type      = "error"
            )

        # ── 7. Servant Room ──
        if servant_diff == 1:
            has_insights = True
            s = AREA_SUGGESTIONS["servant_room"]
            show_insight_card(
                warning_msg    = "Servant room added",
                suggestion_sqft= f"Increase built-up area by approx <b>{s['min']} – {s['max']} sqft</b>",
                reason         = "A servant room adds functional value and requires "
                                "its own dedicated space.",
                card_type      = "success"
            )
        elif servant_diff == -1:
            has_insights = True
            show_insight_card(
                warning_msg    = "Servant room removed",
                suggestion_sqft= "No area change needed.",
                reason         = "Minor reduction in utility value.",
                card_type      = "error"
            )

        # ── 8. Extra Rooms ──
        if extra_diff > 0:
            has_insights = True
            s = AREA_SUGGESTIONS["extra_rooms"]
            needed = s["min"] * extra_diff
            show_insight_card(
                warning_msg    = f"Extra rooms increased by {extra_diff}",
                suggestion_sqft= f"Increase built-up area by approx <b>{needed} – {s['max'] * extra_diff} sqft</b>",
                reason         = "Extra rooms add flexibility (study, gym, storage) "
                                "and require adequate space.",
                card_type      = "success"
            )
        elif extra_diff < 0:
            has_insights = True
            show_insight_card(
                warning_msg    = f"Extra rooms decreased by {abs(extra_diff)}",
                suggestion_sqft= "No area change needed.",
                reason         = "Fewer extra rooms reduce overall space utility.",
                card_type      = "error"
            )

        # ── 9. Covered Parking ──
        if covered_diff > 0:
            has_insights = True
            s = AREA_SUGGESTIONS["covered_parking"]
            show_insight_card(
                warning_msg    = f"Covered parking increased by {covered_diff}",
                suggestion_sqft= f"Increase built-up area by approx <b>{s['min'] * covered_diff} sqft</b>",
                reason         = "Covered parking is a premium feature — "
                                "it requires dedicated covered space.",
                card_type      = "success"
            )
        elif covered_diff < 0:
            has_insights = True
            show_insight_card(
                warning_msg    = f"Covered parking decreased by {abs(covered_diff)}",
                suggestion_sqft= "No area change needed.",
                reason         = "Less covered parking reduces premium value.",
                card_type      = "error"
            )

        # ── 10. Open Parking ──
        if open_diff > 0:
            has_insights = True
            s = AREA_SUGGESTIONS["open_parking"]
            show_insight_card(
                warning_msg    = f"Open parking increased by {open_diff}",
                suggestion_sqft= f"Increase built-up area by approx <b>{s['min'] * open_diff} – {s['max'] * open_diff} sqft</b>",
                reason         = "Open parking spots need surface area allocation.",
                card_type      = "success"
            )
        elif open_diff < 0:
            has_insights = True
            show_insight_card(
                warning_msg    = f"Open parking decreased by {abs(open_diff)}",
                suggestion_sqft= "No area change needed.",
                reason         = "Less open parking slightly reduces property utility.",
                card_type      = "error"
            )

        # ── 11. Furnished Status ──
        if mapping[new_furnished] != original_input.get("furnished_status"):
            has_insights = True
            show_insight_card(
                warning_msg    = f"Furnished status changed to {new_furnished}",
                suggestion_sqft= "No area change needed for furnishing.",
                reason         = "Fully furnished properties command a higher premium "
                                "as they reduce buyer setup cost.",
                card_type      = "success"
            )

        # ── 12. Only area changed ──
        if area_diff != 0 and not any([
            bhk_diff, bath_diff, pooja_diff, servant_diff,
            extra_diff, covered_diff, open_diff
        ]):
            has_insights = True
            if area_diff > 0:
                show_insight_card(
                    warning_msg    = f"Built-up area increased by {area_diff} sqft",
                    suggestion_sqft= "Consider adding BHK or rooms to fully utilise the extra space.",
                    reason         = "Larger area with same rooms can improve price "
                                    "but adding rooms maximises value.",
                    card_type      = "success"
                )
            else:
                show_insight_card(
                    warning_msg    = f"Built-up area decreased by {abs(area_diff)} sqft",
                    suggestion_sqft= "Ensure existing rooms are not too cramped.",
                    reason         = "Reduced area lowers price — "
                                    "keep minimum 200 sqft per bedroom for comfort.",
                    card_type      = "error"
                )

        # ── No changes ──
        if not has_insights:
            st.info("ℹ️ No changes were made — the price remains the same.")

        # ── Overall Summary ──
        st.markdown("---")
        st.subheader("📝 Overall Summary")


        features_decreased = any([
            bhk_diff < 0, bath_diff < 0, pooja_diff < 0,
            servant_diff < 0, extra_diff < 0,
            covered_diff < 0, open_diff < 0
        ])
        features_increased = any([
            bhk_diff > 0, bath_diff > 0, pooja_diff > 0,
            servant_diff > 0, extra_diff > 0,
            covered_diff > 0, open_diff > 0
        ])

        if change_pct > 0 and features_decreased and not features_increased:
            st.warning(
                "⚠️ **Note:** Price increased despite reducing features. "
                "This can happen due to patterns in training data — "
                "smaller flats in Jaipur are sometimes priced higher per sqft "
                "in premium areas. Please interpret with caution."
            )
        if change_pct < 0 and features_increased and not features_decreased:
            st.warning(
                "⚠️ **Note:** Price decreased despite adding features. "
                "This may be due to model correlation patterns. "
                "Please interpret with caution."
            )

        price_diff = round(new_price - base_price, 2)
        arrow      = "▲" if price_diff > 0 else "▼"
        clr_bg     = "#e8f5e9" if price_diff >= 0 else "#ffebee"
        clr_border = "#2e7d32" if price_diff >= 0 else "#c62828"
        clr_text   = "#2e7d32" if price_diff >= 0 else "#c62828"

        st.markdown(f"""
        <div style="background:{clr_bg};border:1.5px solid {clr_border};
                    border-radius:12px;padding:24px 28px;margin-top:8px;">
            <div style="display:flex;justify-content:space-between;
                        align-items:center;flex-wrap:wrap;gap:16px;">
                <div>              
                    <div style="font-size:0.85rem;color:#555;margin-bottom:4px;">
                        Original Price
                    </div>
                    <div style="font-size:1.4rem;font-weight:600;color:#1a1a2e;">
                        ₹ {round(base_price, 2)} {price_unit}
                    </div>
                </div>
                <div style="font-size:2rem;color:{clr_text};font-weight:700;">
                    {arrow}
                </div>
                <div>
                    <div style="font-size:0.85rem;color:#555;margin-bottom:4px;">
                        New Price
                    </div>
                    <div style="font-size:1.4rem;font-weight:600;color:#1a1a2e;">
                        ₹ {round(new_price, 2)} {price_unit}
                    </div>
                </div>
                <div style="background:white;border-radius:10px;
                            padding:12px 20px;text-align:center;">
                    <div style="font-size:0.8rem;color:#555;margin-bottom:4px;">
                        Total Change
                    </div>
                    <div style="font-size:1.5rem;font-weight:700;color:{clr_text};">
                        {arrow} ₹ {abs(price_diff)} {price_unit}
                    </div>
                    <div style="font-size:0.9rem;color:{clr_text};font-weight:600;">
                        ({change_pct:+.2f}%)
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if change_pct > 0:
            st.success(
                f"✅ With these changes, the estimated price **increased by {change_pct:.2f}%** "
                f"from ₹ {round(base_price, 2)} {price_unit} to ₹ {round(new_price, 2)} {price_unit}."
            )
        elif change_pct < 0:
            st.error(
                f"📉 With these changes, the estimated price **decreased by {abs(change_pct):.2f}%** "
                f"from ₹ {round(base_price, 2)} {price_unit} to ₹ {round(new_price, 2)} {price_unit}."
            )
        else:
            st.info("The price did not change with the current modifications.")





# -----------------Plot --------Insight-----------------
else:
    col1, col2, col3 = st.columns(3)

    with col1:
        plot_locations = [
            'Central Jaipur', 'Other', 'Bhapura', 'Jagatpura', 'Ajmer road', 'Pratap Nagar', 'Kishorpura', 'Neota',
            'Kalwara', 'Mansarovar', 'Sirsi road', 'Shivdaspura', 'Tonk Road', 'Diggi Road', 'Sanganer',
            'Delhi Jaipur Expressway', 'Renwal Manji', 'Vatika/Vatika Road', 'Kalwar Road', 'Jaisinghpura',
            'Bhakrota', 'Mahaveer Nagar', 'Hardhyanpura', 'Vaishali Nagar', 'Sikar Road', 'Sitapura',
            'Phagi Road', 'Khatipura', 'Agra Road', 'Gandhi Path', 'Mohanpura', 'Jhai', 'Sodala', 'Ramchandpura']
        orig_loc     = original_input["location_area"]
        loc_options  = [orig_loc] + [l for l in sorted(plot_locations) if l.lower() != orig_loc.lower()] + ['other']
        new_location = (st.selectbox("📍 Location", options=loc_options)).lower()

    with col2:
        new_area = st.number_input("📐 Plot Area (sqft)", min_value=50, value=int(original_input["area"]))

    with col3:
        view_options = ["garden view", "road view", "golf course", "water view"]
        orig_view    = original_input["outside_view"].lower()
        view_opts    = [orig_view] + [v for v in view_options if v != orig_view]
        new_view     = st.selectbox("🏞️ Outside View", options=view_opts)

    col4, col5, col6 = st.columns(3)
    with col5:
        face_options = ["east facing", "north facing", "north east facing",
                        "north west facing", "south east facing",
                        "south facing", "south west facing", "west facing"]
        orig_face = original_input["face"].lower()
        face_opts = [orig_face] + [f for f in face_options if f != orig_face]
        new_face  = st.selectbox("🧭 Plot Face", options=face_opts)

    st.markdown("---")

    if st.button("🔍 Show Insights", use_container_width=True):

        # ── Diffs ──
        area_diff = new_area - original_input["area"]
        loc_changed = new_location != original_input["location_area"].lower()
        view_changed = new_view != original_input["outside_view"].lower()
        face_changed = new_face != original_input["face"].lower()


        # HELPER FUNCTIONS

        def predict_price_plot(input_dict):
            """Predict price — always use Title Case for categorical features."""
            temp = {
                "location_area": str(input_dict.get("location_area", "")),
                "area":          float(input_dict.get("area", 0)),
                "outside_view":  str(input_dict.get("outside_view", "")),
                "face":          str(input_dict.get("face", ""))
            }
            return np.expm1(
                plot_pipeline.predict(pd.DataFrame([temp]))[0]
            ) / 100000

        def get_plot_impact(feature_key, new_value):
            """
            Calculate individual feature impact.
            For area — use smart manual fallback if model gives wrong direction.
            """
            temp = original_input.copy()
            temp[feature_key] = new_value

            if feature_key == "area":
                model_impact = round(predict_price_plot(temp) - base_price, 2)
                area_chng    = new_value - original_input["area"]

                # Smart check — model sahi hai ya galat?
                if area_chng > 0 and model_impact < 0:
                    # Area badhi par price ghati — model galat — manual use karo
                    return round((area_chng * AVG_PRICE_PER_SQFT) / 100000, 2)
                elif area_chng < 0 and model_impact > 0:
                    # Area ghati par price badhi — model galat — manual use karo
                    return round((area_chng * AVG_PRICE_PER_SQFT) / 100000, 2)
                else:
                    return model_impact
            else:
                return round(predict_price_plot(temp) - base_price, 2)

   
        # OVERALL NEW PRICE — SMART CALCULATION

        # Title Case input banao model ke liye
        new_input_title = pd.DataFrame({
            "location_area": [new_location],
            "area":          [float(new_area)],
            "outside_view":  [new_view],
            "face":          [new_face]
        })

        model_new_price = np.expm1(
            plot_pipeline.predict(new_input_title)[0]
        ) / 100000

        if area_diff != 0:
            # Area same rakh ke baaki features ka impact nikalo
            base_no_area_change = pd.DataFrame({
                "location_area": [new_location],
                "area":          [float(original_input["area"])],  # area same rakha
                "outside_view":  [new_view],
                "face":          [new_face]
            })
            price_without_area = np.expm1(
                plot_pipeline.predict(base_no_area_change)[0]
            ) / 100000

            model_area_impact  = model_new_price - price_without_area

            # Smart check — model area impact sahi hai ya galat?
            if area_diff > 0 and model_area_impact < 0:
                # Model galat — manual area impact use karo
                manual_area_impact = (area_diff * AVG_PRICE_PER_SQFT) / 100000
                new_price = price_without_area + manual_area_impact
            elif area_diff < 0 and model_area_impact > 0:
                # Model galat — manual area impact use karo
                manual_area_impact = (area_diff * AVG_PRICE_PER_SQFT) / 100000
                new_price = price_without_area + manual_area_impact
            else:
                # Model sahi — model use karo
                new_price = model_new_price
        else:
            new_price = model_new_price

        price_unit = "L"
        change_pct = ((new_price - base_price) / base_price) * 100

        # ── Price Comparison ──
        st.subheader("📊 Price Comparison")
        r1, r2, r3 = st.columns(3)
        r1.metric("Original Price", f"₹ {round(base_price, 2)} L")
        r2.metric("New Price",      f"₹ {round(new_price, 2)} L")
        r3.metric("Price Change",   f"{change_pct:+.2f}%", delta=f"{change_pct:+.2f}%")

        st.markdown("---")

        # ── Price Badge ──
        def price_badge_plot(impact):
            if impact > 0:
                color, bg, symbol = "#2e7d32", "#e8f5e9", "▲"
            elif impact < 0:
                color, bg, symbol = "#c62828", "#ffebee", "▼"
            else:
                color, bg, symbol = "#555555", "#f5f5f5", "●"
            return (
                f'<span style="background:{bg};color:{color};font-weight:600;'
                f'padding:3px 12px;border-radius:20px;font-size:0.85rem;">'
                f'{symbol} ₹ {abs(impact):.2f} L</span>'
            )

        # ── Plot Card ──
        def plot_card(warning_msg, suggestion, reason,
                      card_type="warning", price_impact=None):
            color_map = {
                "warning": ("#fff8e1", "#f9a825", "⚠️"),
                "success": ("#e8f5e9", "#2e7d32", "✅"),
                "error":   ("#ffebee", "#c62828", "📉"),
            }
            bg, border, icon = color_map[card_type]
            badge = price_badge_plot(price_impact) if price_impact is not None else ""
            st.markdown(f"""
            <div style="background:{bg};border-left:4px solid {border};
                        border-radius:8px;padding:16px 20px;margin-bottom:12px;">
                <div style="display:flex;justify-content:space-between;
                            align-items:center;margin-bottom:10px;">
                    <div style="font-size:1rem;font-weight:600;">
                        {icon}&nbsp; {warning_msg}
                    </div>
                    {badge}
                </div>
                <div style="font-size:0.92rem;margin-bottom:6px;padding-left:4px;">
                    💡 <b>Suggestion:</b>&nbsp; {suggestion}
                </div>
                <div style="font-size:0.88rem;color:#555;padding-left:4px;">
                    📊 <b>Reason:</b>&nbsp; {reason}
                </div>
            </div>
            """, unsafe_allow_html=True)

        # ─────────────────────────────────────────
        # RANK TABLES
        # ─────────────────────────────────────────
        VIEW_RANK = {
            "water view": 4, "golf course": 3,
            "road view":  2, "garden view": 1
        }
        FACE_RANK = {
            "north facing": 4, "north east facing": 4,
            "east facing":  3, "north west facing": 3,
            "south east facing": 2, "west facing":  2,
            "south west facing": 1, "south facing": 1
        }
        VIEW_MSG = {
            "water view":  "Water view is the most premium — very high resale value.",
            "golf course": "Golf course facing commands significant premium.",
            "road view":   "Road facing plots have high commercial value and easy "
                           "accessibility, making them ideal for shops or offices. "
                           "However, for residential use they may have higher noise "
                           "and lower privacy — but resale value remains strong.",
            "garden view": "Garden view is peaceful but commands lower premium.",
        }
        FACE_MSG = {
            "north facing":      "North facing — maximum sunlight, top Vastu compliance.",
            "north east facing": "North East — highly auspicious, commands premium.",
            "east facing":       "East facing — morning sunlight, Vastu compliant.",
            "north west facing": "North West — good ventilation, moderate premium.",
            "south east facing": "South East — acceptable, moderate demand.",
            "west facing":       "West facing — afternoon sun, moderate demand.",
            "south west facing": "South West — less preferred in Vastu.",
            "south facing":      "South facing — least preferred, lowest demand.",
        }


        # INSIGHTS SECTION

        st.subheader("💡 Insights — Why Did the Price Change?")
        has_insights = False

        # 1. Location
        if loc_changed:
            has_insights = True
            impact = get_plot_impact("location_area", new_location)
            if impact >= 0:
                plot_card(
                    f"Location changed to {new_location.title()}",
                    "No plot size change needed for location switch.",
                    f"{new_location.title()} has higher land demand than "
                    f"{original_input['location_area'].title()}. "
                    f"Location is the biggest price driver for plots.",
                    "success",
                    price_impact=impact
                )
            else:
                plot_card(
                    f"Location changed to {new_location.title()}",
                    "Consider Central Jaipur, Vaishali Nagar, or Mansarovar "
                    "for better value.",
                    f"{new_location.title()} has lower land demand than "
                    f"{original_input['location_area'].title()}.",
                    "error",
                    price_impact=impact
                )

        # 2. Area — smart manual fallback
        if area_diff != 0:
            has_insights = True
            impact = get_plot_impact("area", new_area)

            if area_diff > 0:
                plot_card(
                    f"Plot area increased by {area_diff} sqft",
                    f"Larger plot allows construction of approx "
                    f"<b>{int(new_area * 0.6):,} – {int(new_area * 0.7):,} sqft</b> "
                    f"built-up area (60–70% FAR typical in Jaipur).",
                    "Area directly drives plot price. "
                    "Every additional sqft adds proportional resale value.",
                    "success",
                    price_impact=impact
                )
            else:
                plot_card(
                    f"Plot area decreased by {abs(area_diff)} sqft",
                    "Minimum recommended plot size for a comfortable house "
                    "in Jaipur is <b>1000–1200 sqft</b>.",
                    "Smaller plot limits construction and reduces resale value.",
                    "error",
                    price_impact=impact
                )

        # 3. Outside View
        if view_changed:
            has_insights = True
            impact    = get_plot_impact("outside_view", new_view)
            orig_rank = VIEW_RANK.get(original_input["outside_view"].lower(), 1)
            new_rank  = VIEW_RANK.get(new_view, 1)
            if new_rank >= orig_rank:
                plot_card(
                    f"Outside view upgraded to {new_view.title()}",
                    "No area change needed — view directly adds premium value.",
                    VIEW_MSG.get(new_view, "Better view adds value."),
                    "success",
                    price_impact=impact
                )
            else:
                plot_card(
                    f"Outside view changed to {new_view.title()}",
                    "Consider Road View or Water View for better resale value.",
                    VIEW_MSG.get(new_view, "Lower view reduces premium."),
                    "error",
                    price_impact=impact
                )

        # 4. Face
        if face_changed:
            has_insights = True
            impact    = get_plot_impact("face", new_face)
            orig_rank = FACE_RANK.get(original_input["face"].lower(), 1)
            new_rank  = FACE_RANK.get(new_face, 1)
            if new_rank >= orig_rank:
                plot_card(
                    f"Plot face upgraded to {new_face.title()}",
                    "No area change needed — facing directly adds Vastu and market value.",
                    FACE_MSG.get(new_face, "Better facing adds value."),
                    "success",
                    price_impact=impact
                )
            else:
                plot_card(
                    f"Plot face changed to {new_face.title()}",
                    "Consider <b>North, North East, or East</b> facing "
                    "for maximum Vastu compliance and resale value.",
                    FACE_MSG.get(new_face, "Less preferred facing reduces demand."),
                    "error",
                    price_impact=impact
                )

        if not has_insights:
            st.info("ℹ️ No changes were made — the price remains the same.")


        # OVERALL SUMMARY

        st.markdown("---")
        st.subheader("📝 Overall Summary")

        price_diff = round(new_price - base_price, 2)
        arrow      = "▲" if price_diff >= 0 else "▼"
        clr_bg     = "#e8f5e9" if price_diff >= 0 else "#ffebee"
        clr_border = "#2e7d32" if price_diff >= 0 else "#c62828"
        clr_text   = "#2e7d32" if price_diff >= 0 else "#c62828"

        st.markdown(f"""
        <div style="background:{clr_bg};border:1.5px solid {clr_border};
                    border-radius:12px;padding:24px 28px;margin-top:8px;">
            <div style="display:flex;justify-content:space-between;
                        align-items:center;flex-wrap:wrap;gap:16px;">
                <div>
                    <div style="font-size:0.85rem;color:#555;margin-bottom:4px;">
                        Original Price
                    </div>
                    <div style="font-size:1.4rem;font-weight:600;color:#1a1a2e;">
                        ₹ {round(base_price, 2)} L
                    </div>
                </div>
                <div style="font-size:2rem;color:{clr_text};font-weight:700;">
                    {arrow}
                </div>
                <div>
                    <div style="font-size:0.85rem;color:#555;margin-bottom:4px;">
                        New Price
                    </div>
                    <div style="font-size:1.4rem;font-weight:600;color:#1a1a2e;">
                        ₹ {round(new_price, 2)} L
                    </div>
                </div>
                <div style="background:white;border-radius:10px;
                            padding:12px 20px;text-align:center;">
                    <div style="font-size:0.8rem;color:#555;margin-bottom:4px;">
                        Total Change
                    </div>
                    <div style="font-size:1.5rem;font-weight:700;color:{clr_text};">
                        {arrow} ₹ {abs(price_diff)} L
                    </div>
                    <div style="font-size:0.9rem;color:{clr_text};font-weight:600;">
                        ({change_pct:+.2f}%)
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    