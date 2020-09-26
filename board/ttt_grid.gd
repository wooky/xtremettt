extends Spatial

func _ready() -> void:
	for child in get_children():
		(child as MeshInstance).rotation_degrees.z = rand_range(-30, 30)
