# Library Chatbot - LiBO

This project is a simple chatbot designed to help users with common queries related to a library's operations, such as hours, location, membership, borrowing rules, events, and services. The chatbot, named LiBO, uses Natural Language Processing (NLP) techniques to understand and respond to user queries.

## Features

- **Library Information**: Provides information about library hours, location, membership, borrowing rules, events, and services.
- **Natural Language Processing**: Utilizes NLTK (Natural Language Toolkit) for tokenization, stop word removal, and lemmatization to process user inputs.
- **Predefined Responses**: Contains a set of predefined responses for common queries to simulate a conversation.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/library-chatbot.git
    cd library-chatbot
    ```

2. **Create a virtual environment and activate it**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Download necessary NLTK data files**:
    The script includes commands to download necessary NLTK data files:
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('stopwords')
    nltk.download('wordnet')
    ```

## Usage

1. **Run the chatbot**:
    ```sh
    python chatbot.py
    ```

2. **Interact with LiBO**:
    - The chatbot will greet you and ask for your name.
    - You can ask about library hours, location, membership, borrowing rules, events, and services.
    - Type 'exit' to end the conversation.

## Code Overview

- **LibraryChatbot Class**: Contains methods to preprocess user queries and generate appropriate responses.
- **Main Function**: Initializes the chatbot and handles user interactions in a loop.

## Example

```sh
$ python chatbot.py
Hello! I am a library chatbot LiBO. what is your name?
You: John
LIBO: Hi John, I'm here to help you with your library needs.
You can ask about library hours, location, membership, borrowing rules, events, and services.
Type 'exit' to end the conversation.
You: What are the library hours?
LIBO: Our library is open from 9 AM to 9 PM from Monday to Friday, 10 AM to 6 PM on Saturdays, and 12 PM to 5 PM on Sundays.
You: exit
LIBO: Goodbye! Have a great day!

