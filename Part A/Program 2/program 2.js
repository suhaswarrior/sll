function calculate(){ // Function to calculate the total amount
    x=document.getElementById("price").value; // Get the price of the item
    y=document.getElementById("quantity").value; // Get the quantity of the item
    res=x*y; // Calculate the total amount
document.getElementById("result").innerHTML=res; // Display the total amount
} // End of function
function but(){ // Function to display the button
    alert("Paid") // Display the message
} // End of function