import reflex as start
from blocknew.componets.one import one

class State (start.State):
    pass 



def index():
    return start.hstack(
        one())

app = start.App()
app.add_page(index) 
app._compile()
