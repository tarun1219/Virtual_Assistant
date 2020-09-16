







import wikipedia
import wolframalpha
while True:
    my_input("Q  ")

    try:
        #wolframalpha
        app_id="R5QG8R-72PKG3G4XL"

        client=wolframalpha.Client(app_id)

        res= client.query(input)
        answer=next(res.results).text

        print (answer)

    except:
        #wikipedia
        #wikipedia.set_lang("hi")
        print (wikipedia.summary(my_input,sentences=2))
        

































    









