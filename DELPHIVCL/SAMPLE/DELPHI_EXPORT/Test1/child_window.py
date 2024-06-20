import os
from delphifmx import *

class Child_Form(Form):

    def __init__(self, owner):
        self.child_heading = None
        self.result_text_heading = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "child_window.pyfmx"))

def main():
    Application.Initialize()
    Application.Title = 'Child Window'
    Application.MainForm = Child_Form(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()
