---
layout: page
title:  "Biocomputing Group Website is live"
teaser: "BCG GROUP HAS A NEW WEBSITE"
header:
    image_fullwidth: "genvis-dna-bg_optimized_v1a.png"
breadcrumb: true
---

A first draft of the griffith lab site is now live. The site uses the static site generator [jekyll](https://jekyllrb.com/) and is based on the [feeling responsive](https://github.com/Phlow/feeling-responsive) theme. The site uses [jquery-backstretch](https://github.com/jquery-backstretch/jquery-backstretch) (2.1.16) to control full width background images and uses the [foundation](https://foundation.zurb.com/) (5.5.3) front end framework.

## key changes

The site features a number of key differences in contrast to the [feeling responsive](https://github.com/Phlow/feeling-responsive) theme however all of the old functionality remains in place. In brief these differences are:

1. Uses an updated [jquery-backstretch](https://github.com/jquery-backstretch/jquery-backstretch)
2. Blog functionality has been repurposed for a news feed
3. custom templates have been designed for publications and team members.
4. structure of the _data/socialmedia.yml file has been changed
5. added and rebuilt icons from the [entypo+](http://www.entypo.com/) library.

## development

Development of this site occurs on the "dev" branch at [https://github.com/griffithlab/griffithlab.github.io](https://github.com/griffithlab/griffithlab.github.io). The live site is published on the "master" branch and is periodically synced with "dev". To begin development follow the instructions on the README on the site GitHub page. The _drafts folder contains helpful examples for various aspects of the site.

## adding team members

Additional [team members](/team/) can be added by altering the pages/team.md file. The syntax for this is as follows:

{% raw %}
~~~~
 {% include team_member member_name="" full_name="" bio="" image="/assets/img/team/my_photo.png" role="" %}
~~~~
{% endraw %}

The team page is displayed according to the layout in _includes/team_member. The member_name parameter should match that in _data/socialmedia.yml which is used to add social media links. The image to include should be located in /assets/img/team/.

## adding publications

[Publications](/publications/) can be added by altering the pages/publication.md file. When doing so the following syntax should be followed where pmid is the pubmed id and doi is the digital object identifier:
{% raw %}
~~~~
 {% include publication authors="" journal="" doi="" pmid="" %}
~~~~
{% endraw %}

The publications page is displayed according to the layout in _includes/publication.

## adding research projects

[Research projects](/research/) can be added by altering the pages/research.md under the appropriate sub-heading. When doing so the following syntax should be followed where title is a short title for the project, description is a short summary of the project, team is a comma-delimited list of participating lab members, image is a representative graphic (please deposit in /assets/img/research/), citation is the citation for a related publication including author, year, title, journal, etc, and finally pmid is the pubmed id: 
{% raw %}
~~~~
 {% include project title="" description="" team="" image="/assets/img/research/my_image.png" citation="" pmid="" %}
~~~~
{% endraw %}

The research page is displayed according to the layout in _includes/project.
  
## adding news items

[News items](/news/) can be added by creating a new Markdown (.md) file in the _posts/ folder using the existing news item markdown files as examples.

