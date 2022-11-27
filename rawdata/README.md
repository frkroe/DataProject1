# RAW DATA
Raw data have been downloaded for various sources. Please find further details on the used datasets below:

## Products from IKEA
- [Link to Kaggle-Dataset](https://www.kaggle.com/datasets/ahmedkallam/ikea-sa-furniture-web-scraping)
- The data was requested from the IKEA Saudi Arabian website by 4/20/2020. 
- 2962 rows
- 13 features: 
    - **item_id**: item id wich can be used later to merge with other IKEA dataframes
    - **name**: the commercial name of items
    - **category**: the furniture category that the item belongs to (Sofas, beds, chairs, Trolleys,…)
    - **Price**: the current price in Saudi Riyals as it is shown in the website by 4/20/2020
    - **old_price**: the price of item in Saudi Riyals before discount
    - **Short_description**: a brief description of the item
    - **full_Description**: a very detailed description of the item. Because it is long, it is dropped from the final dataframe, but it is available in the code in case it needs to be analyzed.
    - **designer**: The name of the designer who designed the item. this is extracted from the full_description column.
    - **size**: the dimensions of the item including a lot of details.As a lot of dimensions mentioned and they vary from item to item,
    the most common dimensions have been extracted which are: Height, Wideh, and Depth. This column is dropped from the final dataframe, but it is available in the code in case it is needed.
    - **width**: Width of the item in Centimeter
    - **height**: Height of the item in Centimeter
    - **depth**: Depth of the item in Centimeter
    - **sellable_Online**: if the item is available for online purchasing or in-stores only (Boolean)
    - **other_colors**: if other colors are available for the item, or just one color as displayed in the website (Boolean)
    - **link**: the web link of the item

## Random User Generator API 
- [Link to API](https://randomuser.me/api)
- Random User Generator is a free, open-source API for generating random user data. The API will provide a JSON object (default format) that can be parses and applied to one's application. 
- Version 1.4 by 7/4/2022
- Features:
    - gender
    - name
    - location
    - email
    - login
    - registered
    - dob
    - phone
    - cell
    - id
    - picture
    - nat

## Cities in Saudi Arabia
- [Link to List of Cities](https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Saudi_Arabia)
- The data was requested from the Central Department of Statistics and Information (in Arabic). The page was last edited on 20 October 2022, at 11:28 (UTC).
- 47 rows (cities that cannot be identied as cities in Tableau have been removed)
- 1 feature: name of city (other features have been removed due to non-necessity)

## Top 200 Influencers
- [Link to Kaggle-Dataset](https://www.kaggle.com/datasets/syedjaferk/top-200-instagrammers-data-cleaned?select=top_200_instagrammers.csv)
- This dataset comprises of 200 top influencers profile data of instagram, downloaded in Nov 2022
- 200 rows
- 20 features:
    - **Username**: Name of the influencer's account
    - **Channel name**: Name of the Channel
    - **Country**: Influencer's country
    - **Url**: Instagram Url
    - **Main Topic**: Main topic of the page
    - **Main Video Category**: Category of the reels and video
    - **Like**: Total Likes count
    - **Likes Avg.**: Average likes
    - **Post**: Total Posts
    - **Followers**: Total number of the followers
    - **Boost Index**: Boost index value
    - **Comments Avg.**: Average comments number.
    - **Views Avg**: Average Views.
    - **Avg. 1 Day**: Average views perday
    - **Avg. 3 Day**: Average views for 3 days
    - **Avg. 7 Day**: Average views for 7 days
    - **Avg. 14 Day**: Average views for 14 days
    - **Avg. 30 Day**: Average views for 30 days
    - **Engagement Rate**: Percentage of Engagement with users.
    - **Engagement Rate (60 Days)**: Percentage of Engagement with users for 60days