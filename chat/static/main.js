$(document).ready(function () {
	let socketIO = io.connect(`http://${document.domain}:${location.port}`)

	$('.message-field').focus();
	$('.message-display').scrollTop($('.message-display').prop('scrollHeight'));	
	$('.send-btn').attr('disabled', 'disabled');		

	$('.message-field').on('input', function () {
		if (!$(this).val()) {
			$('.send-btn').attr('disabled', 'disabled');
		}else{
			$('.send-btn').removeAttr('disabled');
		}
	});

	$('.message-field').on('keypress', function (event) {
		if (event.keyCode == 13) {
			event.preventDefault();
			if ($(this).val().trim()) {
				socketIO.emit('message_request', {
					text: $(this).val().trim()
				});
				$(this).val('').focus();
				$('.send-btn').attr('disabled', 'disabled');
			}
		}
	});

	$('.send-btn').on('click', function () {
		if ($('.message-field').val().trim()) {
				socketIO.emit('message_request', {
					text: $('.message-field').val().trim()
				});
				$('.message-field').val('').focus();
				$(this).attr('disabled', 'disabled');
			}
	});

	socketIO.on('message_response', function (data) {
		$('.message-display').append(`<div class="message"><small>${data['created']}</small> <span>${data['user']}:</span> ${data['text']}</div></div><hr>`);
		$('.message-display').scrollTop($('.message-display').prop('scrollHeight'));
	});
});