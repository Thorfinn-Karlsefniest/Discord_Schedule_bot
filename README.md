# Discord_Schedule_bot

The Discord bot enables users to easily enter times that they are busy and allows anyone in the server to view that schedule and determine when a user in question is free. 

The bot allows an user to record the folloiwng: 
- Courses they are taking
- Time and room number for said courses
- Committment type (office hour, lecture, tutorial, etc.)

Moreover, it allows both the user and other members of an initiaized Discorrd server to view the following: 
- Who is "free" at this hour (view users not currnetly in a class during a given time period)
- Where a user may be depending on where their last class was
- Any user's schedule on a given day or week

Users may use the bot to issue the following commands: 

- @(user, type: str)!isfree -> type: bool 
  - Views whether a given user is free at that particular hour
- !update_sched
  - Allows the user to update their personal schedule 

The bot out of the fact that I am in a large server and hate having to scroll through dozens of schedules if I want to plan something or meet up with someone. So instead, I built a bot so that people just record when they're free for me and I can easily access it. In other words, the bot was built to ensure that larger servers with friends in a university can easily coordinate meetups depending on availabilty natively on a platform everyone is on. 

The program is built using Python and stores information using SQL. 
