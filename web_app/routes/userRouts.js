const express=require("express");
const router=express.Router();

router.get("/",(req,res)=>{
    res.render("index");
})

router.get("/cctv", (req, res) => {
    res.render("cctv");
  });

  router.use((req,res)=>{
      res.status=404;
        res.render("notfound");
  });
  module.exports = router;