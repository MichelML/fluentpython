# The goal of Command is to decouple an object
# that invokes an operation (the Invoker) 
# from the provider object that implements 
# it (the Receiver). In the example from Design 
# Patterns , each invoker is a menu item in a 
# graphical application, and the receivers are the document being edited or the application itself. 

class MacroCommand:
  """A command that executes a list of commands"""
  def __init__(self, commands):
    self.commands = list(commands)

  def __call__(self):
    for command in self.commands:
      command()

  