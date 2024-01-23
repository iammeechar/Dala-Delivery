# Dala Delivery
This is a project for "Software Development " where a customers can make order food to be delivered to their location. You can search by a (list of) ingredient(s) to find matching recipes. Let's reduce some food waste!
It is using sample images from istock image , who provide great images for any subject matter but in this case we were searching for sample images for our menu.

installing dependencies:
`pip install -r requirements.txt`


start the program: 
`python src/main/python/main.py`



## 1. Git
Github Commit History. It is from two seperate repositories as the merge function produced a fatal error due to conflicting histories

&rarr; [See commit history here](https://github.com/iammeechar/Dala-Delivery/commits/master)

&rarr; [See commit history here](https://github.com/iammeechar/Food-Delivery-App../commits)

## 2. UML 
UML Diagramm created with StarUML (Class, Component and User Diagrams for the project with Edlich's Fund)

&rarr; [PNGs and StarUML-Files](https://github.com/iammeechar/Dala-Delivery/tree/master/UML)

## 3. DDD
Creation with Trello board and Miro Event Storming file and resulting Diagrams and DDD 

&rarr; [Link to the Trello Board.](https://trello.com/b/DndzLlGj/food-delivery-app)
&rarr; [PDF-file with Event Storming, Diagram and DDD](https://trello.com/b/DndzLlGj/food-delivery-app)

## 4. Metrices
Creation of SonarCloud account and connecting to repository (with advanced settings) for metric badges:

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=lunarie16_IngredientRecipeFinder&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=lunarie16_IngredientRecipeFinder)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=lunarie16_IngredientRecipeFinder&metric=bugs)](https://sonarcloud.io/summary/new_code?id=lunarie16_IngredientRecipeFinder)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=lunarie16_IngredientRecipeFinder&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=lunarie16_IngredientRecipeFinder)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=lunarie16_IngredientRecipeFinder&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=lunarie16_IngredientRecipeFinder)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=lunarie16_IngredientRecipeFinder&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=lunarie16_IngredientRecipeFinder)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=lunarie16_IngredientRecipeFinder&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=lunarie16_IngredientRecipeFinder)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=lunarie16_IngredientRecipeFinder&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=lunarie16_IngredientRecipeFinder)
<!-- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=lunarie16_IngredientRecipeFinder&metric=coverage)](https://sonarcloud.io/summary/new_code?id=lunarie16_IngredientRecipeFinder) -->

## 5. Clean Code Dev
Adding clen code developemnt for improved usage and readabilty as well as for better maintance of code.

### A)
&rarr; [parameter and return types](https://github.com/lunarie16/IngredientRecipeFinder/blob/4fdee32c880bd9b0ddc84ddf32752fb916c3f81f/ingredientFinder.py#L13)

&rarr; [docstrings](https://github.com/lunarie16/IngredientRecipeFinder/blob/4fdee32c880bd9b0ddc84ddf32752fb916c3f81f/ingredientFinder.py#L15)

&rarr; [explanatory variable names](https://github.com/lunarie16/IngredientRecipeFinder/blob/4fdee32c880bd9b0ddc84ddf32752fb916c3f81f/ingredientFinder.py#L25)

&rarr; [throw exception with context](https://github.com/lunarie16/IngredientRecipeFinder/blob/4fdee32c880bd9b0ddc84ddf32752fb916c3f81f/ingredientFinder.py#L7)

&rarr; [one assert per test](https://github.com/lunarie16/IngredientRecipeFinder/blob/053c05a87481155602432f135db364b8468c7a3e/src/unittest/python/ingredientfinder_tests.py#L130)

### B)
Creation of a Cheat Sheet for upcoming projects 

&rarr; [Cheat Sheet](https://github.com/iammeechar/Dala-Delivery/blob/master/Clean%20Code%20Cheat%20Sheet/Clean%20Code.md)

## 6. Build
Usage of Pybuilder to build Project and have the ability to install and import as a package for usage in other projects 

&rarr; [with Pybuilder](https://github.com/lunarie16/IngredientRecipeFinder/tree/main/target/dist/IngredientRecipeFinder-1.0.dev0): find files [here](https://github.com/lunarie16/IngredientRecipeFinder/tree/main/target)

## 7. UnitTests
Writing UnitTests to keep correctness and desired functionality of algortihm 

! tests will be executed automatically with every push to respository -> with github actions (see 8.)
&rarr; [find tests here](https://github.com/lunarie16/IngredientRecipeFinder/blob/main/src/unittest/python/ingredientfinder_tests.py)

run tests manually with:
`python3 -m unittest -v src/unittest/python/ingredientfinder_tests.py`

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
Example of use of DSL like Bootstrap and CSS for HTML files   

&rarr; 

&rarr; 
## 11. Functional Programming
Apply functional programming for it's understanding and adding a class for Recipe as learned in Prog. I for java

&rarr; [only final data structures](https://github.com/lunarie16/IngredientRecipeFinder/blob/1ee0024ea1816d2a820f3439ed63d91c83b5b9b6/src/main/python/recipe.py#L5)

&rarr; [(mostly) side effect free functions](https://github.com/lunarie16/IngredientRecipeFinder/blob/1ee0024ea1816d2a820f3439ed63d91c83b5b9b6/src/main/python/recipe.py#L14)

&rarr; [use closures / anonymous functions](https://github.com/lunarie16/IngredientRecipeFinder/blob/1ee0024ea1816d2a820f3439ed63d91c83b5b9b6/src/main/python/recipe.py#L12)

&rarr; [the use of higher-order functions/functions as parameters and return values](https://github.com/lunarie16/IngredientRecipeFinder/blob/1ee0024ea1816d2a820f3439ed63d91c83b5b9b6/src/main/python/main.py#L16)

