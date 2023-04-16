const express = require("express");
const fs = require("fs");

const cors = require("cors");
const formidable = require("formidable");

const app = express();
const server = require("http").createServer(app);

app.use(cors());

// POST request to /api/assignments
app.post("/api/assignments", (req, res) => {
    const form = new formidable.IncomingForm();
    let fields = {};
    let files = {};
    form.parse(req, (err, fields, files) => {
        if (err) {
            console.error("Error", err);
            throw err;
        }
        fields = fields;
        files = files;
        console.log("Fields", fields);

        // save fields as JSON file in the server
        fs.writeFile(
            "fields.json",
            JSON.stringify(fields),
            "utf8",
            (err) => {
                if (err) {
                    console.error("Error", err);
                    throw err;
                }
            }
        );


        console.log("Files", files.file.filepath);



        let response = {};

        if (
            Object.keys(fields).length === 0 ||
            Object.keys(files).length === 0
        ) {
            console.log(Object.keys(fields).length);
            console.log(Object.keys(files).length);
            response = {
                message: "Invalid request. Please check the fields and files",
                status: 400,
            };
            return res.status(400).json(response);
        } else {
            response = {
                message: "Assignment submitted for analysis successfully",
                status: 200,
            };
            // send delayed response of 5 seconds
            setTimeout(() => res.status(200).json(response), 2000);

            // res.status(200).json(response);
        }


    });

    // if either fields or files are empty, send error response
    
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server started on port ${PORT}`));
