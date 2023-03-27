# product-link-cleaner
This is a simple python script which automatically trims and cleans product hyperlinks pasted to the clipboard. 

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
product-link-cleaner monitors the clipboard for new content (it can only process text), and if the content is a product URL from one of the supported sites it trims out anything but the product URL and pastes that to the clipboard instead. I made this for my own convenience when copying multiple product links out of a browser and into note taking software or emails.

Currently, it supports Amazon.com, eBay.com, and Etsy.com.
	
## Technologies
Project is created with:
* Python 3.8.8
	
## Setup
This can simply be run as a script, though I intended it to be made into a standalone executable, which can be easily done using pyinstaller. 
