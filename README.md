# <h1>Django_hw_1</h1>
<h2>Here is second django project.</h2><br> 

List what was done:

* new management command was created:
  * command to create fill db<br>
    use $ python manage.py fill_db a b c d, where:
    * a - numbers of authors
    * b - numbers of publishers
    * c - numbers of books
    * d - numbers of stores
* new models for testing was created (Author, Publisher, Book and Store)
* all fixtures in project
* new ModelAdmin for all models
* added celery and new view to sent reminders to e-mail (to console)<br>
  to test it run $ celery -A hw_project_2 worker --loglevel=INFO
* added periodic task using celery beat, that check updates in site and add new quotes in db<br>
  to run this task use -A hw_project_2 worker -B --loglevel=INFO
* new class based views for Author model (start in /authors/)

You can start from /detail/
