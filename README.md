# eBay Motors #
Generalized car pricing model using linear regression.

### Code cleanup in progress. ###
***To Do:***
------------
1. Improve **scrapy script** -- currently the spider pulls detail categories and values as a single list which requires many more cleaning steps and yields less useable data.
2. Create function to pull **model year** from title when a listing does not have the year listed in the details.
2. Parse **displacement** field to yield engine sizes in consistent unit and format.

***Future:***
-------------
1. Use clustering and NLP to classify auto market into type of car and type of buyer segments.
2. Regression analysis on these segments.
3. Live auction price prediction (and scoring)!
