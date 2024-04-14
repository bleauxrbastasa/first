console.log("script.js is loaded and running");

// AJAX
headers: {
    'Content-Type'; 'application/json',
    'X-CSRFToken'; getCookie('csrftoken')  // Call directly here
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// TOGGLE CART POPUP
cartButton.addEventListener('click', function() {
    console.log('Cart button clicked.');
    console.log('Current display:', cartPopup.style.display); // Add this to debug
    cartPopup.style.display = cartPopup.style.display === 'none' ? 'block' : 'none';
});

var cart = {}; // Global scope

document.addEventListener('DOMContentLoaded', function() {
    const cartButton = document.getElementById('cartButton');
    const cartPopup = document.getElementById('cartPopup');
    const cartItems = document.getElementById('cartItems');
    const cartCount = document.getElementById('cartCount');

    // Add items to the cart
    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', function() {
            const id = this.getAttribute('data-id');
            const name = this.getAttribute('data-name');
            const price = parseFloat(this.getAttribute('data-price')); // Ensure you have a data-price attribute in your HTML
            const quantity = 1; // Default quantity to 1, adjust as needed
            addItemToCart(id, name, price, quantity);
        });
    });

    // Function to add/update an item in the cart
    function addItemToCart(id, name, price, quantity) {
        if (!cart[id]) {
            cart[id] = { name, price, quantity };
        } else {
            cart[id].quantity += quantity; // Increment quantity if item already in cart
        }
        updateCartUI();
    }

    // Update the cart UI
    function updateCartUI() {
        cartItems.innerHTML = ''; // Clear existing cart items
        Object.keys(cart).forEach(id => {
            const item = cart[id];
            const itemDiv = document.createElement('div');
            itemDiv.classList.add('cart-item');
            itemDiv.innerHTML = `
                <span>${item.name} - $${item.price.toFixed(2)} x ${item.quantity}</span>
                <input type="number" class="quantity-input" value="${item.quantity}" data-id="${id}" min="1">
            `;
            cartItems.appendChild(itemDiv);
        });
        cartCount.textContent = Object.keys(cart).length; // Update cart count
    }

    // Handle quantity changes in the cart
    cartItems.addEventListener('change', function(event) {
        if (event.target.classList.contains('quantity-input')) {
            const id = event.target.getAttribute('data-id');
            const quantity = parseInt(event.target.value);
            if (cart[id] && !isNaN(quantity) && quantity > 0) {
                cart[id].quantity = quantity; // Update quantity
                updateCartUI(); // Refresh the cart UI with the new quantity
            } else {
                event.target.value = cart[id] ? cart[id].quantity : 1; // Reset to previous value if invalid
            }
        }
    });


});

// // Function to get CSRF token from cookies
// function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         const cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             const cookie = cookies[i].trim();
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }

// Helper function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


