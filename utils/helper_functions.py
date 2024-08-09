import os
import datetime



def save_conversation(conversation_history, directory="conversation_history"):
    """
    Save a given conversation history to a markdown file with timestamps.
    """
    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Get the current date and time for the filename
    current_datetime = datetime.datetime.now().strftime('%Y_%m_%d_%H%M%S')
    file_path = os.path.join(directory, f"{current_datetime}.md")

    with open(file_path, 'w', encoding='utf-8') as file:
        for message in conversation_history:
            if message["role"] in ["user", "assistant"]:
                message_timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                role_icon = '🧑‍💻' if message["role"] == "user" else '🤖'
                file.write(f"{message_timestamp} **{role_icon} {message['role'].title()}:** {message['content']}\n\n")
    
    return file_path
