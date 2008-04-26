$(document).ready(function() {
	$("#new_game_toggle").click(function() {
		var new_game = $("#new_game");
		new_game.toggle();
		if (new_game.css('display') != 'none') {
			$("#new_game_score1").focus();
		}
	});
});