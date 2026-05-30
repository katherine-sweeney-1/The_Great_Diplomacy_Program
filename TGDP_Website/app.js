const cors = require("cors");
const express = require("express");
const request = require("request");

const 
app = express();
const PORT = 5501;
/*
app.get("/", function(req, res){
    request("http://127.0.0.1:5500/example_save_output", function(error, response, body){
        console.error("error:", error); // print error
        console.log("statusCode:", response && response.statusCode); //print response
        console.log("body:", body) //print received data
        res.send(body); //display response on website
    });
});
*/
app.get("/", (req, res) => {
    res.send("GET request to the homepage")
});

app.post("/", (req, res) => {
    res.send("POST request to the homepage")
});

app.get("/about", (req, res) => {
    res.send("About page")
});

app.all('*', (req, res) =>{
    res.status(404).send("404 - Page not found response")
});


/*
# runs if I use http://127.0.0.1:5000/hello
if __name__ == "__main__":
    app.run("localhost", 5000, debug = True)
*/