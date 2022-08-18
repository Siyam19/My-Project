from googletrans import Translator
ts = Translator()
#text = input("Enter Your text: ")
text = "ধন্যবাদ মনজুরুল ভাই"
result = ts.translate(text,dest="en")
print(result.text)
