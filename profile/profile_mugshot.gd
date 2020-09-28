extends Panel

onready var personification: ProfilePersonification = $ViewportContainer/Viewport/ProfilePersonification

func call_on_personification(arg, method: String) -> void:
	$ViewportContainer/Viewport/ProfilePersonification.call(method, arg)

func call_on_personification_without_arg(method: String) -> void:
	$ViewportContainer/Viewport/ProfilePersonification.call(method)
