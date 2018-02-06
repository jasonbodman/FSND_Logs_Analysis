<h1>FSND_Logs_Analysis</h1>
<h3>Section 3 Project for Udacity's Full Stack Nanodegree Program</h3>

<b>Project Description:</b> Using a pre-built postgreSQL database from Udacity, you are asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

<b>Project Goals:</b>Answer three questions using SQL queries via Python:
<li>What are the titles of the three most popular articles of all time?
<li>Who are the three most popular authors of all time?
<li>List any days where more than 1% of all requests resulted in errors.

<h5>Instructions to Install and Run</h5>
<b>Install</b>
<ul>1) Install <a href="https://www.virtualbox.org/">VirtualBox</a> and <a href="https://www.vagrantup.com/>Vagrant</a>.</ul>
<ul>2) Download or clone this repository.</ul>
<ul>3) Open Terminal/Command Prompt and navigate to the downloaded repository</ul>
<ul>4) Run <code>python logs.py</code></ul>

<h5>Program Notes</h5>
<b>Views used:</b>
<li><code>full_details</code>: combined basic details from <code>articles </code> and<code>authors</code> tables.</li>
<li><code>errorlog</code>: counted the number of <code>404 NOT FOUND</code> statuses returned each day, grouped by date</li>
<li><code>daily_views</code>: counted the number of HTTP requests each day, grouped by date.</li>
