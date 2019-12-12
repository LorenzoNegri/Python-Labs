```python
# creating a class Car with parameters like make, model and color
class Car(object):
    def __init__(self,make,model,color):
        self.make=make;
        self.model=model;
        self.color=color;
        self.owner_number=0 
    def car_info(self):
        print("make: ",self.make)
        print("model:", self.model)
        print("color:",self.color)
        print("number of owners:",self.owner_number)
    def sell(self):
        self.owner_number=self.owner_number+1
```

Now let's create a <code> Car </code> object my_car with some data attributes for "make", "model" and "color": 


```python
my_car=Car("BMW","M3","red") 
```

Using the method car_info() we can print out the data attributes as we specified in the class code


```python
my_car.car_info()
```

    make:  BMW
    model: M3
    color: red
    number of owners: 0


We can call and use the method <code> sell() </code> in a loop to populate SELL, then call the method <code> car_info()</code> again 


```python
for i in range(10):
    my_car.sell()
# in the class structure we find: self.owner_number=self.owner_number+1
    
my_car.car_info() 
```

    make:  BMW
    model: M3
    color: red
    number of owners: 10


We use class has a structure or a record. We can create an instance of the class later on in the code:


```python
class Circle:
    pass

my_circle = Circle()
my_circle.radius = 5
print(2*3.14 * my_circle.radius)
```

    31.400000000000002



```python
# creating circles with default radius = 1
class Circle:
    def __init__(self):
        self.radius = 1

my_circle = Circle()
print(2*3.14 * my_circle.radius)
```

    6.28



```python
# we can change radius on the fly
my_circle.radius = 5
print(2*3.14 * my_circle.radius)
```

    31.400000000000002



```python
# creating a new method "area"
class Circle:
    def __init__(self):
        self.radius = 1
    def area(self):
        return self.radius * self.radius * 3.14159

c = Circle()
c.radius = 3
print(c.area())
```

    28.27431



```python
# adding a parameter to che __init__ 
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius * self.radius * 3.14159
    
c = Circle(5) # we give the radius paramater the value 5
print(c.area())
```

    78.53975



```python
# adding a parameter to che __init__ with default value 
class Circle:
    def __init__(self, radius=1):
        self.radius = radius
    def area(self):
        return self.radius * self.radius * 3.14159
    
c = Circle() # we leave default
print(c.area())
c = Circle(3) # we give a value
print(c.area())
```

    3.14159
    28.27431



```python
# defining a class variable
class Circle:
    pi = 3.14159
    def __init__(self, radius=1):
        self.radius = radius
    def area(self):
        return self.radius * self.radius * Circle.pi

c = Circle()
print(c.area())
```

    3.14159

# using static method decorator and creating the module on file circle.py

"""circle module: contains the Circle Class."""
class Circle:
    """Circle Class"""
    all_circles = [] # class variable containing a list of all circles created
    pi = 3.14159
    def __init__(self, r=1):
        """Create a Circle with the given radius"""
        self.radius = r
        self.__class__.all_circles.append(self) # when an instance is being initialized this adds to all_circles list
    def area(self):
        """determine the area of the Circle"""
        return self.__class__.pi * self.radius * self.radius
    
    @staticmethod
    def total_area():
        """Static method to total the areas of all Circles"""
        total = 0
        for c in Circle.all_circles:
            total = total + c.area()
        return total
Above I've created a module with a class Circle that we can recall in other python scripts:


```python
import circle as cir
c1 = cir.Circle(1)
c2 = cir.Circle(2)
c3 = cir.Circle(5)
c4 = cir.Circle(8)
cir.Circle.total_area()
```




    295.30946




```python
cir.__doc__
```




    'circle module: contains the Circle Class.'




```python
cir.Circle.__doc__
```




    'Circle Class'




```python
cir.Circle.area.__doc__
```




    'determine the area of the Circle'




```python

```
