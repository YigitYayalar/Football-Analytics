# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 03:04:06 2024

@author: Yiğit
"""
import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('player_value_prediction.sav', 'rb'))

#creating a function for Prediction
def market_value_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    return prediction

def main():
    st.title('Football Player Market Value Predictor')

    # Age input
    age = st.number_input('Age', min_value=16, max_value=40, value=20)

    # Other inputs
    CL = st.number_input('Champions League Appearances', min_value=0, value=0)
    wins_gk = st.number_input('Goalkeeper Wins', min_value=0, value=0)
    draws_gk = st.number_input('Goalkeeper Draws', min_value=0, value=0)
    passes_pct_launched_gk = st.number_input('Goalkeeper Passes % Launched', min_value=0.0, max_value=100.0, value=0.0)
    psnpxg_per_shot_on_target_against = st.number_input('Quality of shoots(xG) that goalkeeper faced', min_value=0.0,max_value=1.0, value=0.0)
    clean_sheets = st.number_input('Clean Sheets', min_value=0, value=0)
    goals = st.number_input('Goals', min_value=0, value=0)
    xg_xa_per90 = st.number_input('xG + xA per 90 minutes', min_value=0.0,max_value=1.0, value=0.0)
    passes_ground = st.number_input('Ground Passes', min_value=0, value=0)
    touches_att_pen_area = st.number_input('Touches in Attacking Penalty Area', min_value=0, value=0)
    touches_def_pen_area = st.number_input('Touches in Defensive Penalty Area', min_value=0, value=0)
    aerials_won_pct = st.number_input('Aerials Won %', min_value=0.0, max_value=100.0, value=0.0)
    Pts = st.number_input('Points', min_value=0, value=0)
    xGA = st.number_input('Expected Goals Against', min_value=0.0, value=0.0)
    xG = st.number_input('Expected Goals', min_value=0.0, value=0.0)
    passes_completed_short = st.number_input('Short Passes Completed', min_value=0, value=0)
    passes_into_final_third = st.number_input('Passes Into Final Third', min_value=0, value=0)
    carry_distance = st.number_input('Carry Distance', min_value=0, value=0)
    dribbles_completed = st.number_input('Dribbles Completed', min_value=0, value=0)
    height = st.number_input('Height (in cm)', min_value=150, max_value=220, value=175)
    starting_ratio = st.number_input('Starting Ratio', min_value=0.0, max_value=1.0, value=0.0)
    central_midfield = st.selectbox("Please select 0 or 1 for central_midfield:", (0,1))
    defender_centre_back = st.selectbox("Please select 0 or 1 for centre back:", (0,1))
    defender_left_back = st.selectbox("Please select 0 or 1 for left back:", (0,1))
    defender_right_back = st.selectbox("Please select 0 or 1 for right back:", (0,1))
    forward_centre = st.selectbox("Please select 0 or 1 for centre forward:", (0,1))
    forward_left_winger = st.selectbox("Please select 0 or 1 for left winger:", (0,1))
    forward_right_winger = st.selectbox("Please select 0 or 1 for right winger:", (0,1))
    forward_second_striker = st.selectbox("Please select 0 or 1 for second striker:", (0,1))
    goalkeeper = st.selectbox("Please select 0 or 1 for goalkeeper:", (0,1))
    midfielder_attacking = st.selectbox("Please select 0 or 1 for attacking midfielder:", (0,1))
    midfielder_central = st.selectbox("Please select 0 or 1 for central midfielder:", (0,1))
    midfielder_defensive = st.selectbox("Please select 0 or 1 for defensive midfielder:", (0,1))
    midfielder_left = st.selectbox("Please select 0 or 1 for left midfielder:", (0,1))
    midfielder_right = st.selectbox("Please select 0 or 1 for right midfielder:", (0,1))
    Bundesliga = st.selectbox("Please select 0 or 1 if player plays in Bundesliga:", (0,1))
    LaLiga = st.selectbox("Please select 0 or 1 if player plays in Laliga:", (0,1))
    Ligue1 = st.selectbox("Please select 0 or 1 if player plays in Ligue1:", (0,1))
    Premier_league = st.selectbox("Please select 0 or 1 if player plays in Premier_league:", (0,1))
    Serie_A = st.selectbox("Please select 0 or 1 if player plays in SerieA:", (0,1))


    # Create a dictionary to store user input
    user_input = {
        'age': age,
        'CL': CL,
        'wins_gk': wins_gk,
        'draws_gk': draws_gk,
        'passes_pct_launched_gk': passes_pct_launched_gk,
        'psnpxg_per_shot_on_target_against': psnpxg_per_shot_on_target_against,
        'clean_sheets': clean_sheets,
        'goals': goals,
        'xg_xa_per90': xg_xa_per90,
        'passes_ground': passes_ground,
        'touches_att_pen_area': touches_att_pen_area,
        'touches_def_pen_area': touches_def_pen_area,
        'aerials_won_pct': aerials_won_pct,
        'Pts': Pts,
        'xGA': xGA,
        'xG': xG,
        'passes_completed_short': passes_completed_short,
        'passes_into_final_third': passes_into_final_third,
        'carry_distance': carry_distance,
        'dribbles_completed': dribbles_completed,
        'height': height,
        'starting_ratio': starting_ratio,
        'central_midfield': central_midfield,
        'defender_centre_back': defender_centre_back,
        'defender_left_back' : defender_left_back, 
        'defender_right_back': defender_right_back, 
        'forward_centre': forward_centre, 
        'forward_left_winger': forward_left_winger,
        'forward_right_winger': forward_right_winger, 
        'forward_second_striker': forward_second_striker, 
        'goalkeeper': goalkeeper,
        'midfielder_attacking': midfielder_attacking,
        'midfielder_central': midfielder_central,
        'midfielder_defensive' : midfielder_defensive, 
        'midfielder_left': midfielder_left, 
        'midfielder_right': midfielder_right,
        'Bundesliga': Bundesliga,
        'LaLiga': LaLiga,
        'Ligue1': Ligue1,
        'Premier_league': Premier_league,
        'Serie_A': Serie_A
    }

    # Generate prediction when 'Predict' button is clicked
    if st.button('Predict'):
        prediction = market_value_prediction(list(user_input.values()))
        st.write('Predicted market value:', prediction)

if __name__ == "__main__":
    main()
