# Math Web Kit
Math-Web-Kit is a python library than is used in creating a table to arrange your data, downloading youtube videos with a ease, getting search results from web.
Current version of math web kit is 1.2 and will be publishing the next version soon. 
# Benefits of Math-Web-Kit
1. Downloading youtube videos.
2. Solving algebraic expression and doing factorisation.
3. Getting Gcd and Lcm of a list.
4. Creating a table to agrrange your data.
5. Getting ip address of a website
6. Solving linear equations in one variable.

# Tutorial

> import math_web_kit as m

Math-web-kit has a ability that when we will import it, package will assign variables for algebra.
# For Example

First, when you have not imported the library type the below algebraic expression:<br>
  'a * a-b * b'

You will get the error variable not defined.

Now import math_web_kit and try the expression again.

Error solved!
Python solved the expression without any extra attribute.

# Next Tutorial

Now it you want to add any extra variable like: math, lsl, etc. you can do than with the following attribute:<br>

    >>> lsl=m.set_variables(['lsl'])
  
This will make a symbol/variable similar to that of sympy.

When you have learned to set a variable for algebra we can solve linear equation using it.

# m.solve_equation(equation,equals,variables)

solve_equation is a attribute that is used to solve linear equations in one variable.

Example:<br>

    >>> solve_equation(2*x,4,[x])
    >>> {x: 2}
