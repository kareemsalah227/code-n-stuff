import express from "express";
import bodyParser from "body-parser";
import { Pool } from "pg";

const app = express();
const port = 3001;

const pg_pool = new Pool({
  host: "localhost",
  user: "the_user",
  password: "the_user_wordpass",
  database: "forms_db",
  port: 5432,
  idleTimeoutMillis: 30000,
});

app.use(bodyParser.json({ type: 'application/json' }));

app.get("/forms", async (req, res) => {
  // Read from Database
  try {
    const forms = await pg_pool.query("SELECT * FROM forms;");

    res.json(forms.rows);
  } catch (error) {
    console.error("[Error] GET /forms: something went wrong!", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
});

app.post("/forms", async (req, res) => {
  // Extract data form from request body
  const data = req.body;

  // Save to database
  try {
    await pg_pool.query("INSERT INTO forms(name, preference) VALUES ($1, $2);", [
      data.name,
      data.preference,
    ]);
    res.status(201).send();
  } catch (error) {
    console.error("[Error] POST /forms: something went wrong!", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
});

// This endpoint is used for serving the web client
// app.get("/", (req, res) => {
//   // Log something

//   // Send the corresponding file for the client from a dist directory
// });

app.listen(port, () => {
  console.log("Let them requests come in...");
});
