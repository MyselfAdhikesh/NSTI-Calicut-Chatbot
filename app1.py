# app.py

import streamlit as st
from chatbot import get_answer

# --- Page Config ---
st.set_page_config(
    page_title="NSTI Calicut Chatbot",
    page_icon="🎓",
    layout="wide"
)

# --- Color Constants ---
PRIMARY_COLOR = "#B8E3E9"   
ACCENT_COLOR = "#93B1B5"    
TEXT_COLOR = "#4F7C82"      
BG_COLOR = "#0B2E33"       






# --- Sidebar ---
with st.sidebar:
    st.image("nsti_logo.jpg", use_container_width=True)

    st.markdown(f"""
        <div style="color: {PRIMARY_COLOR};">
            <h2>NSTI Calicut</h2>
            <p style="font-size: 14px;">National Skill Training Institute</p>
            <p>📍 Kerala, India</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)

    st.markdown(f"<h4 style='color: {ACCENT_COLOR};'>💬 Select a Section</h4>", unsafe_allow_html=True)
    category = st.radio(
        "",
        ["General", "Admissions", "Courses", "Fees", "Facilities"],
        index=0
    )

    st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)

    st.markdown(f"""
        <h4 style='color: {ACCENT_COLOR};'>📞 Need Help?</h4>
        <a href="https://nsticalicut.dgt.gov.in/" target="_blank">Visit Official Site</a>
        <p style="font-size: 12px; color: grey;">Developed by an NSTI Calicut student.</p>
    """, unsafe_allow_html=True)

# --- Header ---
st.markdown(f"""
    <div style="text-align: center; padding: 10px 0;">
        <h1 style="color: {PRIMARY_COLOR}; margin-bottom: 6px;">NSTI Calicut Chatbot</h1>
        <p style="font-size: 17px; color: {ACCENT_COLOR};">Ask anything about courses, admissions, campus life, and more</p>
    </div>
""", unsafe_allow_html=True)

st.markdown(f"<hr style='border: 1px solid {ACCENT_COLOR};'>", unsafe_allow_html=True)

# --- Static Info Area Based on Category ---
category_info = {
    "General": f"""
        <div style="color: {TEXT_COLOR};">
        <b>Welcome to NSTI Calicut!</b><br><br>
        National Skill Training Institute, Calicut is one of the premier national institute under Directorate General of Training , 
        Ministry of Skill Development & Entrepreneurship, Government of India engaged in developing skilled manpower for the industries , 
        Instructional staff for the Industrial Training Institutes & upgrading skill of in-service persons from the industry.
        This exclusive institute  facilitates short term training programme and regular long term training programme in various disciplines.
        Long term courses are conducted in levels such as Craftsmen Training Scheme (CTS), Craft Instructor Training Scheme (CITS) and recently started Advanced Diploma in IT, Networking and Cloud course also. 
        IT, Networking and Cloud course is very much essential in the current scenario due to a lot of demand in software industries where every industry is using cloud as base.
        </div>
    """,
    "Admissions": f"""
        <div style="color: {TEXT_COLOR};">
        <b>Admission Process</b><br><br>
         Obtain the Application Form:<br> Online: Download the application form from the NSTI Calicut website.
         <br>Offline: Collect the application form directly from the NSTI Calicut institute. 
         <br> 2. Fill Out the Application: <br>
         Carefully: Complete the application form accurately and provide all required details.
         <br> Gather Necessary Documents: Ensure you have all the necessary documents and information ready.<br>
           3. Submit the Application:<br>
           Address:Submit the completed application form to the Principal, NSTI, Govindapuram, Calicut- 673601.<br>
           Deadline:Ensure you submit the application before the specified deadline <br>
             4. Payment of Registration Fee:<br>
               Online: For online registration fee payment guidelines, refer to the NSTI Calicut website.<br>
               Offline: You can pay the registration fee directly at the institute. <br>
               5. Other Important Information:<br>
                 CTS Admissions: Check the NSTI Calicut website for the latest information on CTS (ITI) admissions, including how to submit your interest. <br>
                   Registration Fee: A registration fee may be required for processing your application.\n Contact Details: For any further queries, you can contact the institute directly.
        </div>
    """,
    "Courses": f"""
        <div style="color: {TEXT_COLOR};">
        <b>Courses Offered:</b><br>
        • We offer courses like:<br>
        1.CTS SOLAR TECHNICIAN (ELECTRICAL)<br>
        2.Electrician – Power Distribution<br>
        3.CITS Mechanic Refrigeration and Air Conditioning<br>
        4.CITS ELECTRICIAN<br>
        5.AI Programming Assistant Course<br>
        Duration: 1–2 years depending on course
        </div>
    """,
    "Fees": f"""
        <div style="color: {TEXT_COLOR};">
        <b>Fee Structure</b><br><br>
        • The course fee at NSTI Calicut for ITI courses/CTS (Craftsmen Training Scheme) ranges from Rs 1500 to Rs 4200 depending on the course duration (6 months, 1 year, or 2 years). Specific fees for different programs, including Advanced Diploma in IT, Networking & Cloud (ADIT), are also available on the NSTI Calicut website. \n Detailed Fee Structure:\n 6-month courses: Rs 1500 \n 1-year courses: Rs 2400 \n 2-year courses: Rs 4200 \n Fee Concessions: Available for SC/ST categories. \n Tuition and Exam Fee Waivers: Offered for girls. \n ADIT (Advanced Diploma): Fees vary by category (Unreserved/OBC vs. SC/ST) and include registration, admission, tuition, and examination fees. Details can be found on the NSTI Calicut website. \n Other fees: May include caution money, library security, hostel rent, and service charges, depending on the program and whether students are hostellers.
        </div>
    """,
    "Facilities": f"""
        <div style="color: {TEXT_COLOR};">
        <b>Campus Facilities</b><br><br>
        • Hostel with mess<br>
        • Modern computer labs<br>
        • Library and reading rooms<br>
        • Sports ground<br>
        </div>
    """
}

st.markdown(f"<h3 style='color: {ACCENT_COLOR};'>ℹ️ About {category}</h3>", unsafe_allow_html=True)
st.markdown(category_info[category], unsafe_allow_html=True)

st.markdown(f"<hr style='border: 1px solid {ACCENT_COLOR};'>", unsafe_allow_html=True)

# --- Session State ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Chat History Display ---
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(message)

# --- Chat Input ---
user_input = st.chat_input("Ask your question here...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append(("user", user_input))

    context_input = f"[{category}] {user_input}"

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = get_answer(context_input)
            st.markdown(answer)

    st.session_state.chat_history.append(("assistant", answer))

# --- Footer ---
st.markdown(f"""
    <hr style="border: 1px solid {ACCENT_COLOR};">
    <div style="text-align: center; font-size: 13px; color: grey;">
        🤖 Built by Trainees of AIPA 2024-25 Batch <strong>N S T I CALICUT</strong>
    </div>
""", unsafe_allow_html=True)
