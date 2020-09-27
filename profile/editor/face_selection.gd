extends Panel
class_name FaceSelection

signal selection_changed

var _image_size: Vector2
var _dragging_bounds: Rect2
var _handle_dragged = null

func load_from_image(image: Image) -> void:
	self._image_size = image.get_size()
	self.rect_position = Vector2.ZERO
	self.rect_size = Vector2(
		min(self._image_size.x, 200),
		min(self._image_size.y, 100)
	)
	self.show()

func _gui_input(event: InputEvent) -> void:
	if not _is_handle_dragged(self): return
	if _did_mouse_just_press(event, self):
		self._dragging_bounds = Rect2(Vector2.ZERO, self._image_size)
	else:
		var offset := _get_mouse_offset(event)
		if offset != Vector2.ZERO:
			var rect = get_rect()
			rect.position += offset
			_update_rect(rect)

func _on_TopLeft_gui_input(event: InputEvent) -> void:
	if not _is_handle_dragged($TopLeft): return
	if _did_mouse_just_press(event, $TopLeft):
		self._dragging_bounds = Rect2(Vector2.ZERO, self.rect_position + self.rect_size)
	else:
		var offset := _get_mouse_offset(event)
		if offset != Vector2.ZERO:
			var rect = get_rect()
			rect.position += offset
			rect.size -= offset
			_update_rect(rect)

func _on_TopRight_gui_input(event: InputEvent) -> void:
	if not _is_handle_dragged($TopRight): return
	if _did_mouse_just_press(event, $TopRight):
		var self_rect := get_rect()
		self._dragging_bounds.position = Vector2(self_rect.position.x, 0)
		self._dragging_bounds.end = Vector2(self._image_size.x, self_rect.end.y)
	else:
		var offset := _get_mouse_offset(event)
		if offset != Vector2.ZERO:
			var rect = get_rect()
			rect.position.y += offset.y
			rect.size.x += offset.x
			rect.size.y -= offset.y
			_update_rect(rect)

func _on_BottomLeft_gui_input(event: InputEvent) -> void:
	if not _is_handle_dragged($BottomLeft): return
	if _did_mouse_just_press(event, $BottomLeft):
		var self_rect := get_rect()
		self._dragging_bounds.position = Vector2(0, self_rect.position.y)
		self._dragging_bounds.end = Vector2(self_rect.end.x, self._image_size.y)
	else:
		var offset := _get_mouse_offset(event)
		if offset != Vector2.ZERO:
			var rect = get_rect()
			rect.position.x += offset.x
			rect.size.x -= offset.x
			rect.size.y += offset.y
			_update_rect(rect)

func _on_BottomRight_gui_input(event: InputEvent) -> void:
	if not _is_handle_dragged($TopLeft): return
	if _did_mouse_just_press(event, $TopLeft):
		self._dragging_bounds = Rect2(self.rect_position, self._image_size - self.rect_position)
	else:
		var offset := _get_mouse_offset(event)
		if offset != Vector2.ZERO:
			var rect = get_rect()
			rect.size += offset
			_update_rect(rect)

func _is_handle_dragged(handle: Node) -> bool:
	return self._handle_dragged == null or self._handle_dragged == handle

func _did_mouse_just_press(event: InputEvent, handle: Node) -> bool:
	if event is InputEventMouseButton:
		event = event as InputEventMouseButton
		if event.button_index == BUTTON_LEFT:
			get_tree().set_input_as_handled()
			self._handle_dragged = handle if event.pressed else null
			return event.pressed

	return false

func _get_mouse_offset(event: InputEvent) -> Vector2:
	if event is InputEventMouseMotion and self._handle_dragged != null:
			event = event as InputEventMouseMotion
			return event.relative

	return Vector2.ZERO

func _update_rect(rect: Rect2) -> void:
	if rect.size.x >= self.rect_min_size.x && rect.size.y >= self.rect_min_size.y && \
			self._dragging_bounds.encloses(rect):
		self.rect_position = rect.position
		self.rect_size = rect.size
		emit_signal("selection_changed")
