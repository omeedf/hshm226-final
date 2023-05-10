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
def game_page(game_code: str) -> None:
    """Returns the game page based on the game code"""
    st.title('Primary Source Game')

    # Astonomical Trivia Game
    if game_code == 'ZI123':
        num_correct = 0
        st.header("Astronomical Trivia")

        # Question 1
        question = st.selectbox("Which Persian astronomer wrote the Zij-i Ilkhani?",
                                options=["", "Al-Biruni", "Nasir al-Din al-Tusi", "Al-Khwarizmi"])
        if question == "Nasir al-Din al-Tusi":
            num_correct += 1
            st.success("Correct! Nasir al-Din al-Tusi wrote the Zij-i Ilkhani.")
        elif question != "":
            st.error("Incorrect. Hint: This Persian astronomer was also a prominent mathematician and philosopher.")

         # Question 2
        question = st.selectbox("Which ruler commissioned the Zij-i Ilkhani to be written?",
                                options=["", "Genghis Khan", "Hulagu Khan", "Timur", "Babur"])
        if question == "Hulagu Khan":
            num_correct += 1
            st.success("Correct! Hulagu Khan was the patron of Nasir al-Din al-Tusi.")
        elif question != "":
            st.error("Incorrect. Hint: This ruler was the founder of the Ilkhanate dynasty in Iran.")

        # Question 3
        question = st.selectbox("In what language was the Zij-i Ilkhani originally written?",
                                options=["", "Arabic", "Farsi (Persian)", "Turkish", "Urdu"])
        if question == "Farsi (Persian)":
            num_correct += 1
            st.success("Correct! Zij-i Ilkhani was originally written in Farsi (Persian), and later translated to Arabic.")
        elif question != "":
            st.error("Incorrect. Hint: This language is the official language of Iran.")

        # Question 4
        question = st.selectbox("Nasir al-Din al-Tusi also wrote treatises laying the foundation for improvements to which celestial tool?",
                                options=["", "Telescope", "Sextant", "Astrolabe", "Planisphere"])
        if question == "Astrolabe":
            num_correct += 1
            st.success("Correct! Nasir al-Din al-Tusi wrote many treatises outlining and explaining the astrolabe.")
        elif question != "":
            st.error("Incorrect. Hint: This device, which is still used today, was originally developed by the ancient Greeks but was improved upon by Islamic astronomers like Nasir al-Din al-Tusi.")

        if num_correct >= 4:
            st.balloons()
            st.subheader("Summary of the primary source:")
            st.write("Zij-i Ilkhani by Nasir al-Din al-Tusi (Persia, 13th century) is a book of astronomical tables which describes planetary movements. It contains tables for calculating not only positions of planets but also the names of stars. The data used to compile these tables was compiled over 12 years in the Maragha observatory. This data enabled al-Tusi to accurately predict many cosmological processes (J. A. Boyle (1963) 'The Longer Introduction to the Zij-i Ilkhani of Nasir ad-Din Tusi', Journal of Semitic Studies 8(2), pp.244-254).")

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
            st.balloons()
            st.subheader("Summary of the primary source:")
            st.write("The Almagestum Novum by Giovanni Battista Riccioli (Italy, 1651) is a significant astronomical work that presents a comprehensive analysis of both the Copernican and Ptolemaic systems. It played a crucial role in shaping the scientific discourse of its time by providing a platform for comparing and contrasting these two influential models of the universe. Riccioli's work also included meticulous observations and experiments, helping to advance the understanding of celestial mechanics and laying the groundwork for future astronomical research. (Grant, Edward. (1994). Planets, Stars, and Orbs: The Medieval Cosmos, 1200-1687. Cambridge: Cambridge University Press. ISBN 9780521565097.)")
        elif event_order:
            st.error("Incorrect. Hint: Think about the sequence of astronomers' discoveries and publications.")

    # Herbal Medicine Matching Game
    elif game_code == 'BG789':
        num_correct = 0
        st.header("Herbal Medicine Matching")

        match_1 = st.selectbox("Which herb is used to treat coughs and colds?", options=[
                               "", "Ginseng", "Astragalus", "Licorice"])
        if match_1 == "Licorice":
            num_correct += 1
            st.success("Correct!")
        elif match_1 != "":
            st.error("Incorrect. Hint: this herb is popular in candy today!")

        match_2 = st.selectbox("Which herb is used to improve energy and stamina?", options=[
                               "", "Ginseng", "Astragalus", "Licorice"])
        if match_2 == "Ginseng":
            num_correct += 1
            st.success("Correct!")
        elif match_2 != "":
            st.error("Incorrect. Hint: this herb is sometimes called 'man-root' because it can be shaped like a person.")

        match_3 = st.selectbox("Which herb is known as the 'king of herbs' in Chinese medicine and is believed to boost the immune system and improve overall health?", options=[
                               "", "Reishi Mushroom", "Ginkgo Biloba", "Turmeric"])
        if match_3 == "Reishi Mushroom":
            num_correct += 1
            st.success("Correct!")
        elif match_3 != "":
            st.error("Incorrect. Hint: this herb is neither an animal nor a plant!")
        
        match_4 = st.selectbox("Which herb is commonly used in Chinese medicine to improve digestion and alleviate stomach discomfort?", options=[
                               "", "Fennel", "Ginger", "Cinnamon"])
        if match_4 == "Ginger":
            num_correct += 1
            st.success("Correct!")
        elif match_4 != "":
            st.error("Incorrect. Hint: this herb is commonly used today in both Chinese and Japanese cuisine.")
        
        match_5 = st.selectbox("Which herb is known for its calming properties and is used to treat anxiety, insomnia, and other stress-related conditions?",
                               options=["", "Valerian Root", "St. John's Wort", "Kava"])
        if match_5 == "Valerian Root":
            num_correct += 1
            st.success("Correct!")
        elif match_5 != "":
            st.error("Incorrect. Hint: the name of this herb comes from the Latin word meaning 'to be strong' or 'to be in good health.'")

        match_6 = st.selectbox("Which herb is used to alleviate pain and inflammation, and is often used to treat arthritis and other joint conditions?", options=[
                               "", "Turmeric", "Boswellia", "Devil's Claw"])
        if match_6 == "Turmeric":
            num_correct += 1
            st.success("Correct!")
        elif match_6 != "":
            st.error("Incorrect. Hint: this herb is popular in many Indian dishes and is commonly used in dyes.")

        match_7 = st.selectbox("Which herb is commonly used in Chinese medicine to improve circulation and treat menstrual cramps?", options=[
                               "", "Dong Quai", "Black Cohosh", "Chasteberry"])
        if match_7 == "Dong Quai":
            num_correct += 1
            st.success("Correct!")
        elif match_7 != "":
            st.error("Incorrect. Hint: this herb is sometimes called the 'female ginseng' and has been used in China, Korea, and Japan for over 1000 years.")

        if num_correct >= 7:
            st.success("Great job! You have matched all the herbs correctly. You would make a great doctor in 16th century China!")
            st.balloons()
            st.subheader("Summary of the primary source:")
            st.write("The Bencao Gangmu (Compendium of Materia Medica) by Li Shizhen (China, 16th century) is an encyclopedic work that documents the knowledge of traditional Chinese medicine, including the properties, effects, and applications of thousands of medicinal plants, minerals, and animals. It is regarded as one of the most comprehensive and authoritative texts on traditional Chinese medicine, and it has significantly influenced the development of medical science both within China and worldwide (Lin DY, Zhou CE, Lai XM, Yang SJ. [Research and analysis of data source--analysis of the items of medical plants in Xiandai Bencao Gangmu]. Zhongguo Zhong Yao Za Zhi. 2008 Sep;33(17):2094-6. Chinese).")

    # Mughal Empire Quiz
    elif game_code == 'AA012':
        st.header("Mughal Empire Quiz")
        num_correct = 0

        question = st.radio("What was the official language of the Mughal Empire?",
                            options=["", "Hindi", "Urdu", "Persian"])
        if question == "Persian":
            num_correct += 1
            st.success("Correct! Persian was the official language of the Mughal Empire.")
        elif question != "":
            st.error("Incorrect. Hint: This language is also widely spoken in Iran.")

        question_2 = st.radio("Who was the first emperor of the Mughal Empire?",
                              options=["", "Babur", "Akbar", "Jahangir"])
        if question_2 == "Babur":
            num_correct += 1
            st.success("Correct! Babur was the first emperor of the Mughal Empire.")
        elif question_2 != "":
            st.error("Incorrect. Hint: He was also known for his writing, poetry, and love of literature.")

        question_3 = st.radio("Who was the last emperor of the Mughal empire?",
                              options=["", "Bahadur Shah II (Zafar)", "Aurangzeb", "Shah Jahan II"])
        if question_3 == "Bahadur Shah II (Zafar)":
            num_correct += 1
            st.success( "Correct! Bahadur Shah Zafar was the last emperor of the Mughal empire.")
        elif question_3 != "":
            st.error("Incorrect. Hint: He was exiled to Rangoon after the Indian Rebellion of 1857.")

        if num_correct >= 3:
            st.balloons()
            st.subheader("Summary of the primary source:")
            st.write("The Ain-i-Akbari (The Institutes of Akbar) by Abul Fazl (India, 16th century) is a detailed chronicle of culture and society during the reign of Emperor Akbar, one of the great Mughal rulers in India. The text covers a range of topics such as valuable information about the natural resources, flora, and fauna of the region, reflecting the scientific and intellectual curiosity in India at the time (http://www.columbia.edu/itc/mealac/pritchett/00litlinks/abulfazl/ain_zzcontents.html)")


    elif game_code == 'TP345':
        st.header("Indigenous Medicine Puzzle")
        num_correct = 0

        puzzle_solution = st.text_input("Enter the names of two indigenous plants used in Nahua and Aztec medicine (separated by a comma):")
        if "chamomile" in puzzle_solution.lower() and "cacao" in puzzle_solution.lower():
            num_correct += 1
            st.success("Correct! Chamomile and cacao are two examples of indigenous plants used in Nahua and Aztec medicine.")
        elif puzzle_solution:
            st.error("Incorrect. Hint: One herb is known for being a common tea ingredient, while the other can be found in chocolate.")

        question_1 = st.radio("What is the English translation of 'Libellus de Medicinalibus Indorum Herbis'?",
                              options=["", "The Indigenous Herbal", "The Compendium of Materia Medica", "Little Book of the Medicinal Herbs of the Indians"])
        if question_1 == "Little Book of the Medicinal Herbs of the Indians":
            num_correct += 1
            st.success("Correct!")
        elif question_1 != "":
            st.error("Incorrect. Try again!")

        question_2 = st.radio("What indigenous Mexican plant was used to treat skin infections and promote wound healing?",
                              options=["", "Chamomile", "Cacao", "Eucalyptus"])
        if question_2 == "Eucalyptus":
            num_correct += 1
            st.success("Correct!")
        elif question_2 != "":
            st.error("Incorrect. Try again!")

        question_3 = st.radio("What is the Nahuatl name for the plant that is used to make chocolate?",
                              options=["", "Xocolatl", "Tlilxochitl", "Mizquitl"])
        if question_3 == "Xocolatl":
            num_correct += 1
            st.success("Correct!")
        elif question_3 != "":
            st.error("Incorrect. Try again!")
        
        if num_correct >= 4:
            st.success("Congratulations! You have answered all questions correctly.")
            st.balloons()
            st.subheader("Summary of the primary source:")
            st.write("Libellus de Medicinalibus Indorum Herbis by Martin de la Cruz and translated by Juan Badiano (Mexico, 16th century) is an illustrated herbal manuscript that documents the medicinal properties and uses of various plants native to Mexico. The manuscript is based on the indigenous knowledge of the Aztec people and serves as a valuable resource for understanding their traditional medical practices and expertise in science (L. Y. Centeno-Betanzos, R. Reyes-Chilpa, N. B. Pigni, C. K. Jankowski, L. Torras-Claveria, J. Bastida, Chem. Biodiversity 2021, 18, e2000834).")

# Streamlit app
st.title('Global Science Explorer')
st.subheader('Instructions: click on a pin to select a location and play the corresponding game by entering the game code below.')


# Create folium map
m = folium.Map(location=[30.76, -3.47], zoom_start=2,
               tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}", attr="Data by ESRI")

# Add markers for primary sources with click functionality
for country, data in locations.items():
    folium.Marker(
        data['coords'], popup=f'<b>{country}</b><br>Game Code: {data["game_code"]}').add_to(m)

# Display folium map in Streamlit
folium_static(m)

# Game code input
code = st.text_input("Enter the game code:")
if code in [data['game_code'] for data in locations.values()]:
    game_page(code)
else:
    if code:
        st.error("Invalid game code. Please try again.")
