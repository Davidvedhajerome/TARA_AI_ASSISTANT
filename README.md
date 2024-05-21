
## Tara: Your Personal AI Assistant
• Abstract: 
      Tara stands as a groundbreaking AI assistant meticulously crafted to elevate  daily productivity through seamless voice interaction and automation. At its core,  Tara harnesses cutting-edge AI technologies and Python libraries to execute an extensive array of tasks. These encompass managing emails, navigating the web, system administration, and delivering real-time updates on weather, news, and beyond. By exemplifying how AI can seamlessly integrate into everyday life, this project demonstrates the potential of Tara as a reliable, efficient, and indispensable personal assistant.

pyttsx3 falls under the category of Natural Language Processing (NLP) in the broader field of Artificial Intelligence (AI).
Natural Language Processing involves the interaction between computers and human (natural) languages. In the case of pyttsx3, it is specifically concerned with the generation of human-like speech from text. This process typically involves the use of machine learning algorithms and linguistic rules to convert written text into spoken words, mimicking the way humans speak.
Within NLP, text-to-speech (TTS) conversion is an important area that enables various applications such as virtual assistants, accessibility tools for visually impaired individuals, language learning platforms, and more.
So, while pyttsx3 itself is not an AI algorithm, it provides a useful tool for developers working in the field of NLP to incorporate speech synthesis capabilities into their AI applications.

## System Requirements:
  # 1.Hardware Requirements:
  •	Processor: Intel Core i5 or equivalent
  •	RAM: Minimum 4 GB (8 GB recommended)
  •	Storage: At least 500 MB of free disk space
  •	Microphone: For voice command input
  •	Speakers: For audio output
  
  # 2.Software Requirements:
  •	Operating System: Windows 10 or later
  •	Python: Version 3.7 or later
  •	Internet Connection: Required for web-based functionalities like email, weather updates, and news retrieval.
  
  # 3.Tools and Versions:
  •	Python: Version 3.7+
  •	pyttsx3: 2.90
  •	datetime: Standard Python library
  •	speech_recognition: 3.8.1
  •	wikipedia: 1.4.0
  •	smtplib: StSetup and Installation
  
  # 4.Features
  • Text-to-Speech: Converts text responses to speech.
  • Speech Recognition: Takes voice commands from the user.
  • Weather Updates: Provides weather information for a specified city.
  • News Updates: Fetches top news headlines.
  • CPU and Battery Status: Reports the current CPU usage and battery status.
  • Jokes: Tells a random joke.
  • Wikipedia Search: Retrieves summary information from Wikipedia.
  • Web Browser Control: Opens websites and performs searches in the default web browser.
  • Screenshot: Takes a screenshot and saves it to a specified location.
  • Music Playback: Plays songs from a specified directory.
  • Memory: Remembers user-provided information.
  • Shutdown and Restart: Can shutdown or restart the system.
  • GUI: Provides a simple GUI for user interaction.
  # 5.Requirements
  • Python 3.x
  # • The following Python libraries:
  • pyttsx3
  • datetime
  • speech_recognition
  • wikipedia
  • webbrowser
  • os
  • pyautogui
  • psutil
  • pyjokes
  • requests
  • json
  • tkinter
  • PIL (Pillow)
  • threading

## Setup and Installation
# 1.Clone the Repository

  # bash
  • git clone <repository-url>
  • cd tara-assistant
  • Install Required Libraries

# 2. Use the following command to install all required libraries:
# bash
  • pip install pyttsx3 speechrecognition wikipedia pyautogui psutil pyjokes requests pillow

# 3. Update API Key
# • Replace the placeholders with your actual API keys in the code:
  • OpenWeatherMap API key in the weather function.
  • NewsAPI key in the get_news function.

## Usage
  # 1.Run the Application
  
  • Execute the main script:
 • python tara_assistant.py

# 2.Interact with Tara
  • Speech Mode: Use your microphone to give voice commands.
  • Text Mode: Type your queries into the text entry field and press "Enter" or click the "Start" button.

# 3.Commands
• Time: "What is the time?"
• Date: "What is the date today?"
• Weather: "What is the weather in [city]?"
• News: "Give me the news."
• Jokes: "Tell me a joke."
• CPU Status: "What is the CPU usage?"
• Screenshot: "Take a screenshot."
• Wikipedia Search: "Search [topic] on Wikipedia."
• Web Browser: "Open [website] in Chrome" or "Search [query] in Chrome."
• Memory: "Remember [something]" and "Do you know [something]?"
• Music Playback: "Play songs."
• Shutdown/Restart: "Shutdown the system" or "Restart the system."

## GUI Components
• Microphone Icon: Displays a microphone icon.
• Mode Selection: Radio buttons to switch between "Speech Mode" and "Text Mode."
• Query Entry: A text entry field for typing queries.
• Start Button: A button to start processing the input.
• Output Display: A scrolled text area to display the assistant's responses.

## Additional Notes
• Ensure your microphone is working correctly for speech recognition.
• Make sure the specified paths (e.g., for saving screenshots) exist on your system.
• The assistant will greet you and offer its services upon startup.

## Contributing
• Contributions are welcome! Feel free to submit a pull request or open an issue if you encounter any bugs or have suggestions for new features.

## Standard Python library
•	webbrowser: Standard Python library
•	os: Standard Python library
•	pyautogui: 0.9.53
•	psutil: 5.9.0
•	pyjokes: 0.6.0
•	requests: 2.25.1
•	json: Standard Python library


