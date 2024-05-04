console.log("Base js sanity check");

// Get Stripe publishable key
fetch("config/")
.then((result) => { 
    if (!result.ok) {
        throw new Error('Failed to fetch configuration data');
    }
    return result.json(); 
})
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);

  // Event handler
  let submitBtn = document.querySelector("#submitBtn");
  if (submitBtn !== null) {
    submitBtn.addEventListener("click", () => {
        console.log("Button clicked!"); // Log message to console when button is clicked
        // Get Checkout Session ID
        fetch("create-checkout-session/")
        .then((result) => { 
            if (!result.ok) {
                throw new Error('Failed to create checkout session');
            }
            return result.json(); 
        })
        .then((data) => {
            console.log("Checkout session created:", data); // Log checkout session data
            // Redirect to Stripe Checkout
            return stripe.redirectToCheckout({sessionId: data.sessionId})
        })
        .then((res) => {
            console.log("Redirect result:", res); // Log redirect result
        })
        .catch((error) => {
            console.error('Error:', error.message);
            // Send error message to server using fetch or any other method
            // Example: sendErrorToServer(error.message);
        });
    });
  }
})
.catch((error) => {
    console.error('Error:', error.message);
    // Send error message to server using fetch or any other method
    // Example: sendErrorToServer(error.message);
});