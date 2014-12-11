var express=require('express');
var http=require('http');
var port=3000;
var path=require('path');
var app=express();

var routes = require('./routes/index');
var users = require('./routes/users');

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

/*app.engine('jade',require('jade').__express);
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());*/
app.use(express.static(__dirname + '/public'));

app.use('/', routes);
app.use('/users', users);


/*app.get("/",function(req,res){
	res.render("index");
});

app.get("/crearsala",function(req,res){
	res.render("crearsala",{});
});*/
var server=http.createServer(app).listen(port,function(){
	console.log("servidor corriendo en el puerto" + port);
});
require('./routes/sockets.js').initialize(server)