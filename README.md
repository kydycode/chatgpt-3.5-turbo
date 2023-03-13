# OpenAI Chatbot with gpt-3.5-turbo (ChatCompletion) code-davinci-002 (Codex) models

This is a simple chatbot that uses OpenAI's GPT-3.5-turbo and code-davinci-002 language models to generate responses to user input.

## Installation

1. Clone the repository: `git clone https://github.com/anzz1/chatgpt-cli-python.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Set up an OpenAI API key by following the instructions [here](https://platform.openai.com/account/api-keys)
4. Add your API key to the `YOUR_API_KEY` field in `chat.py` and/or `codex.py`

## Usage

To start the chatbot, run `chat.py` or `codex.py` using Python 3:

    python chat.py


The chatbot will prompt you to enter your input, and then it will generate a response using the GPT-3 or Codex models. The conversation history is stored in a list of dictionaries called `message_log`. Input and output is additionally logged to `chat.log` or `codex.log`

To enter a multiline input mode, type "m".
To finish input, finally type an EOF character (CTRL+D in *nix / CTRL+Z in Windows terminals)

To end the chatbot, type "quit" at any time.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* This chatbot was inspired by the [OpenAI GPT-3 Playground](https://beta.openai.com/playground/)
* The GPT-3 and Codex models are provided by [OpenAI](https://openai.com/)
