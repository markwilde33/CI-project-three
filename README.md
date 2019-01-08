# Animal Riddle Game

### Code Institute: Practical Python Milestone Project

<a href="http://flask-riddle.herokuapp.com" target="_blank"> Click here to view website</a>

*Developer: Mark Wilde*

-------



## Index


1. [Project Instructions](#instructions-from-code-institute)
2. [Riddle Information](#riddle-information)
3. [UX](#ux)
    * [Wireframes](#wireframes)
    * [Design](#design)
    * [User Stories](#user-stories)
4. [Features](#features)
5. [Technologies](#technologies-used)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Installation](#installation)
9. [Credits](#credits)



## Instructions From Code Institute


Guidelines for project development:

- The project's logic must be written in Python. HTML and CSS. Use flask, a micro-framework, to structure your project's back-end. 
- Build a web application game that asks players to guess the answer to a pictorial or text-based riddle.
- The player is presented with an image or text that contains the riddle. Players enter their answer into a textarea and submit their answer using a form.
- If a player guesses correctly, they are redirected to the next riddle.
- If a player guesses incorrectly, their incorrect guess is stored and printed below the riddle. The textarea is cleared so they can guess again.
- Multiple players can play an instance of the game at the same time, each in their own browser. Users are identified by a unique username, but note that no authentication features such as a password are required for this project.
- Create a leaderboard that ranks top scores for all (at least recent) users.
- You should conduct and document tests to ensure that all of your website’s functionality works well.
- Write a README.md file for your project.
- Use Git & GitHub for version control.
- Deploy the final version of your code to a hosting platform such as Heroku.



## Riddle Information

-Players are requested to register and login to play the game. They can then read the rules or began a game immediately.
-The game consists of 10 animal riddles.
-Players are allowed 3 guesses per riddle.
-Players receive 5 points for each correct answer.
-Players are deducted 1 point for each incorrect answer.
-When players give a correct answer they receive a success message and are shown an image of the animal. A link with further information regards each animal is also provided above the image.
-Players continue with the riddle by clicking on the next question button which displays below the animal image when a correct answer is given.
-When players give an incorrect answer they receive a warning message which also displays how many attempts they have left.
-When a player gives 3 incorrect answers they receive a warning message are taken to the next riddle.
-On completion of the riddle users receive a message with their final score and are taken to the leaderboard page which displays the top ten riddle scores.


## UX


### Wireframes

[Balsamiq](https://balsamiq.com/) was used to create the wireframes.

<details>
      <summary><strong><em>Homepage</em></strong></summary>
  
  
  ![alt="Homepage mockup"](mockups/Home_page.png)
</details> 

<details>
   <summary><strong><em>Music page</em></strong></summary>
  
 
  ![alt="Music page mockup"](mockups/Music_page.png)
</details> 

<details>
   <summary><strong><em>Customers page</em></strong></summary>
  
   
  ![alt="Customer page mockup"](mockups/Customer_page.png)
</details> 

<details>
  <summary><strong><em>Contact page</em></strong></summary>
  
  
  ![alt="Contact page mockup"](mockups/Booking_page.png)
</details> 



### Design


- Development of the website adhered to a mobile first approach. The site consists of four separate pages. Two of the audio tracks, and a customer story, have been hidden on smaller screens to improve the aesthetic.

- All pages share the same navbar and footer, though each page has a clear purpose and some unique functionality.
  
- The Bootstrap framework underpins the project and was implemented as per convention.

- The project also made use of the CloudFlare and Font Awesome libraries.

- The websites color scheme and layout were chosen in an attempt to represent the Animals long standing brand style with their peak popularity coming in the 1960s. A retro, classic-style approach was undertaken; to invoke The Animals experience.
 
- Includes a side article regards the bands ongoing activism in the field of animal rights and welfare. Customers are informed that 20% of all band earnings are made available to several animal charities. A link is provided for users if they would like to visit the webpage of one of their favorite [charities](https://www.worldanimalprotection.org/). It is hoped that this commitment may be appealing to potential customers and increase event bookings.



### User Stories


Several user stories were considered before development began:

1. "As a current Animals fan I want to be able to quickly access the bands music online via an official website. I also want 
    to be up-to date with new material, news and announcements"
 
2. "As a current Animals fan I would like to recommend an official Animals website to my friends (as potential new fans). So that they can watch and listen to the bands videos and music; and learn more about the bands history."

3. "As a potential Animals fan, I would appreciate access to an official band website were I can easily access the bands material for free. I would like to see some pictures of the band and be provided with up-to date information about the band."

4. "As a potential customer who is considering booking the band for an event, I want easy access to the means of doing so through an official, secure website. I also want quick access to some of their greatest hits which I would expect to find freely available on their website. Furthermore, I would like access to useful information such as band availability and event prices. Again, I would expect this information to be clearly presented and easily accessible via the bands website."

5. "As a current fan interested in the day to day news and activities of the band, I would like to be provided easily accessed links to their social media accounts, so that I can follow them and be the first to know of any exciting developments."



## Features


| Page      |                                                                                             Description                                                                                             |
| :-------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Home      |                 This the the landing page. It includes the bands logo, information about the band an iconic band photograph and two embedded YouTube videos of the bands hit songs.                 |
| Music     | This page includes 6 audio tracks with individual album covers, current band news and a link to lead singer Eric Burdons latest solo album. It will also host new material as it becomes available. |
| Customers |                 This page includes some kind words of recommendation from some of the bands famous customers. It also documents the bands ongoing animal activism and charity work.                 |
| Contact   |               This page provides information on how to contact the band and book an event. Links to the bands availability throughout the year and event pricing, are also provided.                |



## Existing/Future Technologies


- A merchandise page.
- A page listing the music festivals and concerts the band will be playing at in the coming calender year.
- A page hosting a photo collection and personal stories about each band member.



## Technologies Used


- [HTML](https://www.w3.org/)
    - The project uses **HTML** to create the pages.

- [CSS](https://www.w3.org/)
    - The project uses **CSS** to style the pages.

- [Bootstrap CSS Framework](https://getbootstrap.com/)
    - The project uses **Bootstrap** for styling and responsive design.

- [FontAwesome Icons](https://fontawesome.com/)
    - The project uses **FontAwesome** for the social media icons and the navbar buttons.
    
- [Hover.CSS](http://ianlunn.github.io/Hover/)
    - The project uses **Hover** for button hover animations for social media icons and the navbar buttons.
 
- [Google Fonts Library](https://fonts.google.com/)
    - The project uses **GoogleFonts** to import and use unique fonts.
   
   
    
## Testing


In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.



## Deployment


The website has been deployed to [Github Pages](https://pages.github.com/) and can be accessed [here](https://markwilde33.github.io/CI-project-one/)

This project has been saved to a Github repository from the beginning of development. Hosting it to Github Pages was very straightforward. In the repository, from the settings menu, Github Pages was activated and the master branch was included as the source. A message is then generated by Github containing the following information: Your site is published at https://markwilde33.github.io/CI-project-one/

In my case when I clicked on the link it returned a 404 error. After visiting [Stackoverflow](https://stackoverflow.com/questions/11577147/how-to-fix-page-404-on-github-page), I took the following advice:

``` 
<!-- input the following commands in your terminal -->

$ git commit --allow-empty -m "Trigger rebuild"

$ git push
```
This fixed the issue and the website loaded as intended.



## Installation


``` 
from the console type:

$ git clone https://github.com/markwilde33/CI-project-one.git
$ cd CI-project-one
$ pip3 install -r requirements.txt
$ python3 run.py

```
App available at http://127.0.0.1:5000/


## Credits


[Code Institute](https://codeinstitute.net/)

The Html Fundamentals module, Css Fundamentals module and the User Centric Frontend Development module were used for guidance.


### Content

- [Wikepedia](https://en.wikipedia.org/wiki/The_Animals) was used for band information.
- [Youtube](https://www.youtube.com/results?search_query=the+animals) was used for band music.


### Media


- [Google Images](https://www.google.com/search?tbm=isch&source=hp&biw=1357&bih=978&ei=erXyW_DiGMP4kwWR64bYDg&q=the+animals&oq=the+animasl&gs_l=img.1.0.0i10i24.6344.8119..10740...0.0..1.212.973.9j1j1......3....1..gws-wiz-img.....0..0j0i8i30j0i24.4zqtiao4AEY) was used for band pictures.


### Acknowledgements


- I received inspiration for this project from [The Net Ninja](https://www.thenetninja.co.uk), [Brad Traversy](https://www.traversymedia.com/) and [Corey Schafer](https://www.youtube.com/user/schafer5/featured).

