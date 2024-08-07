## Overview

This is the github repo for the Biocomputing Group at ASU [website](https://lee-cbg.github.io/). The website uses the static site generator [jekyll](https://jekyllrb.com/) and is based on the [Feeling Responsive jekyll theme](https://github.com/Phlow/feeling-responsive). Development occurs on the dev branch, the live site is located on the master branch.

## Installation

To install this site locally run the following commands:

1. Clone the repo and cd into it `$ git clone https://github.com/Lee-CBG/Lee-CBG.github.io.git`
2. Install the bundler `$ gem install bundler`
3. Install gems `$ bundle install`
4. build jekyll and watch for changes `$ bundle exec jekyll build`
5. run jekyll `$ bundle exec jekyll serve`

The site should now be running on localhost port 4000. Changes to files will show up interactively on localhost:4000

# How to modify content 

## UNIX users might require python3 command in manage_site script

## Dependencies to install using ->  pip install beautifulsoup4

1. Being in root folder run, ./manage_site.sh 
2. Then follow steps to add content. 
3. To remove content, choose the unique name like persons name or Site Title with exact case match. 
4. After that press 3 in the menu to generate the new markdown file 
5. Note: To modify data like body of a content its faster to go json file and modify it there and then click generate again.
6. !Optional! See archived folder to see examples of asset locations url, and store it in that respective folder.
7. Lastly, push the changes with a commit message! 
8. Exception-> To update publications, just add all the bibtex in scripts/example.bib and then choose Publications option in main menu it'll automatically generate the markdown file. 


## License

The code for this site is licensed under an MIT license, images may have specific attribution requirements and are licensed individually under assets/img/image_attribution
