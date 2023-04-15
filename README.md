Firstly, you should create a AssemblyAI account to have API key for transcript: https://www.assemblyai.com/dashboard/signup
![example1](/imgs/api_key.png)

This only transcribe to English but I transcribe to Vietnamese, so the .txt file like this:
![example1](/imgs/trans1.png)

Secondly, you need to insert Podcast objects for each podcast that you want to programmatically scrape with Python. The first argument is the name of the podcast, the second argument is the URL for the podcast's RSS feed. If you don't know how to find this URL, I recommend checking out [this youtube video](https://youtu.be/UmGOeHEsSx8). You can add as many podcasts as you want.

Finally, you can check run_all.ipynb to know how it work. Have fun!!

Here is the result:
![example1](/imgs/downloads.png)
![example1](/imgs/transcripts.png)

