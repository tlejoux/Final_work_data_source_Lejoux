import requests
import json


class JokeRequest:
    url = "https://v2.jokeapi.dev/joke/Any"
    category=""
    flags=""
    joke_type=""
    id=""
    safe_mode=""
    lang="" 
    joke = ""    
    
    @classmethod
    def get_jokes(cls):
        res = requests.get(cls.url)
        res = res.json()

        with open('res.txt', 'w') as outfile:
            json.dump(res, outfile)

        print(res)
        if res['type'] == "twopart":
            print(res["setup"],res["delivery"])
            cls.joke_type = "twopart"
            cls.joke = res["setup"] + res["delivery"]
        if res['type']=="single":
            print(res["joke"])
            cls.joke_type="single"
            cls.joke=res["joke"]
        cls.category=res["category"]
        cls.flags = res["flags"]
        cls.id=res["id"]
        cls.safe=res["safe"]
        cls.lang=res["lang"]
        return res