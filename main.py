from language_processing import maruti
from task_management import task_manager
from calculator import calculator
from weather import weather
from news import news

# Example usage
if __name__ == "__main__":
    print("Maruti AI")

    # Language Processing
    maruti.analyze_text("OpenAI is located in San Francisco.")

    # Task Management
    task_manager.add_task("Complete AI project")
    task_manager.view_tasks()

    # Calculator
    print(calculator.add(5, 3))

    # Weather
    print(weather.get_weather("New York"))

    # News
    print(news.get_news())
