const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
const bodyParser = require("body-parser");

const app = express();
const port = 5000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// MongoDB Connection
mongoose.connect("mongodb+srv://janhvidhale4:pekPWLiPTfN98KCB@data.col76.mongodb.net/?retryWrites=true&w=majority&appName=Data") // ✅ No extra options needed
  .then(() => console.log("Connected to MongoDB"))
  .catch(err => console.error("MongoDB connection error:", err));


// Report Schema & Model
const reportSchema = new mongoose.Schema({
  name: String,
  email: String,
  category: String,
  subCategory: String,
  date: String,
  time: String,
  location: String,
  reason: String,
  report: String,
});

const Report = mongoose.model("Report", reportSchema);

// Route to Save Report
app.post("/reports", async (req, res) => {
  try {
    const newReport = new Report(req.body);
    await newReport.save();
    res.json({ message: "Report submitted successfully!" });
  } catch (error) {
    res.status(500).json({ error: "Failed to submit report" });
  }
});

// Route to Fetch Reports
app.get("/reports", async (req, res) => {
  try {
    const reports = await Report.find();
    res.json(reports);
  } catch (error) {
    res.status(500).json({ error: "Failed to fetch reports" });
  }
});

// Start Server
app.listen(port, () => console.log(`Server running on port ${port}`));
