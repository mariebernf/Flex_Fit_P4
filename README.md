# Flex_Fit_P4

View here:

## Description

## Project requirments

## User stories

## Features

## Future Features

## Design

## Database Schema

## Colour scheme

## Typography

## Wireframe

## Technologies used

## Tools used

## Deployment

**Deployment steps:**

**Forking the Repository:**

**Cloning the Github Respository:**

## Testing

## Lighthouse reports

## W3C Markup Validation

## W3C CSS Validator

**Manual testing:**

Responsiveness: 

## Bugs and Fixes

| Bug | Cause | Solution | Result |
|-----|-------|----------|--------|
| CSS files not loading in templates. | Django didn’t know about the static folder. | Added STATICFILES_DIRS = [BASE_DIR / "static"] in settings.py. | CSS now loads correctly and pages display styling as expected. |
|||||
| Product images not shown. | Template did not have code to display images. | Added product.image.url to products.html. | Images now display for products. |
|||||
| Product card images did not display correctly. | Images had different dimensions, causing uneven card layouts. | Applied bootstrap card-img-top and fixed image height using CSS with object-fit:cover. | Product images now display correctly. |
|||||
| Product grid was not responsive on smaller screen sizes, it remained in a 3 column layout. | The viewport meta tag was missing from base.html.  | Added meta name="viewport" content="width=device-width, initial-scale=1" to the base template. | The product grid now stacks correctly on smaller screen sizes. |



## Credits


 
