# Project \#2 - eBay Motors Regression #
---
For our second project at Metis, we were tasked with applying regression techniques to a data set of our choosing (to be acquired by webscraping). I have always loved cars, so I set out to build a generalized car pricing model using linear regression.

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

***Overview:***
-------------
I believe that with access to the right data, namely historical transacted price information for common makes and models, it is possible to accurately predict not only what a car will sell for in the used market, but also which of these cars will become 'classic' or 'collector' cars.

I began with the idea that while the price curve for most cars looks something like an exponential decay function, certain cars exhibit a 'j-curve' in prices--that is, for any number of reasons, the value of the car begins to increase again after some period of depreciation. This could be because certain features are no longer available in newer model years, because the car is no longer manufactured (or the company no longer exists), because the car was rare to begin with, or for a host of other reasons unique to smaller segments of buyers in the car market. A pet project of mine with my new data science skillset is to find out what causes price reversal in the used car market, and how to spot excellent values.

***Challenges:***
-----------------
With this project, it was a real challenge to find good price data for used cars. Certain data providers such as Edmunds make this information available via their API, but with data access limits there was no good way to scale up and generalize the analysis in the two weeks we were allotted. I wanted to develop a better understanding of regression techniques instead of building an accurate but limited pricing tool for a handful of car models, so I decided to scrape data from eBay Motors, one of the most common places to list a used car which importantly *maintains completed auction and sale listings* for a few months (including *transacted prices*). 

This is crucial. If I were to work with data from Craigslist, Autotrader, Cars.com, CarGurus or any other popular online car buying marketplace, I would have to have used *listed* prices as a proxy for *true value*. The only way to get an accurate picture of today's value for a 1968 Ford Mustang, for example, is to see what that car (or a very similar model) is currently trading for--*not* what a seller thinks he or she can get for it.

The second problem, also related to the availability of data, is that model MSRPs (and corresponding used car values) vary widely with factory options. To return to the previous example, two Ford Mustangs from 1968 could easily vary in value by a factor of 10 if one is a fully equipped high-performance model, and the other is a stripped down economy model. I knew I would need to account for all of these options and features using the text data from the eBay listing. But, eBay does not require sellers to fill out all or even most of the fields in order to list a car. At minimum, a car can be listed with just the following:
- Year
- Make & Model
- VIN: Vehicle Identification Number (can be faked)
- Mileage (also can be faked)
- Title Status (can be left blank)

eBay also allows sellers to enter their own values for dropdown menus:
**insert image here**

Because I could not implement a VIN lookup tool to fill in sparse or incorrect data given a large proportion of listings with faked numbers, I ran into further challenges both in cleaning the data and creating categorical variables.

***Conclusion:***
-----------------
While my generalized model did not achieve a high Adjusted R-Squared score partly due to a lack of reliable data, I will be working towards building an accurate price prediction and auction monitoring tool for specific car models. First I will try to make this approach work with a better scraper and text processing techniques to create categorical variables, and then I hope to incorporate one or more paid commercial datasets and data from other online used car marketplaces.
