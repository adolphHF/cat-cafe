$(document).ready(function(){
	$('.secciones article').hide();
	$('.secciones article:first').show();

	$('ul.tabs li a').click(function(){
		$('.secciones article').hide();

		var activeTab = $(this).attr('href');
		$(activeTab).show();
		return false;
	});

     // Manejar clics en el enlace para volver al inicio
     $('a.navbar-brand').click(function(){
        $('.secciones article').hide();
        $('.secciones article:first').show();
        return false;
    });

});