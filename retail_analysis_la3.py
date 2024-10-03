import streamlit as st

# Set the title of your app
st.title("Retail Analysis Dashboard By 24MAI0091 LAB 03 ASSIGNMENT..")

# Embed the Power BI dashboard using an iframe
st.components.v1.iframe("https://app.powerbi.com/reportEmbed?reportId=dc6c3b64-3db7-4504-b0e9-9302f377137d&autoAuth=true&ctid=d4963ce2-af94-4122-95a9-644e8b01624d", width=940, height=541)
