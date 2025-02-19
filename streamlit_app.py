import random
import streamlit as st

# List of coworkers
coworkers = ['Laiyi', 'Karen', 'Svenja', 'Remi', 'Amanda', 'Penny', 'Mai', 'Teppei', 'Valentina', 'Saki', 'Satoru', 'Ryoko', 'Kiho', 'Yudai', 'Kei', 'Dan', 'Martin']

# Initialize the lunchbuddy in the session state if not already set
if 'lunchbuddy' not in st.session_state:
    st.session_state.lunchbuddy = random.choice(coworkers) + ' today!!!!!'

# Display the lunch buddy
st.write(f"""
# You are having lunch with: 
## {st.session_state.lunchbuddy}
""")

# Button to reroll the lunchbuddy
if st.button('Reroll'):
    st.session_state.lunchbuddy = random.choice(coworkers) + ' today!!!!!'
