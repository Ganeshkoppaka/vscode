const mysql = require("mysql");

const db = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "yourpassword",
  database: "game",
});

db.connect((err) => {
  if (err) throw err;
  console.log("Connected to MySQL database.");
});

app.post("/submit-score", (req, res) => {
  const { username, score } = req.body;
  const query = "INSERT INTO scores (username, score) VALUES (?, ?)";
  db.query(query, [username, score], (err, result) => {
    if (err) throw err;
    res.status(200).send("Score saved!");
  });
});

app.get("/leaderboard", (req, res) => {
  const query = "SELECT username, score FROM scores ORDER BY score DESC LIMIT 10";
  db.query(query, (err, results) => {
    if (err) throw err;
    res.json(results);
  });
});

