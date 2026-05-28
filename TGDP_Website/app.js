const express = require("express")
//const request = require("request");

app = express();
const PORT = 3000;
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
app.listen(PORT, function(){
    console.log("listening on port 5501");
});
/*
app.get("/", (req, res) => {
    res.send("GET request to the homepage")
});

app.post("/", (req, res) => {
    res.send("POST request to the homepage")
});
*/
app.get("/about", (req, res) => {
    res.send("About page")
});
/*
app.all('*', (req, res) =>{
    res.status(404).send("404 - Page not found response")
});
*/

app.listen(PORT, () => {
    console.log("example listening at localhost:${PORT}")
})

app.post("/TGDP_Home.html", (req, res) => {
    const data_dict = {}
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
    
/*  
    console.log("received data -save output: ${data_button")
    data_dict["data from site"] = data_button
    var file = require("file"),  str  = data_dict;
    // e = event
    file.open("/Example_Submission.json", "a", 666, function(e, id) {
        file.write(id, "string to append to file", null, "utf8", function(){
            file.close(id, function(){
                console.log("file closed");
            });
        });
    });
});
*/
/*
app.route("/")
def home():
    #europe_map_url = "/home/katherine/Documents/The_Great_Diplomacy_Program/GUI/Europe_Map.png"
    europe_map_url = "Static/Europe_Map.png"
    #europe_map_url = "/home/katherine/Documents/The_Great_Diplomacy_Program/TGDP_Website/Static/Europe_Map_For_Website.png"
    return render_template("TGDP_Home.html", image_url = europe_map_url)

@app.route("/example", methods = ["GET", "POST"])
def users():
    print("checking example")
    if request.method == "GET":
        with open("TGDP_Website/example_json_data.json", "r") as file_input:
            data = json.load(file_input)
            data.append({
                "owner": "Nicola",
                "pets": ["Mango"]
            })
            return flask.jsonify(data)
    if request.method == "POST":
        received_data = request.get_json()
        print(f"received data: {received_data}")
        message = received_data["data 1"]
        return_data = {
            "status": "success",
            "message": f"received: {message}"
        }
        return flask.Response(response = json.dumps(return_data), status = 201)



@app.route("/example_save_output", methods = ["GET", "POST"])
def users_save_output():
    print("checking example save output")
    if request.method == "POST":
        received_data = request.get_json()
        print(f"received data - save output: {received_data}")
        message = received_data["data 2"]
        return_data = {
            "status": "success",
            "message": f"received: {message}"
        }
        with open("TGDP_Website/Example_Submissions.json", "a") as file_input:
            #json.dump(data, file_input, indent = 4)
            file_input.write(json.dumps(received_data) + "\n")
            #return flask.jsonify(file_input)
        return flask.Response(response = json.dumps(return_data), status = 201)


# runs if I use http://127.0.0.1:5000/hello
if __name__ == "__main__":
    app.run("localhost", 5000, debug = True)
*/