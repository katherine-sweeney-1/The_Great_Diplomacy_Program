


image_path_list = "Static/Europe_Map_For_Website.png"
function iterate_images (image_path_list){

    return "hello";
}

const express = require("express"); // import express module
const app = express(); //initializes a new express application
app.use(express.json()); // used to parse json boddies
app.listen(5000, () => console.log("Server running on port 3000")) //starts server on port 3000

//Get Endpoint
app.get("/api/items", (req, res) => { //define get route, get request is made to api/items and callback function is executed
    res.send("List of items"); //return the string "list of items"
});

//Post endpoint
app.post("/api/items", (req, res) => { // Handles post requests
    const newItem = req.body; // Data sent in the request body
    // eventually use this to write data to a resource such as a database
    res.send("Item added : ${newItem.name}");
});

app.put("/api/items/:id", (req, res) => { //handles put request, 
    // id of resource to update is often passed as a query parameter or URI parameter
    const itemId = req.params.id; //Access URL parameter
    // use req.params.id to fetch the id parameter from the URL
    // in real life you'd make a database call to update the resource with
    // data usually found in the request body
    // and then return a boolean stating whether the update was procesed
    res.send("Item with ID ${itemID} updated");
});

app.delete("api.items/:id", (req, res) => {
    const itemId = req.params.id;
    res.send("Item with ID ${itemId} deleted");
});