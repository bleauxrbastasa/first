console.log("script.js is loaded and running");



document.addEventListener('DOMContentLoaded', function () {
    const cartButton = document.getElementById('cartButton');
    const cartPopup = document.getElementById('cartPopup');
    const cartItems = document.getElementById('cartItems');
    const cartCount = document.getElementById('cartCount');
    let cart = {};

    cartButton.addEventListener('click', () => {
        cartPopup.classList.toggle('show');
    });

    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', function () {
            const id = this.getAttribute('data-id');
            const quantity = parseInt(this.previousElementSibling.value);
            addItemToCart(id, quantity);
        });
    });

    function addItemToCart(id, quantity) {
        if (cart[id]) {
            cart[id] += quantity;
        } else {
            cart[id] = quantity;
        }
        updateCartUI();
    }

    function updateCartUI() {
        cartItems.innerHTML = ''; // Reset cart items
        Object.keys(cart).forEach(id => {
            const itemElement = document.createElement('div');
            itemElement.textContent = `Item ${id}: ${cart[id]}`;
            cartItems.appendChild(itemElement);
        });
        cartCount.textContent = Object.keys(cart).length; // Update cart count
    }




});


document.addEventListener('DOMContentLoaded', function() {
    const cartButton = document.getElementById('cartButton');
    const cartPopup = document.getElementById('cartPopup');
    let cart = {};

    cartButton.addEventListener('click', function() {
        cartPopup.style.display = cartPopup.style.display === 'none' ? 'block' : 'none';
    });

    // Example function to add an item to the cart
    function addItemToCart(id, name, quantity) {
        if (!cart[id]) {
            cart[id] = { name, quantity };
        } else {
            cart[id].quantity += quantity;
        }
        updateCartUI();
    }

    function updateCartUI() {
        const cartItems = document.getElementById('cartItems');
        cartItems.innerHTML = ''; // Clear existing items
    
        Object.keys(cart).forEach(id => {
            const item = cart[id];
            const itemDiv = document.createElement('div');
            itemDiv.classList.add('cart-item');
            itemDiv.innerHTML = `
                <span>${item.name}</span>
                <label for="qty-${id}">Qty:</label>
                <input type="number" id="qty-${id}" class="quantity-input" value="${item.quantity}" data-id="${id}" min="1">
            `;
            cartItems.appendChild(itemDiv);
        });
    
        // Update cart count
        document.getElementById('cartCount').textContent = Object.keys(cart).length;
    }
    

    // Event delegation for quantity changes
    document.getElementById('cartItems').addEventListener('change', function(event) {
        if (event.target.tagName === 'INPUT' && event.target.type === 'number') {
            const id = event.target.getAttribute('data-id');
            const quantity = parseInt(event.target.value);
            if (cart[id] && !isNaN(quantity)) {
                cart[id].quantity = quantity;
            }
        }
    });

    // Example usage
    // addItemToCart('1', 'Product Name', 1);
});


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
