#Step 1: Header First (text elements)
import streamlit as st 
st.title("Course Management")
st.header("Course Management Dashboard")
st.caption("MISY350")
st.divider()

#Step 2: Define Assignments List (data Continuity)
assignments = [
    {
        "id" : "HW1",
        "title" : "Introduction to Database",
        "description" : "Basics of database design",
        "points" : 100,
        "type" : "homework"
    },
    {
        "id" : "HW2",
        "title" : "Normalization",
        "description" : "Normalize the table designs",
        "points" : 100,
        "type" : "lab"
    }
]

#Step 3: Add New Assignment Section (Inputs & Layout)
st.subheader("Add New Assignment")
with st.container(border=True):
    col1, col2 = st.columns([2,1])

    with col1:
        with st.container(border=True):
            st.markdown("### Assignment Details")
            title = st.text_input("Assignment Title", placeholder="homework")
            description = st.text_input("Assignment Description")
            points = st.number_input("Points")
    with col2:
        st.markdown("**Time and Type**")
        due_date = st.date_input("Due Date")
        type = st.radio("Type",["Homework","Lab"])


                                    
#Add New assignment 
st.markdown("# Add New Assignment")

#input
title = st.text_input("Title", placeholder = "ex. Homework 1", 
                      help = "This is the name of the assignment")
description = st.text_area("Description", placeholder = "ex. Database Design...")
due_date = st.date_input("Due Date")
assignments_type = st.radio("Type", ["Homework", "Lab"])
#assignments_type2 = st.selectbox("Type", ["Homework", "Lab", "Other"])
#if assignments_type2 == "Other":
#    assignments_type2 = st.text_input("Assignment Type")

#lab = st.checkbox("Lab")

with st.expander("Assignment Preview", expanded=True):
    st.markdown("## Live Preview")
    st.markdown(f"Title: {title}")

btn_save = st.button("Save", width="stretch")
if btn_save:
    st.warning("Working on it!")    
