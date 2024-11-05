from fastipy import Fastipy, Reply, Request

app = Fastipy().cors()

messages = []


def reset():
    global messages
    messages = []


@app.get("/messages")
async def index(_, reply: Reply):
    await reply.send({"messages": messages})


@app.post("/messages")
async def index(request: Request, reply: Reply):
    message = request.body.json.get("message", None)

    if message:
        messages.append(message)
        return await reply.send_code(201)

    await reply.send_code(400)


@app.delete("/messages")
async def index(_, reply: Reply):
    global messages
    messages = []
    await reply.send_code(204)


@app.get("/hello/:name")
async def index(request: Request, reply: Reply):
    name = request.params.get("name", None)
    await reply.send({"message": f"Hello, {name}!"})


@app.get("/hello")
async def index(request: Request, reply: Reply):
    name = request.query.get("name", None)
    await reply.send({"message": f"Hello, {name}!"})


@app.get("/plain-text")
async def index(_: Request, reply: Reply):
    await reply.send("Hello, World!")


@app.get("/html")
async def index(_: Request, reply: Reply):
    await reply.header("Content-Type", "text/html").send("<h1>Hello, World!</h1>")


@app.get("/stream")
async def index(_: Request, reply: Reply):
    message = "Hello, World!"

    async def generator():
        for char in message:
            yield char

    await reply.send(generator())
