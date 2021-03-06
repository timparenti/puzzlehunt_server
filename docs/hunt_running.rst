How to Run a Hunt
*****************

So you want to run a puzzlehunt...

Below are all of the steps you should need to take to run an already created puzzlehunt:

Download Puzzles
================

Before anybody can start playing your hunt, you have to download the puzzles. Head over to ``{server URL}/staff/management/``, make sure the hunt you are trying to run is marked as the current hunt, and click the "Fetch ALL puzzles from URLs". It will take a few minutes, be patient.

That should just work, if it doesn't, check your links, check your PDF accessibility and try again. (if you really think it is a bug, feel free to submit an issue)

Playtester Setup
================

You probably want people to test your hunt before the actual event. This is easy using the puzzlehunt server. Just have the team of playtesters sign up like normal, then navigate to ``{server URL}/admin/huntserver/team/``, find the team, check the "Playtester" checkbox on their edit page, and save the team. They will then have access to the puzzlehunt as if it was open to them. 

Note: To mimic the exact puzzle experience, they will only have access to puzzles that are unlocked for them, so make sure to head over to the progress page and make sure to unlock their starting puzzles. 
 
Like any other team, their progress will be visible on the progress page, their submissions on the queue page, and their messages on the chat page. 

Hunt Start
==========

Okay, the hunt is almost ready to happen, you've downloaded all the puzzles, you've had people playtest the hunt, and now you're ready to turn it over to the public. Below is a short checklist of items to consider before and during the first few minutes of the event.

Before the hunt:
  - [ ] *Make sure the hunt start time is accurate*
  - [ ] Reset all progress from the management page
  - [ ] Ensure all puzzles have working PDFs and images
  - [ ] Ensure all teams have room assignments

Start of the hunt:
  - [ ] When you want to release the puzzles, click "Release Initial Puzzles" from the management page
  - [ ] Ensure that all teams show puzzles as unlocked on the progress page (may take a moment to update)
  - [ ] Have someone watching each of the staff pages (see below)

Staff Pages / During the Hunt
=============================

Hopefully your opening information session went well, the puzzles released flawlessly and people are now solving puzzles. Time to sit back and watch/make the magic happen with the help of the following staff pages:

Progress page:
  One of the 2 pages you definitely are going displayed somewhere during the hunt. Some cool features about this page:

    - The number of solved puzzles the team has solved is displayed next to each team
    - The color of each unsolved puzzle for a team will slowly fade from yellow to red the longer they have had the puzzle unlocked but not solved.
    - The last submission time will be visible in the cell for unsolved puzzles
    - The solve time will be visible in the cell for solved puzzles

Queue page:
  The other page you will almost certainly want displayed somewhere during the hunt. 

  Now that all answers are automatically responded to in one way or another upon submission, there is less work to do on this page, but make sure to keep an eye out for teams that need help or have possibly just misspelled something. 

  You can always update the submission response using the "Fix" link. The new content will be pushed to the team's page automatically. 

Chat page:
  It is important to maintain communication with the teams, which is where the chat page comes in. New messages from a team since the page was loaded will make the team's name appear in red. Only teams that have sent a message to the staff will show up on the list. 

  If you absolutely need to send a message to a team who has not contacted staff yet, you can manually do so from the /admin/huntserver/message/ page. 

Management page:
  The only thing you would want to do with the management page during the hunt is to update puzzle PDFs. If you find that you need to make a change, simply update the remote PDF content, and fetch the single puzzle with the single puzzle fetch button. The PDF and PNGs should update to match the remote content. 

Email page:
  You can use this to send email from the configured email to all hunt participants. If you don't trust the interface for some reason or want to send something fancier than plain text, you can click the "Click to show all emails" button to display all hunt participant emails and send something manually.

Charts page:
  Everybody likes charts! At the moment, we have the following charts:

    - Graph of number of teams that have any given puzzle locked, unlocked or solved
    - Graph of correct vs incorrect submissions for all puzzles
    - Graph of submissions over time during the hours that the hunt was open
    - Graph of solves over time during the hours that the hunt was open


Hunt End
========

The hunt is nearing completion, hopefully everything went well and enough teams have completed the hunt to satisfy you. If you think the hunt hasn't run long enough, be sure to update the hunt end time before you reach it. 

Once the hunt end time is reached, all puzzles will be available for the public and all hunt interfaces will update to indicate that the hunt is over. 