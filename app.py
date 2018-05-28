from flask import Flask ,jsonify ,request,render_template, Response

app = Flask(__name__)
import os
from synthesizer import Synthesizer



@app.route("/",methods=["GET"])
def home():
    return render_template('index.html')


@app.route("/synthesize",methods=["GET"])
def synthesize():
  if not request.args.get('text'):
    return {},400
  return Response(
    synthesizer.synthesize(request.args.get('text')),
    headers={
      'content_type' : 'audio/wav'
    }
  )


synthesizer = Synthesizer()
filedir = os.path.dirname(__file__)
checkpoint = os.path.join(filedir,'model_checkpoint/model.ckpt')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
synthesizer.load(checkpoint)

if __name__ == '__main__':
  Flask.run(app)

