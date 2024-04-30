from deepmultilingualpunctuation import PunctuationModel

def punctuator(text):
    model = PunctuationModel()
    # text = "hey there how are you doing so i wanted to tell you how amazing you are by the way will you go out with me"
    result = model.restore_punctuation(text)
    # print(result)
    return result