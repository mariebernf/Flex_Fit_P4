# Flex_Fit_P4

View here:

## Description

Flex Fit is an e-commerce web application built using Django. Flex Fit sells fitness clothing for men and women. The site allows users to browse clothing products, select sizes, add items to a shopping cart, and complete a secure checkout process.

The application supports user authentication, enabling users to create accounts, log in and view their order history. Admin users can manage products, stock levels and customer orders through the Django admin interface.

The web site focuses on delivering core e-commerce functionality with a clean, minimal design and a responsive user experience across desktop, tablet and mobile devices.

## Project requirments

This project was developed to meet the requirements of a full-stack Django web application with CRUD functionality, authentication, and a relational database.

The key project requirements include:

### Core Requirements:

* Build a full-stack web application using Django.

* Implement CRUD functionality for managing products and orders.

* Use a relational database (SQLite during development).

* Apply user authentication and authorisation.

* Ensure the application is responsive and user-friendly.

* Deploy the project to a live hosting platform.

### E-commerce Functionality

* Allow users to browse products with images, prices, and size options.

* Enable users to add, update, and remove items from a shopping cart.

* Provide a secure checkout process with order confirmation.

* Store completed orders in the database.

### Security and Access Control

* Restrict access to certain pages to authenticated users only.

* Display navigation options based on user login status.

* Implement custom 403 and 404 error pages.

### Admin Functionality

* Allow admin user to add, edit, and delete products.

* Mangage stock levels through the admin interface.

* View customer orders and order line items.

## User stories

## Features

### User Accounts and Authentication

* Users can create an account, log in, and log out securely.
* Authenticated users can view their personal order history.
* Restricted pages are protected so only logged in users can access them.

### Product Browsing

* Users can browse products displayed with images, prices and size options.
* Featured products are highlighted on the homepage.
* Product images are clickable for easy navigation to product detail page.

### Shopping Cart

* Users can add products to the cart.
* A cart icon in the navigation bar displays the current cart status.
* Users can update quanties or remove items from the cart.

### Checkout and Orders

* Secure checkout process with order summary.
* Orders are saved to the database upon successful checkout.
* Users receive an order confirmation page displaying their order number.
* Logged in users can view past orders via the "My Orders" page.

### Admin Management

* Admin users can add, edit, and delete products through the Django admin panel.
* Stock levels are managed per product.
* Orders and order line items are visible in the admin interface.

### Responsive Design

* The site is fully responsive and works across desktop, tablet and mobile devices.
* Built using Bootstrap to ensure consistent layout and styling.

### Error Handling

* Custom 403 and 404 error pages are implemented for improved user experience.
* Authentication prevents unauthorised access to restricted pages.

## Future Features

* **Advanced Product Variations:** Implement a system to manage sizes and other attributes like colour as variations of a single product in the admin interface, simplifying stock management.
  
* **Improved Search and Filtering:** Add filters for size, price and category to help users find products more easily.
  
* **Enhanced User Accounts:** Include features like a wishlist, favorites and profile management.

* **Separate Men's and Women's Pages:** Add separate shopping pages for Men's and Women's products to improve naviagation and filtering and to improve user experience.

* **Saved Delivery Details:** Allow logged in users to save delivery information to speed up future checkouts.

## Design

### Design Limitations: 

**Product Size Variations:**

Product sizes ( S, M, L ) are implemented as separate products instead of selectable size options within a single product in the admin interface.

On the website, users can still select their size but in the admin, each size is managed as an individual product. This design keeps the product, cart, checkout, and order logic simple and reliable within the project timeframe. Each size is treated as its own product with an individual stock level, which helps ensure accurate ordering and stock management.

As a result, the same product appears multiple times in the shop, once per size. A more advanced size variation system would be implemented in the future and is documented in the Future Features section.

**Men's and Women's Product Pages:**

Separte Men's and Women's pages were not implemented in this project. All products are displayed on a single shop page.

This decision was made to keep the project focused on core e-commerce funtionality within the project timeframe. Products are still labelled by gender, allowing users to browse easily. Separate category pages are planned as a future feature.

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

* Python – Core programming language used to build the backend logic.

* Django – Python web framework used to develop the application.

* HTML – Used for structuring the website content.

* CSS – Used for custom styling and layout.

* Bootstrap – Frontend framework used for responsive design and layout.

* SQLite – Database used during development.

* Git – Version control system used to track changes.

* Heroku – Cloud platform used to deploy the application.

## Tools used

* GitHub – Used to host the project repository.

* VS Code – Code editor used to write and manage the project.

* Django Admin – Used to manage products, orders, and site data.

* Chrome DevTools – Used for debugging, testing responsiveness, and inspecting elements.

* Google Fonts – Used to import the Lato font for site typography.

* TinyPNG – Used to compress images to improve site performance.

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

**User testing:**

**User Feedback Testing:** ( Testing carried out with family and friends. ) 

During testing, it was noted that there was no button to continue shopping from the cart page. 

**Fix:** A "Continue Shopping" button was added to the cart page, linking back to the products page to improve user navigation.

**It was also noted:** 

* The product sizes appear as separate listings for the same product. This was a known design limiation and is documented in the Design Limiations and Future Features sections.

* That there is not a separte Men's and Women's shopping page. The reason for this is documented in the Design Limiations section and is also included in the Future Features section.

**General Feedback:** 

They reported the site was easy to navigate and liked the design of the website.

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
|  |  |  |  |

## Credits

### **Content and Learning Resources:**

**Code Institute - Boutique Ado Tutorial**

This project was influenced by the *Boutique Ado* tutorial provided by Code Institute. The tutorial was used as a learning reference for Django e-commerce concepts. The tutorial is available via the Code Institute learning platform.

### Learning and Libraries:

- [Django Documentation](https://docs.djangoproject.com/)

- [Bootstrap Documentation](https://getbootstrap.com/docs/)

### Media and Assets:

Images used throughout the site were sourced from:

- [Pexels](https://www.pexels.com/)

- [Unsplash](https://unsplash.com/)

### Image Optimisation:

- [TinyPNG](https://tinypng.com/) was used to compress images and improve performance.

### Favicon: 

- Favicon was generated using [Favicon.io](https://favicon.io/).

### Design and Typography:

**Google Fonts:**

- [Lato](https://fonts.google.com/specimen/Lato) font was imported from Google Fonts and used as the primary typography across the site.

### Wireframes:

- Wireframes were created using [Canva](https://www.canva.com/) to plan layout and page structure.

### Icons:

- Social media and user interface icons were sourced from [Font Awesome](https://fontawesome.com/).

## Acknowledgements

* **Code Institute for providing the learning materials, support and guidance.**

* **Family and friends who participated in user testing and provided valuable feedback.**












 
