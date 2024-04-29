from transformers import pipeline


summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", revision="a4f8f3e")


ARTICLE = """
When I got home from school that day, my grandmother greeted me with a plate of cookies and a worried expression. I hadn't received the scholarship I needed to go to ballet camp, and we'd need to find another way to earn the money. That's when I started my business giving dance lessons to preschoolers, and it's taught me a lot about how to solve problems on my own.
"""

summary = summarizer(ARTICLE, max_length=30, min_length=20, do_sample=False)

print(len(ARTICLE.split(' ')))
print(summary[0]['summary_text'])
print(len(summary[0]['summary_text'].split(' ')))

