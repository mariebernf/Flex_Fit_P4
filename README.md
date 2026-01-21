# Flex_Fit_P4

View here:

## Description

## Project requirments

## User stories

## Features

## Future Features

* **Advanced Product Variations:** Implement a system to manage sizes and other attributes like colour as variations of a single product in the admin interface, simplifying stock management.
  
* **Improved Search and Filtering:** Add filters for size, price and category to help users find products more easily.
  
* **Enhanced User Accounts:** Include features like a wishlist and profile management.

## Design

### Design Limitation: Product Size Variations

Product sizes ( S, M, L ) are implemented as separate products instead of selectable size options within a single product in the admin interface.

On the website, users can still select their size but in the admin, each size is managed as an individual product. This design keeps the product, cart, checkout, and order logic simple and reliable within the project timeframe. Each size is treated as its own product with an individual stock level, which helps ensure accurate ordering and stock management.

As a result, the same product appears multiple times in the shop, once per size. A more advanced size variation system would be implemented in the future and is documented in the Future Features section.

### Database Schema

### Colour Scheme

| Element                | Colour / Class          | Purpose |
|------------------------|------------------------|---------|
| Navbar background.     | Dark gray / Bootstrap bg-dark (#212529). | Strong contrast, clean and modern look. Matches the footer. |
| Navbar text and buttons.| White (#FFFFFF).         | High readability against the dark background. |
| Footer background.      | Dark gray / Bootstrap bg-dark (#212529). | Matches the navbar for a consistent layout. |
| Page background.        | White (#FFFFFF).         | Clean and makes the content easy to read. |

### Button Styling

| Element                    | Colour      | Purpose |
|----------------------------|------------|---------|
| Add to Cart / Primary Action.| Green.    | Indicates a positive action. |
| Edit button.                 | Blue.       | Standard action for editing content. |
| Delete button.               | Red.        | Brings attention to a destructive action. |
| Shop now (Hero Section).     | White.        | Stands out againt the dark background, encourages users to start shopping. |
| View Product Buttons.        | Bootstrap btn-dark. | Directs users to the products. |

### Typography

- **Primary Font:** Lato from Google Fonts. 
- **Fallback Font:** Sans-serif in case Lato doesn’t load.

Lato is clean and highly readable. It complements the minimalist colour scheme of the website and works well with Bootstrap styling.

### Homepage Styling

* **Hero Section:** Hero section has a dark overlay, large heading, and a call to action button.

* **Intro Section:** Centered text with a muted paragraph, which highlights the brands mission.

* **Featured Products:** Responsive grid using Bootstrap cards, showing image, name, price, and a "View Product" button.

* **Buttons:**
  
  **Shop Now:** Light button on the dark hero background for contrast.
  
  **View Product and View All Products:** Dark and outling buttons to stand out.

## Wireframe

## Technologies used

## Tools used

## Deployment

**Deployment steps:**

**Forking the Repository:**

**Cloning the Github Respository:**

## Security

- User login and registration are handled using Django Allauth.
- Sensitive pages such as order history are protected using Django’s "login_required" decorator.
- Users who are not logged in are redirected to the login page.
- Navigation links change based on whether the user is logged in or not.
- Direct URL access to protected pages is blocked.

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
|||||
| Cart page did not load. | Missing ( cart: ) namespace in {% url %} template tags. | Added the correct ( cart: ) namespace to all cart-related template URLs. | The cart page now loads correctly. The quanity and remove funciton now work. |
|||||
| Checkout success page returned "Template does not exist error". | The checkout success html file was placed outside of the orders/templates/orders folders. | File was placed in the correct folder. | Page now loads correctly. |
|||||
| Users could not complete a purchase after adding items to the cart. | There was no button on the cart page to go to the checkout page. | A "Proceed to Checkout" button was added to the cart page. | Users can now move from the cart to the checkout page and complete their order. |
|||||
| Checkout success page came up NoReverseMatch error when adding a "Continue Shopping" link. | Template was not using correct URL route for the button. | Updated template to use the correct URL ( products:product_list ). | "Continue Shopping" button now works and redirects to the product list page. |
|||||
| Signup failed with error "ConnectionRefusedError". | Django tried to send a confirmation email during signup, but there is no email server running. | Added "EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' to settings.py. | Signup works successfully. |
|||||
| Orders placed by logged in users were not appearing in the order history page. | Orders were not linked to the logged in user. | Added a user foreign key to the Order model and assigned "order.user = request.user" during checkout. | Orders now appear correctly in the order history page for logged in users. |
|||||
| Cart caused a page error. | Cart session data was stored in two different formats ( numbers or dictionary with size ). | Updated the cart context processor to handle both types. | Cart now works correctly without errors. |
|||||
| . | . |  |  |

## Credits


 
