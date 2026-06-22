import streamlit as st

from workflows.startup import StartupWorkflow

workflow = StartupWorkflow()

st.set_page_config(
    page_title="StartupGPT",
    layout="wide"
)

st.title("🚀 StartupGPT")

idea = st.text_area(
    "Describe your startup idea",
    height=200
)

if st.button("Generate"):

    with st.spinner("Generating..."):

        result = workflow.run(idea)

        tab1, tab2, tab3, tab4 = st.tabs([
            "PRD",
            "UI",
            "Backend",
            "Database"
        ])

        with tab1:
            st.markdown(result["prd"])

        with tab2:
            st.markdown(result["ui"])

        with tab3:
            st.code(result["backend"])

        with tab4:
            st.code(result["schema"])
