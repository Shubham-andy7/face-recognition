const connection=require("./model")
const express=require("express");
const application=express();
const path=require("path");
const expressHandleBars=require("express-handlebars");
const bodyparser=require("body-parser");
application.set('view engine', 'pug')
application.set('views', './views')

application.use(bodyparser.urlencoded({
    extended:true
}));

application.get("/",(req,res)=>{
    res.render("index");
})

application.get("/cctv", (req, res) => {
    res.render("cctv");
  });

application.listen("4000",()=>{
   // console.log("Server listening on port 4000");
});