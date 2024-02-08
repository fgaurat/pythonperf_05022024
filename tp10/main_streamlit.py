import streamlit as st
from UserDAO import UserDAO


def main():
    st.set_page_config(layout="wide")
    # Run streamlit
    # streamlit run main_streamlit.py
    with UserDAO('users_db.db') as dao:
        data_users = list(dao.findAll())
    
    

    st.button("Reset", type="primary")
    if st.button('Say hello'):
        st.write('Why hello there')
    else:
        st.write('Goodbye')
    
    title = st.text_input('Movie title', 'Life of Brian')
    if st.button("OK", type="primary"):

        st.write('The current movie title is', title)
    
    st.table(data_users)
if __name__=='__main__':
    main()
