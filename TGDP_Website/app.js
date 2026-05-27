const express = require("express")
const request = require("request");

app = express();
const PORT = 3000;

app.get("/home", function(req, res){
    request("http://127.0.0.1:5500/example_save_output", function(error, response, body){
        console.error("error:", error); // print error
        console.log("statusCode:", response && response.statusCode); //print response
        console.log("body:", body) //print received data
        res.send(body); //display response on website
    });
});
app.listen(PORT, function(){
    console.log("listening on port 3000");
})

/*
app.route("/")
def home():
    #europe_map_url = "/home/katherine/Documents/The_Great_Diplomacy_Program/GUI/Europe_Map.png"
    europe_map_url = "Static/Europe_Map.png"
    #europe_map_url = "/home/katherine/Documents/The_Great_Diplomacy_Program/TGDP_Website/Static/Europe_Map_For_Website.png"
    return render_template("TGDP_Home.html", image_url = europe_map_url)
/*
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