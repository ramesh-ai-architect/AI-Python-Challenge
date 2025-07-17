import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.title("📂 Menu")
        st.radio("Navigate", ["Dashboard", "Settings"])
        theme = st.radio("🎨 Theme", ["Light", "Dark"])
        st.session_state["theme"] = theme
        st.markdown("""
            <style>
                .sidebar .sidebar-content { width: 250px; }
                body { background-color: #111 if theme == "Dark" else "#fff"; }
            </style>
        """, unsafe_allow_html=True)