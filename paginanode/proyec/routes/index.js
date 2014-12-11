var express = require('express');
var router = express.Router();
var mysql=require("../db/mysql");
var query=new mysql({host:"localhost",user:"root",password:"",database:"db_trivial"});
/* GET home page. */
router.get('/', function(req, res) {
  res.render('index', { title: 'Express' });
});

/*router.get("/crearsala/:id?",function(req,res){
	//req.params.id
	console.log(req.params.id);
	query.get("django_session").where({session_key:req.params.id}).execute(function(rows){
		if(rows.length>0){
			console.log(rows);
			res.render("crearsala",{});
		}
	});

});*/

router.get("/crearsala",function(req,res){
	res.render("crearsala",{});
});

module.exports = router;
