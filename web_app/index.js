const connection=require("./model")
const express=require("express");
const application=express();
const path=require("path");
const expressHandleBars=require("express-handlebars");
const bodyparser=require("body-parser");
const router=require("./routes/userRouts");
application.set('view engine', 'pug')
application.set('views', './views')

application.use(bodyparser.urlencoded({
    extended:true
}));
application.use(router);
application.listen(port=4000,()=>{
   console.log("Server listening on port "+port);
});