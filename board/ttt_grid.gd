extends Spatial

func _ready() -> void:
	for child in get_children():
		randomize()
		(child as MeshInstance).rotation_degrees.z = rand_range(-15, 15)
