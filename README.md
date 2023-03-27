# product-link-cleaner
This is a simple python script which automatically trims and cleans product hyperlinks pasted to the clipboard. It monitors the clipboard for new content (it can only handle text), and if the content is the URL is a product link on one of the supported sites it trims out anything but the product URL and pastes that to the clipboard instead.

Currently, it only supports Amazon.com, eBay.com, and Etsy.com, though I may add more.

I made this for my own convenience when copying multiple product links out of a browser and into note taking software or emails. It is meant to be made into a standalone executable, which can be easil one using pyinstaller. 
