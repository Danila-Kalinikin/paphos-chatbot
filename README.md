PAPHOS CITY BOT
Description
This bot provides information about the city of Paphos using APIs from OpenWeather, OpenAI, Bing, and web scraping from the Paphos Life website. It can provide weather updates, news, information on top attractions, and engage in a conversation in English.

Installation

	1.	Clone the repository:
git clone https://github.com/Danila-Kalinikin/paphos-chatbot.git

	2.	Navigate to the project directory:
cd paphos-chatbot

	3.	Set up a virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate

	4.	Install the required libraries:
 pip install -r Libraries.txt
 
	5.	Create a .env file with your API keys for OpenWeather, OpenAI, and Bing:
 OPENWEATHER_API_KEY= 6bd5c36da907fb54cc9fdcddb28af0b9
OPENAI_API_KEY= your_api_key
BING_API_KEY= hz7F7fjntxZeKOpa3Lx9nrozBmhYJqxdK09vy0I1Z_T3BlbkFJkNlVVOXhhvaZh1PU23dwZUMI28zOv7fcZLCrBFMpkA

Usage

Run the bot with the command:

python3 main.py

The bot supports the following commands:

	•	weather — provides current weather in Paphos.
	•	time — shows the current time in Paphos.
	•	news — fetches the latest news from the Paphos Life website.
	•	attractions — gives information about top attractions in Paphos.

Example interaction:

User: What is the weather?
Bot: Weather: clear sky, Temperature: 25°C, Humidity: 60%

Requirements

	•	Python 3.x
	•	Required libraries are listed in Libraries.txt

License

MIT License
You can now add this description in the README.md file on GitHub or via your local repository.
