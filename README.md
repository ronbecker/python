# python
Just a repo of simple Python scripts I use.

## CleanJaro:
CleanJaro is a really simple script I use to do some basic maintenance on my Manjaro install. It has 5 options not including Exit. Each option will loop back around to the main menu so you can run it once and run every action you want to.

CleanJaro Getting Started:

You have a couple options here.

`cd` into the directory with cleanjaro.py in it, and run `python cleanjaro.py`

or

Place it in your `~/bin` directory, rename it to `cleanjaro` removing the `.py` extension. Then you will need to `chmod +x cleanjaro` to make it executable. As long as your bin folder is in your path you can now run it from anywhere by typing `cleanjaro` in terminal.

## reddit-scrape
This little program uses PRAW, and Pandas to scrape info from r/learnpython and store the results in a csv file. 

reddit-scrape Getting Started:

You will need to create a reddit app. You are going to need the app's client id, client secret, and a username and password. 

1. First clone this repo to your machince: `git clone https://github.com/ronbecker/python`

2. `cd` into the the `python` folder, and then `cd` into the `reddit-scrape` folder. Example: `cd python/reddit-scrape`

3. Make sure you edit scrape.py and put in your client id, client secret, username, and password. You can also change what subreddit it will scrape by changing line 12 `subreddit = reddit.subreddit('learnpython')`. Just change learnpython to the name of the subreddit you wish to scrape. 

4. Run `python scrape.py`

5. Enjoy.

