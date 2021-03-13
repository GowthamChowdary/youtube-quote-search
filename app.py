from flask import Flask,render_template, request
from youtube_transcript_api import YouTubeTranscriptApi

app=Flask(__name__)
@app.route("/res",methods=["POST"])
def index():
    link=request.form.get("link")
    comment=request.form.get("comment")
    a=[]
    b=[]
    try:
        srt=YouTubeTranscriptApi.get_transcript(link)
    except:
        return render_template("nosubtitle.html")    
    for i in srt:
        a.append(i)
    for j in a:
        if comment in j['text']:
            j['start']=int(j['start'])
            b.append(j)
    if len(b)==0:
        return render_template("subtitlenotfound.html")                         
    return render_template("result.html",results=b,url=link,comment=comment)        
@app.route("/")
def welcome():
    return render_template("index.html")
