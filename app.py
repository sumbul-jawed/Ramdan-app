import streamlit as st
import requests

# Page Layout
st.set_page_config(page_title="\U0001F319 Ramadan App", layout="wide")

# UI Custom Styling
st.markdown(
    """
   <style>
    /* Sidebar Customization */
    [data-testid="stSidebar"] {
        background-color: #E28B46  !important; /* Light Pink */
        color: black !important;
    }
    [data-testid="stSidebar"] * {
        color: black !important;
    }

    /* Custom Content Box */
    .content-box {
        background-color: #FFFDD0;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
</style>

    """,
    unsafe_allow_html=True
)

# Sidebar Navigation
st.sidebar.header("📌 Islamic Resources")
menu = st.sidebar.radio(
    "Select a Section",
    ["Home", "Sehri & Iftar Timings", "Sehri & Iftar Duas", "3 Ashras Duas", "Ramadan Calendar "]
)

# Home Page (Ramadan Mubarak + Hadith)
if menu == "Home":
    st.markdown("""
        <div style='color: #A131F3; font-size: 40px; font-weight: bold;'>
            \U0001F319 Ramadan Mubarak \U0001F319
        </div>
    """, unsafe_allow_html=True)
   
    # Ramadan Hadith
    st.markdown("""
    ### 💚 **Ramadan Hadith 1st**  
    **عن أبي هريرة رضي الله عنه قال: قال رسول الله 🗣️:**  
    **إِذَا جَاءَ رَمَضَانُ فُتِحَتْ أَبوَابُ الجَنَّةِ وَغُلِّقَتْ أَبوَابُ النَّارِ وصُفِّدَتْ الشَّيَاطِينُ**  
    *(صحیح البخاری: 1899، صحیح مسلم: 1079)*  

    **English Translation:**  
    *"When the month of Ramadan starts, the gates of Jannah (Paradise) are opened, the gates of Jahannam (Hellfire) are closed, and the devils are chained."*  
    *(Sahih Bukhari: 1899, Sahih Muslim: 1079)*
    """)
    
    st.markdown("""
      ### 💚 **Ramadan Hadith 2nd**  
     **إِنَّ فِي الْجَنَّةِ بَابًا يُقَالُ لَهُ الرَّيَّانُ، يَدْخُلُ مِنْهُ الصَّائِمُونَ يَوْمَ الْقِيَامَةِ، لَا يَدْخُلُ مِنْهُ أَحَدٌ غَيْرُهُمْ**  
     *(صحیح البخاری: 1896، صحیح مسلم: 1152)*    

      **English Translation:**  
      *"Indeed, in Paradise, there is a gate called **Ar-Rayyan**. Only the fasting people will enter through it on the Day of Judgment, and no one else will enter through it."* 
      *(Sahih Bukhari: 1896, Sahih Muslim: 1152)* 
     """)


    # 📜 **Sehri & Iftar Timings**
elif menu == "Sehri & Iftar Timings":
    st.markdown("""
        <div style='text-align: center; color: #F64571; font-size: 35px; font-weight: bold;'>
            Sehri & Iftar Timings
        </div>
    """, unsafe_allow_html=True)
    
    city = st.text_input("🌍 Enter Your City", value="Karachi")
    country = st.text_input("🏳️ Enter Your Country", value="Pakistan")

    if st.button("Get Sehri & Iftar Timings"):
        api_url = f"https://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2"
        response = requests.get(api_url).json()

        sehri_time = response['data']['timings']['Fajr']
        iftar_time = response['data']['timings']['Maghrib']

        # 🌙 Display Sehri & Iftar Timings
        st.markdown(f"""
            <div style='background: #f8f8f8; padding: 15px; border-radius: 10px; text-align: center;
                        box-shadow: 2px 2px 10px rgba(0,0,0,0.2);'>
                <h2 style='color: #FF5733;'>⏳ Sehri & Iftar Timings</h2>
                <p style='font-size: 18px;'><b>🌙 Sehri Time:</b> {sehri_time}</p>
                <p style='font-size: 18px;'><b>🌅 Iftar Time:</b> {iftar_time}</p>
            </div>
        """, unsafe_allow_html=True)

# Sehri & Iftar Duas
elif menu == "Sehri & Iftar Duas":
    st.markdown("""
        <div style='color: #3357FF; font-size: 30px; font-weight: bold;'>
            Sehri & Iftar Duas
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    **💛 Sehri Dua:**  
    **وَبِصَوْمِ غَدٍ نَّوَيْتُ مِنْ شَهْرِ رَمَضَانَ**  
    *"I intend to keep the fast for tomorrow in the month of Ramadan."*  

    **💜 Iftar Dua:**  
    **اللَّهُمَّ إِنِّي لَكَ صُمْتُ وَبِكَ آمَنْتُ وَعَلَيْكَ تَوَكَّلْتُ وَعَلَىٰ رِزْقِكَ أَفْطَرْتُ**  
    *"O Allah! I fasted for You, I believe in You, I put my trust in You, and I break my fast with Your sustenance."*  
    """)

# 3 Ashras
elif menu == "3 Ashras Duas":
    st.markdown("""
        <div style='color: #C70039; font-size: 25px; font-weight: bold;'>
            Three Ashras of Ramadan
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    **1st Ashra (Mercy) - رحمت**  
    **Dua:**  
    **اللَّهُمَّ ارْحَمْنِي يَا أَرْحَمَ الرَّاحِمِينَ**  
    *"O Allah, have mercy on me, O Most Merciful of those who show mercy."*  

    **2nd Ashra (Forgiveness) - مغفرت**  
    **Dua:**  
    **أَسْتَغْفِرُ اللَّهَ رَبِّي مِنْ كُلِّ ذَنْبٍ وَأَتُوبُ إِلَيْهِ**  
    *"I seek forgiveness from Allah, my Lord, for all my sins and turn to Him in repentance."*  

    **3rd Ashra (Salvation) - نجات**  
    **Dua:**  
    **اللَّهُمَّ أَجِرْنِي مِنَ النَّارِ**  
    *"O Allah, save me from the fire (of Hell)."*  
    """)

# Ramadan Calendar
elif menu == "Ramadan Calendar ":
    st.markdown("""
        <div style=' color: #127A07; font-size: 30px; font-weight: bold;'>
            Ramadan Calendar 2025
        </div>
    """, unsafe_allow_html=True)
    
    # Ramadan Calendar Image
    image_url = "https://raw.githubusercontent.com/sumbul-jawed/Ramdan-app/main/ram.PNG"

        # Display Image
    st.image(image_url, caption="Ramadan Calendar", use_container_width=400)
    # 🎉 Closing Message
st.markdown("##### The month of mercy, blessings, and forgiveness—Ramadan is a gift from Allah. 🌙✨")
