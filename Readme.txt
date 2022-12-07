This is a django rest framework application for seller and buyer vendors which mainly goals is:
  1. Buyer Can view all products and cannot add products
  2. Seller can add products and view only his products
  3. Custom Authentication system
  4. Permission and groups
  5. User can add product to wishlist table
Achieved:
  ✅ the system achieved to make all of the apis authenticated (required to sign in to access it).
  ✅ the system also successfully created API tokens for each user and every new user is created (if admin or not).
  ✅ the system created groups for buyers and sellers and assigned permissions (3,4) (manualy through admin panel).
Remaining:
  ✅to assign each user token the restricts and allowance because each token can access any api for now.
  you can test the token (token keys are saved in the authtoken_token in sqlite table) through the curl command below:
  http GET 127.0.0.1:8000/products/ 'Authorization: Token the_token_key_value_in_the_sqlite_database'
  ✅ once each user token has assigned its restricts goal 1,2 will be achieved.
  ✅ creating wishlist for the buyer so he can add products to his wishlist.
