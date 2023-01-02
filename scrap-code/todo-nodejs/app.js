const express = require("express")
const db = require('./config/db')
const app = express()



app.use("/static", express.static("public"))
app.use(express.urlencoded({ extended: true }))
app.set("view engine", "pug")


app.get('/', async (req,res) => {
    const query = 'SELECT * FROM notes ORDER BY id;';
    const { rows } = await db.query(query);
    res.render('index', { item: rows });
})

app.post('/addToDo', async (req, res) => {
    console.log(req.body);
    const query = 'INSERT INTO notes(note) VALUES($1);';
    const value = [req.body.note]
    const {rows} = await db.query(query, value)
    console.log(rows)
    res.redirect('/')
})


app.post('/delete', async (req,res) => {
    const query = 'DELETE FROM notes WHERE note = $1;';
    const value
})


app.listen(
    3000, () => 
    console.log("Server is running", "url: http://localhost:3000")
)