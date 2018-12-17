import wolframalpha
import wikipedia



wikipedia.set_lang("es")
while True:
    input = raw_input("Question: ")

    try:
        #wolframalpha
        app_id = "QXYG8Q-QPW5T7LV57"
        client = wolframalpha.Client(app_id)
        res = client.query(input)
        answer = next(res.results).text
        print answer
    except:
        #wikipedia
        print  wikipedia.summary(input)
