import openai

# Set up OpenAI API key
api_key = "YOUR_API_KEY"
openai.api_key = api_key

# Function to send a message to the OpenAI chatbot model and return its response
def send_message(message_log):
    # Use OpenAI's ChatCompletion API to get the chatbot's response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # The name of the OpenAI chatbot model to use
        messages=message_log,   # The conversation history up to this point, as a list of dictionaries
        max_tokens=3800,        # The maximum number of tokens (words or subwords) in the generated response
        stop=None,              # The stopping sequence for the generated response, if any (not used here)
        temperature=0.7,        # The "creativity" of the generated response (higher temperature = more creative)
    )

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

    # Set a flag to keep track of whether this is the first request in the conversation
    first_request = True

    # Start a loop that runs until the user types "quit"
    while True:
        if first_request:
            # If this is the first request, get the user's input and add it to the conversation history
            user_input = input("You: ")
            message_log.append({"role": "user", "content": user_input})

            # Add a message from the chatbot to the conversation history
            message_log.append({"role": "assistant", "content": "You are a helpful assistant."})

            # Send the conversation history to the chatbot and get its response
            response = send_message(message_log)

            # Add the chatbot's response to the conversation history and print it to the console
            message_log.append({"role": "assistant", "content": response})
            print(f"AI assistant: {response}")

            # Set the flag to False so that this branch is not executed again
            first_request = False
        else:
            # If this is not the first request, get the user's input and add it to the conversation history
            user_input = input("You: ")

            # If the user types "quit", end the loop and print a goodbye message
            if user_input.lower() == "quit":
                print("Goodbye!")
                break

            message_log.append({"role": "user", "content": user_input})

            # Send the conversation history to the chatbot and get its response
            response = send_message(message_log)

            # Add the chatbot's response to the conversation history and print it to the console
            message_log.append({"role": "assistant", "content": response})
            print(f"AI assistant: {response}")


# Call the main function if this file is executed directly (not imported as a module)
if __name__ == "__main__":
    main()
