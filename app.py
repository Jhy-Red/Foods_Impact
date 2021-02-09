from flask import Flask, render_template, request, url_for, Response
import ressources.video_tools as vt

app = Flask(__name__,static_url_path='/static')

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/camera')
def webcamisation():
    return Response(vt.webcam(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/images')
def pictures():
    return render_template('from_pictures.html')

if __name__ == "__main__":
    app.run(debug=True)
    