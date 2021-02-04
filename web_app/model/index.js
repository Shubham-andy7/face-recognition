const mongoose=require("mongoose");

mongoose.connect("mongodb://localhost:27017/face_recog",{ useNewUrlParser: true,useUnifiedTopology: true},(error)=>{
    if(!error)
    {
        console.log("Success");
    }
    else
    {
        console.log("Error connecting to database")
    }
});
const user=require("./user.model");