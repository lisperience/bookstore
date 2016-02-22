Bookstore Project
============

Bookstore project is a web application designed to help to catalog, maintain and lend books.

Administrator of a bookstore can add/remove books, mark them as read, or rate them.
Books can belong to multiple categories, have multiple properties, like ISBN number,
Title, Author, publication year, reviewers, edition number, publisher, link to amazon, pictures of different sizes
number of pages, publication year, condition (new/ like-new/ old/ don't-touch), etc...

User (or a borrower) is an authenticated user who can borrow books for a specified period of time, after which he will be charged if he doesnt give back his books,
each user can see everything available and mark if he wants to borrow certain book, and when he will come to borrow the books he has marked.

There will be also information about how many books are borrowed, how many are overdued, who borrowed which books etc.


Goals
------------
 1. To catalog books in my home (or potentialy other places)
 2. To experiment on building a responsive website
 3. To build a full-stack working Web Application
 4. Have fun and potentialy profit (yeah sure...)

Frameworks/ tools used
------------

Because I DON'T want to repeat myself and dangle between different choices (there is no one-size-fits-all solution either way) such as flask, pyramid, bottle, and whats worse even different languages/frameworks like nodejs, rails, or even yesod (haskell).
    All of those choices are very interesting it's better to stick to one solution for now as a starter project.

 * for backend: django framework using rest-api ( http://www.django-rest-framework.org/ )
* Why?: I already know python both theoretically and practically but used it in some non-web related projects, so why not trying if for web?
        Django is most-wanted framework on the market right now, even though it tastes bitter to me I will stick to it because I don't have infinite time to do R&D on other frameworks
    
 * for frontend: twitter-bootstrap, with angularjs
* Why#2:        I don't want to create complicated site, just to make it look good and create it ASAP, whats more I already used some bootstrap and angularjs before so it should not be a big problem, and moreover those are the tools that are most valuable on the market today


TODO
------------
Design appropriate models
Use AngularJS and twitter-bootatrap at some point

After everything learn abour restful api and use it here
