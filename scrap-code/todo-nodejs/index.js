const express = require("express")
const app = express()

app.set("view engine", "ejs")

app.get('/',(req,res) => {
    res.render('todo.ejs');
})



app.listen(3000, () => console.log("Server is running", "url: http://localhost:3000"))