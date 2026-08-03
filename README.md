# Gadget Buddy AI Chatbot

A Streamlit-based chatbot for gadget and electronics retail stores. It uses
the Google Gemini API to answer customer questions with awareness of live
inventory, and pairs that with a secure admin panel for stock management
and a WhatsApp-based lead capture flow for the shop owner.

## What It Does

- Answers customer questions about available gadgets using Gemini,
  grounded in the store's current inventory rather than generic
  knowledge.
- Gives the shop owner a password-protected admin panel to update stock
  levels in real time, without touching code.
- Captures customer details as leads during the conversation.
- Routes interested customers straight to the shop owner over WhatsApp,
  turning a chat conversation into a direct sales contact.

## Features

- **Inventory-aware responses.** The chatbot's answers are grounded in
  the store's actual current stock, not a static or generic product
  catalog.
- **Secure admin panel.** A password-protected interface lets the store
  owner update inventory directly, with changes reflected in the
  chatbot's responses immediately.
- **Customer lead capture.** Visitor details are collected during the
  conversation for follow-up.
- **WhatsApp integration.** Customers can be connected to the shop
  owner directly through WhatsApp for a real, human conversation once
  the chatbot has qualified their interest.

## Tech Stack

| Component | Library | Purpose |
|---|---|---|
| Web interface | Streamlit | Chat UI and admin panel |
| LLM | Google Gemini API (`google-generativeai`) | Generates inventory-aware customer responses |
| Data handling | `json` (standard library) | Reads and writes inventory and lead data |
| System paths | `os` (standard library) | File and environment variable access |
| WhatsApp linking | `urllib.parse` (standard library) | Builds WhatsApp click-to-chat links |

## Requirements

- Python 3.9 or higher
- A Google Gemini API key (free tier available at aistudio.google.com)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SalmaML56/gadget-buddy-ai-chatbot.git
   cd gadget-buddy-ai-chatbot
   ```

2. Install dependencies:
   ```bash
   pip install streamlit google-generativeai
   ```

3. Set your Gemini API key as an environment variable rather than
   hardcoding it in the source file:

   **Windows (PowerShell):**
   ```powershell
   $env:GEMINI_API_KEY="your_key_here"
   ```

   **Mac/Linux:**
   ```bash
   export GEMINI_API_KEY="your_key_here"
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Security Notes

- Never commit an API key or admin password directly into the
  repository. Use environment variables, and keep any `.env` file listed
  in `.gitignore`.
- The admin panel is password-protected - use a strong password, and
  change the default before deploying publicly.
- For a production deployment, set the API key and admin credentials as
  secrets in your hosting platform's settings (for example, Streamlit
  Community Cloud's Secrets manager) rather than as plain environment
  variables on a shared machine.

## Known Limitations

- Inventory updates are managed through the admin panel; there is no
  bulk-import or point-of-sale integration yet, so stock changes made
  outside the app will not be reflected automatically.
- Lead data capture depends on the customer voluntarily providing their
  details during the conversation - there is no verification step.
- WhatsApp integration opens a click-to-chat link; it does not send
  messages automatically or track delivery status.

## Deploying for Free

1. Push this repository to GitHub, with `.gitignore` excluding any file
   containing your API key or admin password.
2. Go to share.streamlit.io and connect the repository.
3. In the app's Settings -> Secrets, add:
   ```
   GEMINI_API_KEY = "your_key_here"
   ```
4. Deploy.
