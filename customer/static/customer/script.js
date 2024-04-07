console.log("script.js is loaded and running");

document.addEventListener('DOMContentLoaded', function() {
    const cartButton = document.getElementById('cartButton');
    const cartPopup = document.getElementById('cartPopup');
    const cartItems = document.getElementById('cartItems');
    const cartCount = document.getElementById('cartCount');
    let cart = {};

    // Toggle the cart popup
    cartButton.addEventListener('click', function() {
        cartPopup.style.display = cartPopup.style.display === 'none' ? 'block' : 'none';
    });

    // Add items to the cart
    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', function() {
            const id = this.getAttribute('data-id');
            const name = this.getAttribute('data-name');
            const price = parseFloat(this.getAttribute('data-price'));
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
                <span>${item.name} - $${item.price}</span>
                <label for="qty-${id}">Qty:</label>
                <input type="number" id="qty-${id}" class="quantity-input" value="${item.quantity}" data-id="${id}" min="1">
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




// document.addEventListener('DOMContentLoaded', function() {
//     const cartButton = document.getElementById('cartButton');
//     const cartPopup = document.getElementById('cartPopup');
//     let cart = {};

//     cartButton.addEventListener('click', function() {
//         cartPopup.style.display = cartPopup.style.display === 'none' ? 'block' : 'none';
//     });



//     function updateCartUI() {
//         const cartItems = document.getElementById('cartItems');
//         cartItems.innerHTML = ''; // Clear existing items
    
//         Object.keys(cart).forEach(id => {
//             const item = cart[id];
//             const itemDiv = document.createElement('div');
//             itemDiv.classList.add('cart-item');
//             itemDiv.innerHTML = `
//                 <span>${item.name}</span>
//                 <label for="qty-${id}">Qty:</label>
//                 <input type="number" id="qty-${id}" class="quantity-input" value="${item.quantity}" data-id="${id}" min="1">
//             `;
//             cartItems.appendChild(itemDiv);
//         });
    
//         // Update cart count
//         document.getElementById('cartCount').textContent = Object.keys(cart).length;
//     }
    

//     // Event delegation for quantity changes
//     document.getElementById('cartItems').addEventListener('change', function(event) {
//         if (event.target.tagName === 'INPUT' && event.target.type === 'number') {
//             const id = event.target.getAttribute('data-id');
//             const quantity = parseInt(event.target.value);
//             if (cart[id] && !isNaN(quantity)) {
//                 cart[id].quantity = quantity;
//             }
//         }
//     });

//     // Example usage
//     // addItemToCart('1', 'Product Name', 1);
// });













document.getElementById('cartItems').addEventListener('change', function(event) {
    if (event.target.classList.contains('quantity-input')) {
        const id = event.target.getAttribute('data-id');
        const quantity = parseInt(event.target.value);
        if (cart[id] && !isNaN(quantity) && quantity > 0) {
            cart[id].quantity = quantity;
            updateCartUI(); // Refresh the cart UI with the new quantity
        } else {
            event.target.value = cart[id] ? cart[id].quantity : 1; // Reset to previous value if invalid
        }
    }
});
