# Robot Bill Peduto!

This Python script powers <a href="http://twitter.com/billpedutobot">@BillPedutoBot</a>, a Twitter bot that shares the Pittsburgh mayor's public schedule with a bit of humor. 

## Included files:

- tweet.py: Queries simple API from sister project <a href="https://github.com/arm5077/wheresbill">Where's Bill</a>, parses response and tweets latest item in schedule.
- config.py: Contains Twitter bot credential information.
- sample_data.csv: A commma-separated values file containing a January-March data dump of Mayor Bill Peduto's public schedule. Not needed to run the bot, but helpful to see the kind of stuff Bill Peduto does!

## How you can help

Right now, @BillPedutoBot is pretty straightforward: It tweets his schedule with a minimum of flair. It needs your help to liven it up!

Things that need done:

- Expanding the parser's vocabulary, allowing it to print custom messages for different types of events on Peduto's schedule. I've made a good dent, but it still has far to go.
- Figuring out other fun things for @BillPedutoBot to tweet! Maybe an animated GIF of 'Dutes chowing down on pierogies every time his schedule mentions dinner? Just sayin!
- Anything else you think would increase the public's access to Pittsburgh's mayor and his doings. Extra points for fun. 

## Contact
If you have any suggestions or ideas for @BillPedutoBot not conducive to Github, shoot me an e-mail at amcgill@post-gazette.com.

## Setup

To run a bot like BillPedutoBot, you will need to have:

* apache or other web server
* python enabled with that web server

1. Edit config.py to fill in your connection details.

2. Run tweet.py to have bot check if there's an event on Peduto's schedule in the next hour and tweet it. 

3. Follow @BillPedutoBot and enjoy!

To keep the bot happy and well-fed, set up a cronjob to run the script every half hour or so. (Tip: Schedule it shortly before the hour, say, 1:59. This will give it time to react to events happening at 2 that it might miss otherwise.)