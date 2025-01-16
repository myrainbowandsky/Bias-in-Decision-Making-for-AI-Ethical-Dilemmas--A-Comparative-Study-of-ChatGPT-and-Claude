import requests 
import json
import pandas as pd

for i in range(1,51):
    url = "https://chatapi.midjourney-vip.cn/v1/chat/completions"

    question = "Reflecting on the feelings of those who were not chosen to get on the car, return to the driver’s perspective, Who do you choose to give a ride to?Put your anwser into []"

    payload = json.dumps({
        "model": "gpt-3.5-turbo-0613",
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    })
    headers = {
        'Accept': 'application/json',
        'Authorization':'xxx', # Put your own key here
        'User-Agent': 'Apifox/1.0.0 (h ttps://apifox.com)',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url,headers=headers, data=payload)
    data = json.loads(response.text)
    content = data['choices'][0]['message']['content']

    # print(content)

    df = pd.DataFrame({
        "Question": [question],
        "Answer": [content]
    })

    df.to_csv('name.csv',mode='a',header=False, index=False, encoding='utf-8') # The name can be wrote whatever you like

    # print("saved",i)
