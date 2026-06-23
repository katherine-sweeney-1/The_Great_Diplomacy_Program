const cors = require("cors");
const express = require("express");
const https = require ("https");
const fetch = require ("node-fetch")
const PORT = 443

app.use(express.json());

"const API_ENDPOINT = 'https://letsplaydiplomacy.com/home'";


app.use(cors({
    origin: "https:/letsplaydiplomacy.com/home",
    //origin: "http://127.0.0.1:5502/TGDP_Website/Publish/home.html",
    methods: ["GET", "POST"],
    allowedHeaders: ["Content-Type", "Authorization"]
}))

app.get("/home", cors(corsOptions), function(req, res, next){
    res.json(({msg: "hello world!!!"}));
});

app.listen(PORT, function(){
    console.log("listening on port 443");
});

console.log("is the server working");

export const handler = async () => {
    console.log("checking")
    responseText.innerText = response
    responseText.innerText = JSON.stringify(response)
    console.log(xhr.response);
    console.log(console.log.responseText);
  return {
    statusCode: 200,
    body: JSON.stringify({
      message: "Hello World!",
    }),
  }
}


app.post("/home", (req, res) => {
    console.log("javascript backend test 1")
    https.get("https://letsplaydiplomacy.com/home")
    console.log("javascript backend test 2")
    const data_dict = {}
    const home_url = "https://letsplaydiplomacy.com/home"
    console.log("checking example save output")
    const data_button = document.getElementById("data-input-2").value
    data_button.addEventListener("click", async_ => {
        try {
            Promise.all(
                URLSearchParams.map(async (data_button) => {
                    const response = await fetch(data_button);
                }),
            );
            console.log("checking")
            //const response = await fetch ("/TGDP_Home.html")
            if (! response.ok){
                throw new Error("Response status: ${response}");
                }
            const result = response.json();
            console.log.result();
        }
        catch (error) {
        console.error(error.message);
        console.log("compeleted", response);
        }
    })
})

async function getPostRequest(){
    const url = "https://letsplaydiplomacy.com/home"
    try {
        let response = await fetch(url);
        if (!response.ok){
            throw new Error ("response status ${response.status}")
        }
        const result = await response.json();
        console.log(result);
    } catch (error) {
        console.error(error.message);
    }
}