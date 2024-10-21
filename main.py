import openai
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from datetime import datetime
import pytz

# Load API keys from .env file
load_dotenv()
openweather_api_key = os.getenv('OPENWEATHER_API_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')
bing_api_key = os.getenv('BING_API_KEY')
print(f"OpenWeather API key loaded: {openweather_api_key}")
print(f"OpenAI API key loaded: {openai_api_key}")
print(f"Bing API key loaded: {bing_api_key}")
openai.api_key = openai_api_key

# Function to get current weather in Paphos
def get_current_weather():
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather"
        params = {
            'id': 146214,  # City ID for Paphos
            'appid': openweather_api_key,
            'units': 'metric'
        }
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        return f"Weather: {weather_description}, Temperature: {temperature}°C, Humidity: {humidity}%"
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to fetch weather data ({e})"

# Function to get time in Paphos
def get_paphos_time():
    timezone = pytz.timezone('Asia/Nicosia')  # Timezone for Paphos
    paphos_time = datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')
    return f"The current time in Paphos is {paphos_time}."

# Function to get latest news from Paphos Life
def get_latest_news():
    try:
        url = "https://www.paphoslife.com/"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('div', class_='thumbnails thumbnail-style thumbnail-kenburn')
        news_list = []
        for article in articles[:5]:  # Limit to top 5 news items
            title = article.find('h3').get_text(strip=True)
            link = article.find('a')['href']
            news_list.append(f"{title} - https://www.paphoslife.com{link}")
        if news_list:
            return news_list
        else:
            return ["No news available at the moment."]
    except requests.exceptions.RequestException as e:
        return [f"Error fetching news: {e}"]

# Function to get top attractions in Paphos using Bing Search API
def get_attractions():
    try:
        search_url = "https://api.bing.microsoft.com/v7.0/search"
        headers = {"Ocp-Apim-Subscription-Key": bing_api_key}
        params = {"q": "top attractions in Paphos"}
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()
        attractions_list = []
        for result in search_results['webPages']['value'][:5]:
            title = result['name']
            link = result['url']
            attractions_list.append(f"{title} - {link}")
        return attractions_list
    except requests.exceptions.RequestException as e:
        return [f"Error fetching attractions: {e}"]

# Function to generate conversation responses using OpenAI API
def generate_conversation_response(user_input, conversation_history):
    prompt = f"User: {user_input}\nBot: "
    conversation_history.append(prompt)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Обновите на доступную модель
        messages=[{"role": "system", "content": "You are a helpful assistant."}] + [{"role": "user", "content": prompt}],
        max_tokens=100,
        temperature=0.7
    )
    bot_reply = response['choices'][0]['message']['content'].strip()
    conversation_history.append(f"Bot: {bot_reply}")
    return bot_reply

# Chatbot logic with conversation handling
def chatbot():
    print("Welcome to the Paphos City Information Bot! Type 'exit' to quit.")
    conversation_history = []

    while True:
        user_input = input("User: ")
        if user_input.lower() == 'exit':
            print("Bot: Goodbye!")
            break
        elif "weather" in user_input.lower():
            weather_info = get_current_weather()
            print(f"Bot: {weather_info}")
        elif "time" in user_input.lower():
            time_info = get_paphos_time()
            print(f"Bot: {time_info}")
        elif "news" in user_input.lower():
            news = get_latest_news()
            print("Bot: Here are the latest news headlines from Paphos:")
            for item in news:
                print(f"- {item}")
        elif "attractions" in user_input.lower():
            attractions = get_attractions()
            print("Bot: Here are some links about top attractions in Paphos:")
            for item in attractions:
                print(f"- {item}")
        else:
            # Use OpenAI to continue conversation
            response = generate_conversation_response(user_input, conversation_history)
            print(f"Bot: {response}")

# Run the chatbot
if __name__ == '__main__':
    chatbot()