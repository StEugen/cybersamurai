const express = require("express")
const app = express()
const knex = require('knex');

const db = kenx({
    client: "pg",
    connection: process.env.POSTGRESQL_URL
})


app.use("/static", express.static("public"))
app.use(express.urlencoded({ extended: true }))
app.set("view engine", "ejs")


app.get('/',(req,res) => {
    res.render('todo.ejs');
})

app.post('/',(req, res) =>{
    console.log(req.body);
})

app.listen(
    3000, () => 
    console.log("Server is running", "url: http://localhost:3000")
)