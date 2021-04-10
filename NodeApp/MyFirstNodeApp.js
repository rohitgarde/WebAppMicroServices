const express = require('express');
const app = express();
const port = 3002;

app.use(express.json());
app.get('/status', (req, res) => res.json({status: "ok"}));
app.listen(port, () => console.log(`Node App listening on port ${port}!`));
