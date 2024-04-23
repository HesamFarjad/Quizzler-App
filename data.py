import requests
import pandas

PARAMETERS = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=PARAMETERS)
response.raise_for_status()
data = response.json()

# question_data = pandas.DataFrame(data['results'])
question_data = data['results']
# print(question_data)

# questions = df['question']
# print(questions)
