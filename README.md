#LollAPI -- A set of DoStuff/Lollapolooza Python API Bindings

This is a very simple library written to benfit both me, and other members
of the [HackLolla](http://hacklolla.com/) competition. It's a very basic
hacked up set of calls to the DoStuff API.

##Requirements
The only requirement to run, is the amazing [Requests](http://docs.python-requests.org/en/latest/index.html)
which if you dont already have, your doing something wrong.

##Usage
The following is an example usage of the library:

```
import lolla

lolla.api_key = "MY_API_KEY" #The api defaults to the documenation/demo API.
x = lolla.getEvents()['events']['event'][0]
y = lolla.getVenue(x['venue']['id'])
```

##Notes
I tried to document all the functions as best as possible. Therefore its 
possible to run help() on any of the api calls

As far as implementation goes, the method I used (decorators w/ empty functions)
is not the cleanest. This would have worked much better in a object, but for now
it's easy enough to add functions and it keeps a fairly clean look.

##Licensing, etc.
There is none. Open source. Enjoy.