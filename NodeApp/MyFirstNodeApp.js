const express = require('express');
const app = express();
const port = 3002;

app.use(express.json());
app.get('/get', (req, res) => res.json({status: "GET Request received on NodeJS App."}));
app.post('/post', (req, res) => res.json({status: "POST Request received on NodeJS App."}));

app.listen(port, () => console.log(`Node App listening on port ${port}!`));
