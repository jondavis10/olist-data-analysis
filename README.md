# **olist-data-analysis**
## Purpose of Project

                ++++++++++++++++++++++++++ GIT COMMANDS +++++++++++++++++++++++++++++++++
- closing marimo
    ```
    ctl+C
    ```

- Cloning files to local directory
    - Go to github.com  -> find your repository -> click on "Code" dropdown and copy the HTTPS URL
    - Go to your terminal and navigate to the directory you want the files to be
    - run `git clone <url> .`

- Staging changes
    - Two ways:
        - In VSCode you can use the UI to stage your changes and commit them or you can use the terminal
        - Terminal commands
        ```
        git add . # this stages everything in the *current* folder
        
        git add -A # this stages everything in your whole directory

        git add <filename> # this stages a specifc file
        ```

- Commiting files
    - Again, you can use the UI or the terminal
    - Terminal commands:
    ```
    git commit # this will commit your staged files **without** a message

    git commit -m "your message here" # this commits your staged files with a message
    ```

- Pushing to Github
    - Again, you can use the UI or the terminal
    - Terminal commands:
    ```
    git push 
    ```

- Pulling the updates _from_ Github
    - Again, you can use the UI or the terminal
    - Terminal commands:
    ```
    git pull 
    ```

                +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

                ++++++++++++++++ Instructions for creaating tables usings marimo +++++++++++++++++++++++++++++++
open marimo in VS studio command prompt: marimo edit 'file name' 
    Example: 
    ```
    marimo edit 00_Olist_setup.py
    ```
- create new SQL command cell and use the syntax: 
    ```
    create table if not exists `name of table` as select* from 'name of source.csv';
    ```
    Example:  
    ```
    create table if not exists Olist_customers as select * from 'olist_customers_dataset.csv';
    ```
-Rinse and repeat for all .csv files located in the C:\Users\15202\Documents\DataEngineeringProjects\VSCodeFiles\PersonalCodingProjects\olist-data-analysis file which can be found in the left panel of the VS studio explorer pane.
                +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

next steps 6-4-26: 
- look up how to connect dbeaver (interact with data) to `Olist_dataset.duckdb`
- Create Tables from CSV files in database file `.duckdb`

Next steps 6-10-26:
- create tables in marimo using the 'marimo edit 00_Olist_setup.py" command to access the marimo notebook. all CSV files in the "Olist-data-analysis" need a table, reference the SQL query to see how to create these tables.
- Mapping exercise: create schema tables linking all the common fileds (drawio can be used for visual or use excel)

meeting notes/next steps 6-30-26
- create tables using the instructions in the above section called 'instructions for creating tables using Marimo'
- if done with creating tables create new notebook file and mess around with joins and stuff

work notes 7-3-2026
- I finished creating tables from all the CSV files. Can I now combine all the tables into a single files that I can upload to Git? ask Matt for next steps.

Work notes 7-7-2026
- Explore data and create ERD (schema) table for data. 
-open the 01_Olist_Explore_Data.py.json file to continue work from last time cmnd: marimo edit 01_Olist_Explore_Data.py.json


Quick tips:
    
    

