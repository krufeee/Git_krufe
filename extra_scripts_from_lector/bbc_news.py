def speak(str1):
    from win32com.client import Dispatch
    speaking = Dispatch('SAPI.SpVoice')
    speaking.Speak(str1)


if __name__ == '__main__':
    import requests
    import json

    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
    }
    main_url = "https://newsapi.org/v1/articles"

    res = requests.get(main_url, params=query_params)
    load = json.loads(res.text)
    speak('Here you listen top BBC news from Kolio. Lets began')
    speak('first news')
    number_of_news = 5
    for i in range(number_of_news):
        print(load['articles'][i]['title'])
        speak(load['articles'][i]['title'])
        if i < number_of_news - 1:
            speak('next news')
        else:
            speak('end of the news')
