from flask import Flask, render_template
from datetime import datetime

#Instance of the class Flask in which the argument it takes is the name of the application's module, i.e. '__name__'.
app = Flask(__name__)

#If the user directs to http://127.0.0.1:5000/clocks.html the function below will execute.
@app.route('/<template>')
def showTime(template):
    """Generates the server current time and calls the render_template function.
    
    The render_tempelate function renders a template from the template folder found in the application folder. The name     of the template is passed to the function, as well as any context (variables) used by the template itself. 
    In this case, the template is 'clocks.html' and the context is the generated server time.
    
    Parameters:
    argument1 (string): Name of the template (in the aplications folder, 'templates') to load.

    Returns:
    template: Rendered template. 
    """
    remoteTime = datetime.now().strftime('%H:%M:%S')
    return render_template(template, remoteTime=remoteTime)
