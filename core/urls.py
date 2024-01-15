from django.urls import path
from core.views import checkout_view, index, about_us, category_list_view, order_completed_view, product_list_view, product_detail_view, category_product_list_view, customer_dashboard, search_view, filter_product, upload_image, projects, approve_quotation, wishlist_view, add_to_wishlist, remove_from_wishlist, add_to_cart, cart_view, delete_item_from_cart, update_cart, warranty_policy, refund_policy, returns_and_cancellations, privacy_policy, terms_and_conditions, faq_view, confirm_payment


app_name = 'core'

urlpatterns = [
    # homepage
    path('', index, name='index'),
    
    # For Categories
    path('category/', category_list_view, name='category-list'),
    path('category/<cid>/', category_product_list_view, name='category-product-list'),
    
    # For products
    path('products/', product_list_view, name='product-list'),
    path('products/<pid>/', product_detail_view, name='product-detail'),
    
    # About us
    path('about-us/', about_us, name='about-us'),
    
    # Customer Dashboard
    path('dashboard/', customer_dashboard, name='dashboard'),
    
    path('confirm_payment/<int:invoice_id>', confirm_payment, name='confirm_payment'),
    
    # To approve quotations
    path('approve_quotation/<int:quotation_id>/', approve_quotation, name='approve_quotation'),
    
    # Search
    path('search/', search_view, name='search'),
    
    # Filter product URL
    path('filter-products/', filter_product, name='filter-product'),
    
    
    # path('ajax-contact-form/', ajax_contact_form, name='ajax-contact-form'),
    
    # To upload images from Forum page
    path('dashboard/upload/', upload_image, name='upload_image'),
    path('projects/', projects, name='projects'),
    
    
    # Wishlist page URL
    path('wishlist/', wishlist_view, name='wishlist'),
    
    # Adding to wishlist
    path('add-to-wishlist/', add_to_wishlist, name='add-to-wishlist'),
    
    # Deleting from wishlist
    path('remove-from-wishlist/', remove_from_wishlist, name='remove-from-wishlist'),
    
    
    #Add to cart URL
    path('add-to-cart/', add_to_cart, name='add-to-cart'),
    
    # checkout url
    path('checkout/', checkout_view, name='checkout'),
    
    # Order Completed
    path('checkout/core/order-completed/', order_completed_view, name='order-completed'),
    
    # Cart page URL
    path('cart/', cart_view, name='cart'),
    
    # Delete item from cart
    path('delete-from-cart/', delete_item_from_cart, name='delete-from-cart'),
    
    # Update items in cart
    path('update-cart/', update_cart, name='update-cart'),
    
    
    # Warranty Policy
    path('warranty-policy/', warranty_policy, name='warranty-policy'),
    
    
    # Refund Policy
    path('refund-policy/', refund_policy, name='refund-policy'),
    
    
    # Returns and cancellations
    path('returns-and-cancellations/', returns_and_cancellations, name='returns-and-cancellations'),
    
    
    # Privacy Policy
    path('privacy-policy/', privacy_policy, name='privacy-policy'),

    
    # Terms and conditions
    path('terms-and-conditions/', terms_and_conditions, name='terms-and-conditions'),
    
    # FAQ
    path('FAQ/', faq_view, name='FAQ'),
    
    
]