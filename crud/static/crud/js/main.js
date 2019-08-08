// Отправка заявки 
$(document).ready(function() {
	$('#form').submit(function() { // проверка на пустоту заполненных полей. Атрибут html5 — required не подходит (не поддерживается Safari)
		if (document.form.title.value == '' || document.form.body.value == '' ) {
			valid = false;
			return valid;
		}
		$.ajax({
			type: "POST",
			url: "/create/",
			data: $(this).serialize()
		}).done(function() {
			$(this).find('input').val('');
			$('#form').trigger('reset');
		});
		return false;
	});
});