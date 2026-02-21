import streamlit as st
import json
import os
import urllib.parse
from google import genai

# --- 1. CORE SETTINGS ---
API_KEY = "use api_key here " 
MY_WHATSAPP = "add your whatsapp number here" 
ADMIN_PASSWORD = "add your admin_password here "


client = genai.Client(api_key=API_KEY)

# --- 2. PREMIUM UI DESIGN (CSS) ---
st.set_page_config(page_title="Gadget Buddy | Liberty Market", page_icon="🤖", layout="wide")

st.markdown(f"""
    <style>
    /* Main Background */
    .stApp {{
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }}
    
    /* Center the Login Card */
    .auth-card {{
        background: white;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        max-width: 600px;
        margin: auto;
        border: 1px solid #e1e4e8;
    }}
    
    /* Buttons Styling */
    .stButton > button {{
        background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
        color: white;
        border: none;
        padding: 12px 20px;
        border-radius: 12px;
        font-weight: bold;
        transition: 0.3s;
    }}
    
    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }}

    /* Chat Styling */
    .stChatMessage {{
        background-color: white !important;
        border-radius: 15px !important;
        border: 1px solid #eaeaea !important;
        margin-bottom: 10px !important;
    }}

    /* WhatsApp Button */
    .wa-link {{
        display: inline-flex;
        align-items: center;
        background-color: #25D366;
        color: white !important;
        padding: 10px 20px;
        border-radius: 30px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGIC FUNCTIONS ---
def get_ai_response(user_query, inventory_context):
    system_instruction = (
        "You are 'Gadget Buddy', the premium tech consultant at Liberty Market. "
        "Provide expert, concise, and professional advice using the inventory. "
        f"INVENTORY:\n{inventory_context}"
    )
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{system_instruction}\n\nCustomer: {user_query}"
        )
        return response.text
    except:
        return "System is busy. Please try again."

# --- 4. SECURE SIDEBAR (ADMIN ONLY) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=100)
    st.title("Admin Hub")
    st.markdown("---")
    
    admin_auth = st.expander("🔒 Owner Access")
    with admin_auth:
        key = st.text_input("Admin Password", type="password")
        if key == ADMIN_PASSWORD:
            st.success("Authenticated")
            if os.path.exists("data/info.txt"):
                with open("data/info.txt", "r") as f:
                    content = f.read()
                new_content = st.text_area("Live Stock Editor", content, height=300)
                if st.button("Update Stock"):
                    with open("data/info.txt", "w") as f:
                        f.write(new_content)
                    st.toast("Stock Updated Successfully!")
        elif key != "":
            st.error("Invalid Key")

# --- 5. PROFESSIONAL ACCESS GATE (REGISTRATION) ---
if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False

if not st.session_state.is_logged_in:
    st.markdown("<br><br>", unsafe_allow_html=True)
    cols = st.columns([1, 2, 1])
    with cols[1]:
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        st.title("🤖 Gadget Buddy")
        st.subheader("Professional Tech Consultant")
        st.write("Please enter your details to unlock live inventory & expert chat.")
        
        name = st.text_input("Full Name", placeholder="e.g. " \
        "John Doe")
        phone = st.text_input("WhatsApp Number", placeholder="e.g. 92xxxxxxxxx")
        
        if st.button("Unlock Expert Chat"):
            if name and phone:
                st.session_state.name = name
                st.session_state.phone = phone
                st.session_state.is_logged_in = True
                # Save customer lead
                if not os.path.exists("data"): os.makedirs("data")
                with open("data/leads.txt", "a") as f:
                    f.write(f"Customer: {name} | Phone: {phone}\n")
                st.rerun()
            else:
                st.error("Fields cannot be empty!")
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- 6. CHAT INTERFACE ---
st.title("Expert Consultation")
st.caption(f"Member: {st.session_state.name} | Status: Active ✅")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": f"Hello {st.session_state.name}, welcome to Gadget Buddy Liberty Market. How can I help you with our premium stock?"}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input := st.chat_input("Inquire about prices or ask for owner..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Load Inventory Data
    inv = ""
    if os.path.exists("data/info.txt"):
        with open("data/info.txt", "r") as f: inv = f.read()

    with st.spinner("Analyzing Stock..."):
        answer = get_ai_response(user_input, inv)

    with st.chat_message("assistant"):
        st.markdown(answer)
        
        # WhatsApp Trigger
        trigger_words = ["owner", "contact", "whatsapp", "call", "baat", "number", "connect"]
        if any(w in user_input.lower() for w in trigger_words):
            msg = f"Inquiry from {st.session_state.name} ({st.session_state.phone}): {user_input}"
            url = f"https://wa.me/{MY_WHATSAPP}?text={urllib.parse.quote(msg)}"
            st.markdown(f'<a href="{url}" target="_blank" class="wa-link">📲 Connect with Owner</a>', unsafe_allow_html=True)


    st.session_state.messages.append({"role": "assistant", "content": answer})
