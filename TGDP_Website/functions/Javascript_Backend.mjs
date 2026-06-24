/*
const cors = require("cors");
const express = require("express");
const https = require ("https");
*/
//const fetch = require ("node-fetch")
//const PORT = 443
import cors from "cors";
import express from "express";
import https from "https";
//import http from "http";
import fetch from "node-fetch"
const app = express();
const PORT = 5002

//app.use(express.json());

//app.use(cors())

const corsOptions = {
    origin: "http://127.0.0.1:5502/TGDP_Website/Publish/home.html",
    methods: ["GET", "POST"], 
};

app.use(cors(corsOptions));

app.use(cors({
    origin: "https://letsplaydiplomacy.com/home",
    //origin: "http://127.0.0.1:5502/TGDP_Website/Publish/home.html",
    methods: ["GET", "POST"],
    //credentions: true,
    //allowedHeaders: ["Content-Type", "Authorization"]
}));



app.use(function(req, res, next) {
    console.log("does app.use run?")
    //res.setHeader("Access-Control-Allow-Origin", "http://127.0.0.1:5502/TGDP_Website/Publish/home.html");
    res.setHeader("Access-Control-Allow-Origin", "https://letsplaydiplomacy.com/home");
    res.setHeader("Access-Control-Allow-Methods", "GET, POST");
    res.setHeader("Access-Control-Allow_Headers", "Content-Type");
    console.log("doest the res.setHEaders work?");
    next();
})

//console.log("is the server working");

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

app.get("/home", (req, res) => {
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

app.listen(PORT, function(){
    console.log("listening on port 443");
});


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