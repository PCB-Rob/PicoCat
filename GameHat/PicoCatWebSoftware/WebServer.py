from microdot import Microdot

app = Microdot()

@app.route('/')
def index(request):
    return 'Hello, world!'

print("Go To => 192.168.1.xx:5000")
app.run()