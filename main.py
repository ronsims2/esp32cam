from src import microdot as md

app = md.Microdot()

@app.route('/')
def index(req):
	return 'hello world'
	

app.run(port=80)
