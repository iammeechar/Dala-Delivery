# Dala Delivery
This is a project for "Software Development " where a customers can make order food to be delivered to their location. You can search by a (list of) ingredient(s) to find matching recipes. Let's reduce some food waste!
It is using sample images from istock image , who provide great images for any subject matter but in this case we were searching for sample images for our menu. The code is written in python.

installing dependencies:
`pip install django`


start the program: 
 On the anaconda terminal locate the Delivery file and run`python manage.py runserver`



## 1. Git
Github Commit History. It is from two seperate repositories as the merge function produced a fatal error due to conflicting histories

&rarr; [See commit history here](https://github.com/iammeechar/Dala-Delivery/commits/master)

&rarr; [See commit history here](https://github.com/iammeechar/Food-Delivery-App../commits)

## 2. UML 
UML Diagrams created with StarUML (Class, Component and User Diagrams for the project.)

&rarr; [PNGs and StarUML-Files](https://github.com/iammeechar/Dala-Delivery/tree/master/UML)

## 3. Requirements Engineering
Creation with Trello board showing the various requirements for website interaction between customers and the restaurant.

&rarr; [Link to the Trello Board.](https://trello.com/b/DndzLlGj/food-delivery-app)


## 4. Metrices

###A)
Creation of SonarCloud account and connecting to  Github repository for metric badges:

[![Maintainability Rating](https://sonarcloud.io/component_measures?id=iammeechar_Dala-Delivery&metric=sqale_rating&view=list)](https://sonarcloud.io/summary/new_code?id=iammeechar_Dala-Delivery)

[![Bugs](https://sonarcloud.io/component_measures?id=iammeechar_Dala-Delivery&metric=reliability_rating&view=list)](https://sonarcloud.io/summary/new_code?id=iammeechar_Dala-Delivery)

[![Duplicated Lines (%)](https://sonarcloud.io/component_measures?id=iammeechar_Dala-Delivery&metric=duplicated_lines_density&view=list)](https://sonarcloud.io/summary/new_code?id=iammeechar_Dala-Delivery)

[![Reliability Rating](https://sonarcloud.io/component_measures?id=iammeechar_Dala-Delivery&metric=reliability_rating&view=list)](https://sonarcloud.io/summary/new_code?id=iammeechar_Dala-Delivery)

[![Quality Gate Status](https://sonarcloud.io/summary/new_code?id=iammeechar_Dala-Delivery)](https://sonarcloud.io/summary/new_code?id=iammeechar_Dala-Delivery)

[![Security](https://sonarcloud.io/component_measures?id=iammeechar_Dala-Delivery&metric=new_security_rating&view=list)](https://sonarcloud.io/summary/new_code?id=iammeechar_Dala-Delivery)

[![Lines of Code](https://sonarcloud.io/summary/new_code?id=iammeechar_Dala-Delivery)](https://sonarcloud.io/summary/new_code?id=iammeechar_Dala-Delivery)

###B)
Below is a link containing the pdf document with an analysis of the project.
[![Project Analysis]](https://github.com/iammeechar/Dala-Delivery/blob/main/Docs/Dala%20delivery%20Analysis.pdf)

## 5. Clean Code Dev
Adding clean code developemnt links. This allows for improved usage and readabilty as well as for better maintance of code.

### A)

&rarr; [parameter and return types](https://github.com/iammeechar/Dala-Delivery/blob/main/customer/views.py#L22)

&rarr; [docstrings](https://github.com/iammeechar/Dala-Delivery/blob/main/customer/views.py#L20)

&rarr; [explanatory variable names](https://github.com/iammeechar/Dala-Delivery/blob/main/customer/views.py#L72)


### B)

Creation of a Cheat Sheet for upcoming projects 

&rarr; [Cheat Sheet](https://github.com/iammeechar/Dala-Delivery/blob/main/Clean%20Code%20Cheat%20Sheet/Clean%20Code%20Cheat%20Sheet.pdf)

## 6. Build
Usage of SonarQube to create a build management system used to scan for clean code and display vulnerabilities using Github Actions 

&rarr; [with SonarQube for python CLI](https://github.com/iammeechar/Dala-Delivery/blob/main/.github/workflows/build.yml)

## 7. DDD
Below is a link to file containing the DDD diagrams.
&rarr; [Link to the DDD diagrams](https://github.com/iammeechar/Dala-Delivery/tree/main/DDD%20Diagram)



## 8. Continuous Delivery
Adding Github Action Test exectuion on every push to verify correctness of the code

&rarr; [GitHub Action - Test](https://github.com/iammeechar/Dala-Delivery/tree/main/.github/workflows)

## 9. IDE
Below are some shortcuts my favourite shortcuts to use during development. 

### VS Code 
  
&rarr; *built-in shortcuts*:
- ```cmd + f``` (find)
- ```cmd + r``` (replace) 
- ```option + c/v/x``` (copy/paste/cut)
- ```cmd + /``` (comment (out))  
- ``` shift + ctrl + d``` (start debugger)

## 10. DSL
Below are some examples of the use of DSL like Bootstrap and CSS for HTML files and  Django urls for linking The HTML Files.   

&rarr;[MDB links for Bootstrap](https://github.com/iammeechar/Dala-Delivery/blob/main/customer/Templates/customer/base.html#L19)

&rarr;[Django HTML urls](https://github.com/iammeechar/Dala-Delivery/blob/main/customer/Templates/customer/order.html#L1)
## 11. Functional Programming
Application of  functional programming to allow for easier understanding of the various functions and variables in python

&rarr; [only final data structures](https://github.com/iammeechar/Dala-Delivery/blob/main/customer/views.py#L72)

&rarr; [side effect free functions](https://github.com/iammeechar/Dala-Delivery/blob/main/customer/views.py#L22)

&rarr; [use closures / anonymous functions](https://github.com/iammeechar/Dala-Delivery/blob/main/customer/views.py#L114)

&rarr; [the use of higher-order functions/functions as parameters and return values](https://github.com/iammeechar/Dala-Delivery/blob/main/customer/views.py#L98)
