import openai

# Set up OpenAI API key
api_key = "YOUR_API_KEY"
openai.api_key = api_key

# Function to send a message to the OpenAI chatbot model and return its response
def send_message(message_log):
    try:
        # Use OpenAI's ChatCompletion API to get the chatbot's response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # The name of the OpenAI chatbot model to use
            messages=message_log,   # The conversation history up to this point, as a list of dictionaries
            max_tokens=3800,        # The maximum number of tokens (words or subwords) in the generated response
            stop=None,              # The stopping sequence for the generated response, if any (not used here)
            temperature=0.7,        # The "creativity" of the generated response (higher temperature = more creative)
        )
    except (openai.error.APIError, openai.error.InvalidRequestError, openai.error.AuthenticationError) as e:
        return(f"OpenAI API returned an API Error:\n{e}")
    except (openai.error.APIConnectionError, openai.error.Timeout, openai.error.ServiceUnavailableError) as e:
        return(f"Failed to connect to OpenAI API:\n{e}")
    except openai.error.RateLimitError as e:
        return(f"OpenAI API request exceeded rate limit:\n{e}")

    # Find the first response from the chatbot that has text in it (some responses may not have text)
    for choice in response.choices:
        if "text" in choice:
            return choice.text

    # If no response with text is found, return the first response's content (which may be empty)
    return response.choices[0].message.content


# Main function that runs the chatbot
def main():
    # Initialize the conversation history with a message from the chatbot
    message_log = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    print("gpt-3.5-turbo")

    # Start a loop that runs until the user types "quit"
    while True:
        try:
            # If this is not the first request, get the user's input and add it to the conversation history
            user_input = input("\n> ")

            # If the user types "quit", end the loop and print a goodbye message
            if user_input.lower() == "q" or user_input.lower() == "quit" or user_input.lower() == "exit":
                break

            # Log input to file
            f = open("chat.log", "a")
            print(f"\n> {user_input}", file=f)
            f.close()

            # If the user types "m", enter multiline input mode
            if user_input.lower() == "m":
                #print("- Multiline input, to finish CTRL-Z + ENTER")
                lines = []
                while True:
                    try:
                        line = input("| ")
                    except EOFError:
                        break
                    f = open("chat.log", "a")
                    print(f"| {line}", file=f)
                    f.close()
                    lines.append(line)
                user_input = '\n'.join(lines)

            message_log.append({"role": "user", "content": user_input})

            # Send the conversation history to the chatbot and get its response
            response = send_message(message_log)

            # Add the chatbot's response to the conversation history, print it to the console and log to file
            message_log.append({"role": "assistant", "content": response})
            print(f"\n{response}")
            f = open("chat.log", "a")
            print(f"\n{response}", file=f)
            f.close()
        except KeyboardInterrupt:
            break

    print("\nGoodbye!")


# Call the main function if this file is executed directly (not imported as a module)
if __name__ == "__main__":
    main()
