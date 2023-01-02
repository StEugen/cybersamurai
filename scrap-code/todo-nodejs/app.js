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
    const query = 'INSERT INTO notes(note) VALUES($1);';
    const value = [req.body.note]
    const {rows} = await db.query(query, value)
    res.redirect('/')
})


app.get('/delete/:id', async (req,res) => {
    const query = 'DELETE FROM notes WHERE id=$1;';
    const value = [req.params.id];
    const { result } = await db.query(query, value)
    res.redirect("/")
})


app.listen(
    3000, () => 
    console.log("Server is running", "url: http://localhost:3000")
)