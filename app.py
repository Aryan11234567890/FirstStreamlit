import requests
import streamlit as st
from streamlit_lottie import st_lottie
st.set_page_config(page_title='ba bum ba bum!!!!!', page_icon='🧑‍💻', layout = 'wide')

def animate(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

animation_gif = animate('https://lottie.host/eb0e538c-fdaf-41c7-9a25-01a1f6787f6e/kix6FcrWy9.json')
profile_gif = animate('https://lottie.host/c16d3e93-c203-4b56-a9fe-c4d1c2db1606/AtmAZu87xX.json')



with st.container():
    lc, rc = st.columns(2)
    with lc:
        st.subheader('Ayo fellas, It is me hehehehhe !!!!!')
        st.title('Aryan Shanker Saxena')
        st.write('Random coder who also plays games and touches grass!! I love Mathematics and Computer Science. Mostly I just love to solve things using Mathematics and Computers are the best way to express your mathematical fantasies and creations')
        st.write('[Explore more!!!](https://www.github.com/Aryan11234567890)')
    with rc:
        st_lottie(profile_gif, height=300, key="coding")
        
with st.container():
    st.write('---')
    lc, rc = st.columns(2)
    with lc:
        st.header('What I do when i dont touch grass...')
        st.write('Play games like Valorant, Counter Strike, PS4 games, code in Python......')
        st.header('What I do when i touch grass...')
        st.write('Play games like Chess (IRL not app), Cricket, Basektball, Football and a lot more......')
    with rc:
        st_lottie(animation_gif, height = 300, key = "gaming")

with st.container():
    st.write('---')
    st.header('''My Tech Stack (I know it is pretty boring but yeah this is what I've got as of now)...''')
    lc, mp, rc = st.columns(3)
    with lc:
        st.write('**Languages (भाषाएँ)**')
        st.write('Python (seh lenge)')
        st.write('C/C++ (isse bhi seh lenge)')
        st.write('HTML/CSS/JavaScript (sirf JS bahut bawaal hai)')
    with mp:
        st.write('**Frameworks**')
        st.write('ReactJS, Streamlit, Django')
        st.write('TensorFlow, Scikit-learn, NumPy, Pandas, Matplotlib, Seaborn')
    with rc:
        st.write('**Databases**')
        st.write('MySQL, PostgreSQL')

with st.container():
    st.write('---')
    st.header('My projects 🎮🐱‍👤(Your avg college grad projects)....')
    lp, mp, rp = st.columns(3)
    with lp:
        st.write('**Web Projects**')
        st.write('- A Fullstack website which allows users to start a discussion and others can also comment on it. Mini communities can be created within a specific topic called room. Django, oh boy, is an absolute life saver for this project. backend is so easy to maintain. This made me fall in love with python. Django templates also helped me in eliminating JavaScript, phew.')
    with mp:
        st.write('**Django Project**')
        st.write('A Fullstack website which allows users to start a discussion and others can also comment on it. Mini communities can be created within a specific topic called room. Django, oh boy, is an absolute life saver for this project. backend is so easy to maintain. This made me fall in love with python. Django templates also helped me in eliminating JavaScript, phew.')
    with rp:
        st.write('**Django Project**')
        st.write('A Fullstack website which allows users to start a discussion and others can also comment on it. Mini communities can be created within a specific topic called room. Django, oh boy, is an absolute life saver for this project. backend is so easy to maintain. This made me fall in love with python. Django templates also helped me in eliminating JavaScript, phew.')
    