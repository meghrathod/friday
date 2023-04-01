const express = require("express");
const {Server} = require("socket.io");

const cors = require("cors");
const formidable = require("formidable");


const app = express();
const server = require("http").createServer(app);

app.use(cors());
const io = new Server(server, {
    cors: {
        origin: "*",
        methods: ["GET", "POST"]
    }
});





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
        console.log("Files", files);
    });

    // if either fields or files are empty, send error response
    let response = {};
    if (Object.keys(fields).length === 0 || Object.keys(files).length === 0) {
        response = {
            message: "Invalid request. Please check the fields and files",
            status : 400
        }
        return res.status(400).json(response);
    } else {

    }


    response = {
        message: "Assignment submitted for analysis successfully",
        status : 200
    }
    // send delayed response of 5 seconds
    setTimeout(() => res.status(200).json(response), 5000);
        
    // res.status(200).json(response);
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server started on port ${PORT}`));
