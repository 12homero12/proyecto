//$(document).ready(function() {
//	alert("hola")
//});
var socket=io.connect("http://localhost:3000/");
socket.on('inicio_server', function(mensaje){
	$("#pagina").html(mensaje);
});
socket.on('mensaje_servidor', function(mensaje){
	$("#pagina").append('<ul>');
	$("#pagina").append('-->'+mensaje);
	$("#pagina").append('</ul>');
});

/*$(function(){
	$("#enviar").click(function(event) {
		mensaje=$("#mensaje").val();
		socket.emit("mensaje_cliente", mensaje)
	});
});*/


$(function(){
	$("#mensaje").keydown(function(event) {
		/* Act on the event */
		if (event.keyCode==13 && $(this).val()!="") 
		{
			mensaje=$("#mensaje").val();
			socket.emit("mensaje_cliente", mensaje)
		};
	});
});

$(function($) {
	/*alert("load")
	$("#sala").click(function(event) {
		event.preventDefault();
		alert("click")

	});*/
	var socket=io.connect("http://localhost:3000/");
	$("#sala").submit(function(event) {
		//enviar
		socket.emit("crearpartida",$(this).serializeObject());
		//socket.emit("idsala",id)
		//return false;
	});
	//escuchar el servidor
	socket.on("crearpartida",function(server){
		/*alert("partida nueva"+server)*/
		html="<div id='partidas'>";
		for(var i=0;i<server.length;i++)
		{
			/*html="<div id='partidas'>";*/
			html+="<h2>"+server[i].nombre+"</h2>";
			html+="<h5> cantidad:  "+server[i].cantidad+"</h5>";
			html+="<h5> temas :"+server[i].tema+"</h5>"
		}
		html+="</div>"
		$("#contaner").html(html);
	});
	/*socket.on ("idsala", function(server){
		html=
	});*/
});
