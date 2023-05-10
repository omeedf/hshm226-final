import streamlit as st
import folium
from streamlit_folium import folium_static

# Define locations of primary sources and their corresponding game codes
locations = {
    'Persia': {'coords': [36.26, 59.57], 'game_code': 'ZI123'},
    'Italy': {'coords': [44.50, 11.34], 'game_code': 'AN456'},
    'China': {'coords': [34.26, 108.93], 'game_code': 'BG789'},
    'India': {'coords': [27.17, 78.04], 'game_code': 'AA012'},
    'Mexico': {'coords': [19.43, -99.13], 'game_code': 'TP345'}
}

# Define function for the game page
def game_page(game_code):
    st.title('Primary Source Game')

    # Astonomical Trivia Game
    if game_code == 'ZI123':
        st.header("Astronomical Trivia")
        
        # Question 1
        question = st.selectbox("Which Persian astronomer wrote the Zij-i Ilkhani?",
                                options=["", "Al-Biruni", "Nasir al-Din al-Tusi", "Al-Khwarizmi"])
        if question == "Nasir al-Din al-Tusi":
            st.success("Correct! Nasir al-Din al-Tusi wrote the Zij-i Ilkhani.")
            st.write("The Compendium of Observations of the Movements of the Stars (Zij-i Ilkhani) by Nasir al-Din al-Tusi (Persia, 13th century)...")
        elif question != "":
            st.error("Incorrect. Hint: This Persian astronomer was also a prominent mathematician and philosopher.")

         # Question 2
        question = st.selectbox("Which ruler commissioned the Zij-i Ilkhani to be written?",
                                options=["", "Genghis Khan", "Hulagu Khan", "Timur", "Babur"])
        if question == "Hulagu Khan":
            st.success("Correct! Hulagu Khan was the patron of Nasir al-Din al-Tusi.")
            st.write("")
        elif question != "":
            st.error("Incorrect. Hint: This ruler was the founder of the Ilkhanate dynasty in Iran.")

        # Question 3
        question = st.selectbox("In what language was the Zij-i Ilkhani originally written?",
                                options=["", "Arabic", "Farsi (Persian)", "Turkish", "Urdu"])
        if question == "Farsi (Persian)":
            st.success("Correct! Zij-i Ilkhani was originally written in Farsi (Persian), and later translated to Arabic.")
            st.write("")
        elif question != "":
            st.error("Incorrect. Hint: This language is the official language of Iran.")

        # Question 4
        question = st.selectbox("Nasir al-Din al-Tusi also wrote treatises laying the foundation for improvements to which celestial tool?",
                                options=["", "Telescope", "Sextant", "Astrolabe", "Planisphere"])
        if question == "Astrolabe":
            st.success("Correct! Nasir al-Din al-Tusi wrote many treatises outlining and explaining the astrolabe.")
            st.write("")
        elif question != "":
            st.error("Incorrect. Hint: This device, which is still used today, was originally developed by the ancient Greeks but was improved upon by Islamic astronomers like Nasir al-Din al-Tusi.")

    # Timeline Challenge Game
    elif game_code == 'AN456':
        st.header("Timeline Challenge")
        event_order = st.multiselect("Arrange these events in chronological order:",
                                      options=["Copernicus publishes 'On the Revolutions of the Heavenly Spheres'",
                                               "Galileo builds his first telescope",
                                               "Riccioli publishes 'Almagestum Novum'",
                                               "Kepler publishes 'Astronomia Nova'"],
                                      default=[])
        if event_order == ["Copernicus publishes 'On the Revolutions of the Heavenly Spheres'",
                           "Kepler publishes 'Astronomia Nova'",
                           "Galileo builds his first telescope",
                           "Riccioli publishes 'Almagestum Novum'"]:
            st.success("Correct! You have arranged the events in chronological order.")
            st.write("The Almagestum Novum by Giovanni Battista Riccioli (Italy, 1651)...")
        elif event_order:
            st.error("Incorrect. Hint: Think about the sequence of astronomers' discoveries and publications.")

    # Herbal Medicine Matching Game
    elif game_code == 'BG789':
        st.header("Herbal Medicine Matching")
        match_1 = st.selectbox("Which herb is used to treat coughs and colds?", options=["", "Ginseng", "Astragalus", "Licorice"])
        match_2 = st.selectbox("Which herb is used to improve energy and stamina?", options=["", "Ginseng", "Astragalus", "Licorice"])
        match_3 = st.selectbox("Which herb is known as the 'king of herbs' in Chinese medicine and is believed to boost the immune system and improve overall health?", options=["", "Reishi Mushroom", "Ginkgo Biloba", "Turmeric"])
        match_4 = st.selectbox("Which herb is commonly used in Chinese medicine to improve digestion and alleviate stomach discomfort?", options=["", "Fennel", "Ginger", "Cinnamon"])
        match_5 = st.selectbox("Which herb is known for its calming properties and is used to treat anxiety, insomnia, and other stress-related conditions?", options=["", "Valerian Root", "St. John's Wort", "Kava"])
        match_6 = st.selectbox("Which herb is used to alleviate pain and inflammation, and is often used to treat arthritis and other joint conditions?", options=["", "Turmeric", "Boswellia", "Devil's Claw"])
        match_7 = st.selectbox("Which herb is commonly used in Chinese medicine to improve circulation and treat menstrual cramps?", options=["", "Dong Quai", "Black Cohosh", "Chasteberry"])
        
        if (match_1 == "Licorice" and match_2 == "Ginseng" and match_3 == "Reishi Mushroom" and match_4 == "Ginger" and match_5 == "Valerian Root" and match_6 == "Turmeric" and match_7 == "Dong Quai"):
            st.success("Correct! You have matched all the herbs correctly.")
            st.write("The Bencao Gangmu (Compendium of Materia Medica) by Li Shizhen (China, 16th century)...")
        elif (match_1 != "" and match_2 != "" and match_3 != "" and match_4 != "" and match_5 != "" and match_6 != "" and match_7 != ""):
            st.error("Incorrect. Hint: Some herbs are commonly used in cooking or have a distinct aroma or flavor, while others are often prepared in tea or supplement form.")

    # Mughal Empire Quiz
    elif game_code == 'AA012':
        st.header("Mughal Empire Quiz")
        question = st.radio("What was the official language of the Mughal Empire?",
                            options=["", "Hindi", "Urdu", "Persian"])
        if question == "Persian":
            st.success("Correct! Persian was the official language of the Mughal Empire.")
            st.write("The Ain-i-Akbari (The Institutes of Akbar) by Abul Fazl (India, 16th century)...")
        elif question != "":
            st.error("Incorrect. Hint: This language is also widely spoken in Iran.")

        question_2 = st.radio("Who was the first emperor of the Mughal Empire?",
                        options=["", "Babur", "Akbar", "Jahangir"])
        if question_2 == "Babur":
            st.success("Correct! Babur was the first emperor of the Mughal Empire.")
        elif question_2 != "":
            st.error("Incorrect. Hint: He was also known for his writing, poetry, and love of literature.")

        question_3 = st.radio("Who was the last emperor of the Mughal empire?",
                        options=["", "Bahadur Shah II (Zafar)", "Aurangzeb", "Shah Jahan II"])
        if question_3 == "Bahadur Shah II (Zafar)":
            st.success("Correct! Bahadur Shah Zafar was the last emperor of the Mughal empire.")
        elif question_3 != "":
            st.error("Incorrect. Hint: He was exiled to Rangoon after the Indian Rebellion of 1857.")       

    elif game_code == 'TP345':
        st.header("Indigenous Medicine Puzzle")
        puzzle_solution = st.text_input("Enter the names of two indigenous plants used in Nahua and Aztec medicine (separated by a comma):")
        if "chamomile" in puzzle_solution.lower() and "cacao" in puzzle_solution.lower():
            st.success("Correct! Chamomile and cacao are two examples of indigenous plants used in Nahua and Aztec medicine.")
            st.write("Libellus de Medicinalibus Indorum Herbis by Martin de la Cruz and translated by Juan Badiano (Mexico, 16th century)...")
        elif puzzle_solution:
            st.error("Incorrect. Hint: One herb is known for being a common tea ingredient, while the other can be found in chocolate.")

        question_1 = st.radio("What is the English translation of 'Libellus de Medicinalibus Indorum Herbis'?",
                        options=["", "The Indigenous Herbal", "The Compendium of Materia Medica", "Little Book of the Medicinal Herbs of the Indians"])
        question_2 = st.radio("What indigenous Mexican plant was used to treat skin infections and promote wound healing?",
                            options=["", "Chamomile", "Cacao", "Eucalyptus"])
        question_3 = st.radio("What is the Nahuatl name for the plant that is used to make chocolate?",
                            options=["", "Xocolatl", "Tlilxochitl", "Mizquitl"])
        
    
        if question_1 == "Little Book of the Medicinal Herbs of the Indians" and question_2 == "Eucalyptus" and question_3 == "Xocolatl":
            st.success("Congratulations! You have answered all questions correctly.")
        elif question_1 != "" and (question_1 != "Little Book of the Medicinal Herbs of the Indians" or question_2 != "Chamomile" or question_3 != "Xocolatl"):
            st.error("Sorry, your answer is incorrect. Please try again.") 

# Streamlit app
st.title('World Map: Primary Sources')
st.subheader('Instructions: click on a pin to select a location and play the corresponding game by entering the game code below.')


# Create folium map
m = folium.Map(location=[30.76, -3.47], zoom_start=2,
               tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}", attr="Data by ESRI")

# Add markers for primary sources with click functionality
for country, data in locations.items():
    folium.Marker(data['coords'], popup=f'<b>{country}</b><br>Game Code: {data["game_code"]}').add_to(m)

# Display folium map in Streamlit
folium_static(m)

# Game code input
game_code = st.text_input("Enter the game code:")
if game_code in [data['game_code'] for data in locations.values()]:
    game_page(game_code)
else:
    if game_code:
        st.error("Invalid game code. Please try again.")

