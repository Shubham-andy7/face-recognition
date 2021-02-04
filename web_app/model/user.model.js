const mongoose=require("mongoose");
var userSchema=new mongoose.Schema({
    name:{
        type:String,
        require:"Name required"
    },
    password:{
        type:String,
        require:"Password required"
    }
});
mongoose.model("User",userSchema);