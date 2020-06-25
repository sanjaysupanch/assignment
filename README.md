# FullThrottle Labs Assignment
<a href="https://fullthrottle-api.herokuapp.com/">Visit to our website!</a>
<a href='https://fullthrottle-api.herokuapp.com/member/W4YX1328A'>For Update and Delete (filter through 'mid')</a>
<a href='https://fullthrottle-api.herokuapp.com/period/'>List of Period table</a>
<a href='https://fullthrottle-api.herokuapp.com/period/1'>For Update and Delete Period Table(filter through 'id')</a>
<br/><br/>

<h4>Command to run this project</h4>
<p>Note: In manage.py directory run</p>

<b>$ pip3 install -r requirement.txt</b></br>
<b>$ python3 manage.py makemigrations</b></br>
<b>$ python3 manage.py migrate</b></br>
<b>$ python3 manage.py runserver</b></br>

<h1>I'm using  Generic Class-Based Views</h1>

<p> The generic class-based-views was introduced to address the common use cases in a Web application, such as creating new objects, form handling, list views,       pagination, archive views and so on.<br>
  
   It come in the Django core, and we can implement them from the module django.views.generic.


<h4>Here is an overview of the available views:</h4>

## Simple Generic Views
* View
* TemplateView
* RedirectView
## Detail Views
* DetailView
## List Views
* ListView
## Editing Views
* FormView
* CreateView
* UpdateView
* DeleteView

# Populating Database With Faker Library
* In order to enter the fake data into our database, we are creating a python file and then running it to complete the process. In our python script, we are first setting our Django environment by using our project settings. Then we are setting-up Django after importing it. To use our faker library, we are creating an instance for it. We are generating a fake name by using obj.name().  We can generate random numbers too with the help of faker library, but we have to specify the number of digits for that. All process has to repeat for N times, where N is the number of Member. Hence, a for loop is used for that purpose.

