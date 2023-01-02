const express = require("express")
const { Connection } = require("pg")
const app = express()



app.use("/static", express.static("public"))
app.use(express.urlencoded({ extended: true }))
app.set("view engine", "ejs")


app.get('/',(req,res) => {
    pg.select("*").from("note").then(data => {
        res.render("todo.ejs", { todos: data });
    }).catch(err => res.status(400).json(err))
})

app.post('/addTask',(req, res) =>{
    const { textTodo } = req.body;
    pg("note").insert({ note: textTodo }).returning("*").then(_=>{
        res.redirect("/")
    }).catch(err =>{
        res.status(400).json({message: "unable to make a task"})
    })
    console.log(req.body);
})


app.listen(
    3000, () => 
    console.log("Server is running", "url: http://localhost:3000")
)