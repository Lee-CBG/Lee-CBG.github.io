## Overview

This is the github repo for the BCG lab [website](http://griffithlab.org). The website uses the static site generator [jekyll](https://jekyllrb.com/) and is based on the [Feeling Responsive jekyll theme](https://github.com/Phlow/feeling-responsive). Development occurs on the dev branch, the live site is located on the master branch.

## Installation

To install this site locally run the following commands:

1. Clone the repo and cd into it `$ git clone `
2. Install the bundler `$ gem install bundler`
3. Install gems `$ bundle install`
4. Build jekyll $ bundle exec jekyll build
5. run jekyll $ bundle exec jekyll serve

The site should now be running on localhost port 4000. Changes to files will show up interactively on localhost:4000

**Note:** The _config.yml file is only read during the initial serve, changing this file will require re-running step 4 for changes to appear.

## License

The code for this site is licensed under an MIT license, images may have specific attribution requirements and are licensed individually under assets/img/image_attribution
