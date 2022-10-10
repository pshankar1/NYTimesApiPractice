import requests
API_KEY="8tV1oij0w53ahibfWqxExHPHR0GmhJ6y"
def get_headlines(query):
    response=requests.get(
        "https://api.nytimes.com/svc/search/v2/articlesearch.json"f"?q=election&api-key={API_KEY}",
        params={"q":query,"api-key":API_KEY}

    )
    response_json=response.json()
    #first_headline=response_json["response"]["docs"][0]["headline"]["main"]
    #print(first_headline)
    headlines=[]
    for doc in response_json["response"]["docs"]:
        headlines.append(doc["headline"]["main"])
        #print(doc["headline"]["main"])
        return headlines
