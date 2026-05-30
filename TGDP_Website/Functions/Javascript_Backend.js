
app.listen(PORT, function(){
    console.log("listening on port 5501");
});

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