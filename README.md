Gadget Buddy AI Chatbot is a Streamlit-based web application for gadget and electronics stores.
It uses the Google Gemini API to provide intelligent, inventory-aware responses to customer queries.
The application includes a secure admin panel for live stock updates, customer registration for lead generation, and WhatsApp integration for direct communication with the shop owner.
Required Libraries

The following Python libraries are required to run this project:

External Libraries (Must Install)
streamlit
google-generativeai
Standard Python Libraries (No Installation Required)

These libraries are included with Python by default:

json

os

urllib.parse
Installation Instructions

Clone the repository:

git clone https://github.com/your-username/gadget-buddy-ai-chatbot.git
Navigate to the project directory:

cd gadget-buddy-ai-chatbot
Install the required libraries:

pip install streamlit google-generativeai

Add your Google Gemini API key in the code or as an environment variable.
streamlit run app.py
Run the application:
Python 3.9 or higher is recommended.

Do not expose API keys or admin passwords in public repositories.

Use environment variables for production deployment.
