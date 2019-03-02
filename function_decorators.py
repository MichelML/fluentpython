# import bobo


# @bobo.query('/')
# def hello(person):
#     return 'Hello %s!' % person

# The point is that Bobo introspects the hello function and finds out it needs one parameter named person to work, and it will retrieve a parameter with that name from the request and pass it to hello , so the programmer does not need to touch the request object at all. 
