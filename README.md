# Enhance Q&A Chatbot with OpenAI
A simple chatbot application that lets users interact with OpenAI’s language model in real time. The user can select a model, adjust parameters like temperature and max tokens, and must supply their own OpenAI API key.

## Features
- Ask any question and get an answer from an OpenAI model.
- Adjustable temperature for creative or precise answers.
- Flexible token limit for controlling response length.
- User-provided OpenAI API key to keep secrets secure

## Demo
Access the deployed app here: [Enhance Q&A Chatbot with OpenAI](https://enhance-q-a-chatbot-with-openai-jjgmcesiyfu7w8zgllkyyh.streamlit.app/).

## **Below is a demonstration of the app's interface:**
![image](https://github.com/user-attachments/assets/1bdd262f-b76e-4768-9e8f-3afd9e06221b)

## Requirements
- Python 3.7+
- OpenAI API Key

## Getting Started

1. Clone this repository
   ``` bash
    git clone https://github.com/<your-username>/Enhance-QA-chatbot-with-OpenAI.git
    cd Enhance-QA-chatbot-with-OpenAI

   ```
2. Create and activate a virtual environment (optional but recommended)
   ``` bash
    # On macOS/Linux
    python3 -m venv env
    source env/bin/activate
    
    # On Windows
    python -m venv env
    env\Scripts\activate

   ```

3. Install dependencies
   ``` bash
   pip install -r requirements.txt

   ```

4. Run the Streamlit app
   ``` bash
    streamlit run app.py
   ```
5. Open your browser
 - After running the above command, Streamlit will provide a local URL (something like http://localhost:8501).
 - Open that link in your web browser.
6. Enter your API key
 - The interface will prompt you for your OpenAI API key. Paste your key in the input box.
 - You can then choose your preferred OpenAI model, temperature, and max tokens.
7. Ask your question
 - Type any question or prompt into the text box (e.g., “Write a poem about Nigeria”) and hit Enter.
 - The chatbot will respond using OpenAI’s API.

``` bash
Enhance-QA-chatbot-with-OpenAI/
├── OpenAI_chatbot/
│   └── ...
├── app.py
├── requirements.txt
└── README.md

```

- app.py – The main Streamlit app script.
- requirements.txt – Python dependencies needed to run the chatbot.
- OpenAI_chatbot/ – (Optional) Additional module folder or scripts (if present).

## Customization
- Modify app.py to adjust the default temperature, token limit, or UI layout.
- Update the UI elements in Streamlit (sliders, text inputs, etc.) to suit your needs.


## Contributing
 Contributions are welcome! If you’d like to add features or fix bugs:
 1. Fork the repository.
 2. Create a new branch for your changes.
 3. Submit a pull request describing your updates.

## License
This project is licensed under the MIT License (or whichever license you choose).

## Contact
If you have questions or feedback, feel free to open an issue or reach out to the repository owner.
