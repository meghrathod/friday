const express = require("express");
const fs = require("fs");
const childProcess = require("child_process");

const cors = require("cors");
const formidable = require("formidable");

const app = express();
const server = require("http").createServer(app);

app.use(cors());

// POST request to /api/assignments
app.post("/api/assignments", (req, res) => {
	const form = new formidable.IncomingForm();

	form.parse(req, (err, fields, files) => {
		if (err) {
			console.error("Error", err);
			throw err;
		}

		console.log("Fields", fields);

		const config = JSON.stringify({
			test_cases: new Array(Number.parseInt(fields.testcases))
				.fill(undefined)
				.map((_, i) => ({
					test_case: fields[`input${i + 1}`],
					output: fields[`output${i + 1}`],
					marks:
						fields[`testWeight${i + 1}`] === "undefined"
							? 1
							: Number.parseInt(fields[`testWeight${i + 1}`]),
				})),
		});
		fs.writeFileSync("/tmp/config.json", config);
		const zipFilePath = files.file.filepath;
		fs.renameSync(zipFilePath, zipFilePath + ".zip");

		console.log([
			"../friday/src/main.py",
			"-i",
			zipFilePath + ".zip",
			"-ti",
			"/tmp/config.json",
			"-lng",
			fields.language,
		]);

		const proc = childProcess.spawn(
			"python3.10",
			[
				"../friday/src/main.py",
				"-i",
				zipFilePath + ".zip",
				"-ti",
				"/tmp/config.json",
				"-lng",
				fields.language,
			],
			{
				stdio: "inherit",
			}
		);

		proc.on("exit", () => {
			res.send(fs.readFileSync("../testResults.json").toString("utf-8"));
		});

		// python3 src/main.py -i files.file.filepath -ti /tmp/config.json -lng C -o /tmp/output.jsom

		// let response = {};

		// if (Object.keys(fields).length === 0 || Object.keys(files).length === 0) {
		// 	console.log(Object.keys(fields).length);
		// 	console.log(Object.keys(files).length);
		// 	response = {
		// 		message: "Invalid request. Please check the fields and files",
		// 		status: 400,
		// 	};
		// 	return res.status(400).json(response);
		// } else {
		// 	response = {
		// 		message: "Assignment submitted for analysis successfully",
		// 		status: 200,
		// 	};
		// 	// send delayed response of 5 seconds
		// 	setTimeout(() => res.status(200).json(response), 2000);

		// 	// res.status(200).json(response);
		// }
	});

	// if either fields or files are empty, send error response
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server started on port ${PORT}`));
