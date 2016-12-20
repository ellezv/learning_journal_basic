# Basic Learning Journal -- DRAFT

Basic learning journal app developed using Pyramid and deployed on heroku.

##Deployement:
You can find this learning journal deployed on Heroku [here](http://maelle-learning-journal.herokuapp.com)



## Getting Started

``sh
- cd <directory containing this file>

- $VENV/bin/pip install -e .

- $VENV/bin/pserve development.ini
``

#Routes
So far we have very basic routing:
    - `/` will take you to the home page, a listing of journal entries
    - `/journal/today` is my journal entry for today 12/19/16
    - `/journal/create-entry` will take you to a (non-functional) form to create an entry
    - `journal/edit-entry` will take you to a (non-functional) form pre-populated with today's entry to edit.

## Authors:
    - Maelle Vance
    - Amos Boldor