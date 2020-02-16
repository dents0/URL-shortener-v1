from flask import Flask, render_template, request, Markup
from shorten_url import shorten_url


app = Flask(__name__)
app.secret_key = "<SECRET-KEY>"


# Index page
@app.route('/')
def index():
    return render_template('index.html')


# Shortened URL
@app.route('/short_URL', methods=['GET', 'POST'])
def shorten():
    url = request.form['url']
    
    try:
        shorten_url(url)
        
    except:
        if not url:
            error_msg = "No URL provided. Try again"
            return render_template('index.html', error=error_msg)
        elif "bit.ly" in url or "bitly.is" in url:
            error_msg = Markup("Seems that the URL has already been shortened: <a href='{}'><span class='text-danger'>{}</span></a>").format(url, url)
            return render_template('index.html', error=error_msg)
        error_msg = "Wrong URL format"
        return render_template('index.html', error=error_msg)


    return render_template(
        'short_URL.html',
        url = url,
        result = shorten_url(url)
    )
    

if __name__ == "__main__":
    app.run(debug=True)



