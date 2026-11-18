import streamlit as st


new_chat = st.Page(
    page="pages/new_chat.py",
    title="New chat",
    icon="✨"
)


search = st.Page(
    page="pages/search.py",
    title="Search",
    icon="🔍"
)

recent = st.Page(
    page="pages/recent.py",
    title="Recent",
    icon="💬"
)

activity = st.Page(
    page="pages/activity.py",
    title="Activity",
    icon="🕘"
)

help_page = st.Page(
    page="pages/help.py",
    title="Help",
    icon="❓"
)

settings = st.Page(
    page="pages/settings.py",
    title="Settings",
    icon="⚙️"
)

account = st.Page(
    page="pages/account.py",
    title="Account",
    icon="👤"
)


pg = st.navigation({
    "Gemini": [new_chat, search, recent],
    "": [activity, help_page, settings, account]
})




pg.run()