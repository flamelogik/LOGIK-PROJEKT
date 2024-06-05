---- [Tab created 06/04/2024 04:29:50 PM] ----

[06/04/2024 04:29:59 PM]
>>> import flame
>>> 
>>> def get_write_file_details(node_name):
>>>     # Get the Write File node
>>>     write_file_node = flame.batch.get_node(node_name)
>>>     if not write_file_node:
>>>         print(f"Write File node '{node_name}' not found.")
>>>         return
>>> 
>>>     # Print attributes and their methods/functions
>>>     print(f"Details for Write File node '{node_name}':")
>>>     
>>>     # Attributes
>>>     print("\nAttributes:")
>>>     for attr_name in dir(write_file_node):
>>>         print(f"  {attr_name}")
>>> 
>>>     # Methods/functions for specific attributes
>>>     print("\nMethods and functions:")
>>>     attributes = write_file_node.attributes
>>>     for attr_name in dir(attributes):
>>>         attr_value = getattr(attributes, attr_name)
>>>         if callable(attr_value):
>>>             print(f"  {attr_name} (method)")
>>> 
>>>     channels = write_file_node.channels
>>>     for attr_name in dir(channels):
>>>         attr_value = getattr(channels, attr_name)
>>>         if callable(attr_value):
>>>             print(f"  {attr_name} (method)")
>>> 
>>>     input_sockets = write_file_node.input_sockets
>>>     for attr_name in dir(input_sockets):
>>>         attr_value = getattr(input_sockets, attr_name)
>>>         if callable(attr_value):
>>>             print(f"  {attr_name} (method)")
>>> 
>>>     output_sockets = write_file_node.output_sockets
>>>     for attr_name in dir(output_sockets):
>>>         attr_value = getattr(output_sockets, attr_name)
>>>         if callable(attr_value):
>>>             print(f"  {attr_name} (method)")
>>> 
>>>     parent_group = write_file_node.parent
>>>     for attr_name in dir(parent_group):
>>>         attr_value = getattr(parent_group, attr_name)
>>>         if callable(attr_value):
>>>             print(f"  {attr_name} (method)")
>>> 
>>>     all_sockets = write_file_node.sockets
>>>     for attr_name in dir(all_sockets):
>>>         attr_value = getattr(all_sockets, attr_name)
>>>         if callable(attr_value):
>>>             print(f"  {attr_name} (method)")
>>> 
>>> # Replace with your actual Write File node name
>>> write_file_node_name = "ANIMALS_0010_comp"
>>> get_write_file_details(write_file_node_name)
Details for Write File node 'ANIMALS_0010_comp':

Attributes:
  __class__
  __delattr__
  __dict__
  __dir__
  __doc__
  __eq__
  __format__
  __ge__
  __getattr__
  __getattribute__
  __getstate__
  __gt__
  __hash__
  __init__
  __init_subclass__
  __le__
  __lt__
  __module__
  __ne__
  __new__
  __reduce__
  __reduce_ex__
  __repr__
  __setattr__
  __sizeof__
  __str__
  __subclasshook__
  __weakref__
  attributes
  channels
  delete
  duplicate
  get_resolved_media_path
  input_sockets
  load_node_setup
  output_sockets
  parent
  save_node_setup
  set_channel_name
  set_context
  sockets

Methods and functions:
  __add__ (method)
  __class__ (method)
  __class_getitem__ (method)
  __contains__ (method)
  __delattr__ (method)
  __delitem__ (method)
  __dir__ (method)
  __eq__ (method)
  __format__ (method)
  __ge__ (method)
  __getattribute__ (method)
  __getitem__ (method)
  __getstate__ (method)
  __gt__ (method)
  __iadd__ (method)
  __imul__ (method)
  __init__ (method)
  __init_subclass__ (method)
  __iter__ (method)
  __le__ (method)
  __len__ (method)
  __lt__ (method)
  __mul__ (method)
  __ne__ (method)
  __new__ (method)
  __reduce__ (method)
  __reduce_ex__ (method)
  __repr__ (method)
  __reversed__ (method)
  __rmul__ (method)
  __setattr__ (method)
  __setitem__ (method)
  __sizeof__ (method)
  __str__ (method)
  __subclasshook__ (method)
  append (method)
  clear (method)
  copy (method)
  count (method)
  extend (method)
  index (method)
  insert (method)
  pop (method)
  remove (method)
  reverse (method)
  sort (method)
  __add__ (method)
  __class__ (method)
  __class_getitem__ (method)
  __contains__ (method)
  __delattr__ (method)
  __delitem__ (method)
  __dir__ (method)
  __eq__ (method)
  __format__ (method)
  __ge__ (method)
  __getattribute__ (method)
  __getitem__ (method)
  __getstate__ (method)
  __gt__ (method)
  __iadd__ (method)
  __imul__ (method)
  __init__ (method)
  __init_subclass__ (method)
  __iter__ (method)
  __le__ (method)
  __len__ (method)
  __lt__ (method)
  __mul__ (method)
  __ne__ (method)
  __new__ (method)
  __reduce__ (method)
  __reduce_ex__ (method)
  __repr__ (method)
  __reversed__ (method)
  __rmul__ (method)
  __setattr__ (method)
  __setitem__ (method)
  __sizeof__ (method)
  __str__ (method)
  __subclasshook__ (method)
  append (method)
  clear (method)
  copy (method)
  count (method)
  extend (method)
  index (method)
  insert (method)
  pop (method)
  remove (method)
  reverse (method)
  sort (method)
  __add__ (method)
  __class__ (method)
  __class_getitem__ (method)
  __contains__ (method)
  __delattr__ (method)
  __delitem__ (method)
  __dir__ (method)
  __eq__ (method)
  __format__ (method)
  __ge__ (method)
  __getattribute__ (method)
  __getitem__ (method)
  __getstate__ (method)
  __gt__ (method)
  __iadd__ (method)
  __imul__ (method)
  __init__ (method)
  __init_subclass__ (method)
  __iter__ (method)
  __le__ (method)
  __len__ (method)
  __lt__ (method)
  __mul__ (method)
  __ne__ (method)
  __new__ (method)
  __reduce__ (method)
  __reduce_ex__ (method)
  __repr__ (method)
  __reversed__ (method)
  __rmul__ (method)
  __setattr__ (method)
  __setitem__ (method)
  __sizeof__ (method)
  __str__ (method)
  __subclasshook__ (method)
  append (method)
  clear (method)
  copy (method)
  count (method)
  extend (method)
  index (method)
  insert (method)
  pop (method)
  remove (method)
  reverse (method)
  sort (method)
  __add__ (method)
  __class__ (method)
  __class_getitem__ (method)
  __contains__ (method)
  __delattr__ (method)
  __delitem__ (method)
  __dir__ (method)
  __eq__ (method)
  __format__ (method)
  __ge__ (method)
  __getattribute__ (method)
  __getitem__ (method)
  __getstate__ (method)
  __gt__ (method)
  __iadd__ (method)
  __imul__ (method)
  __init__ (method)
  __init_subclass__ (method)
  __iter__ (method)
  __le__ (method)
  __len__ (method)
  __lt__ (method)
  __mul__ (method)
  __ne__ (method)
  __new__ (method)
  __reduce__ (method)
  __reduce_ex__ (method)
  __repr__ (method)
  __reversed__ (method)
  __rmul__ (method)
  __setattr__ (method)
  __setitem__ (method)
  __sizeof__ (method)
  __str__ (method)
  __subclasshook__ (method)
  append (method)
  clear (method)
  copy (method)
  count (method)
  extend (method)
  index (method)
  insert (method)
  pop (method)
  remove (method)
  reverse (method)
  sort (method)
  __class__ (method)
  __delattr__ (method)
  __dir__ (method)
  __eq__ (method)
  __format__ (method)
  __ge__ (method)
  __getattr__ (method)
  __getattribute__ (method)
  __getstate__ (method)
  __gt__ (method)
  __hash__ (method)
  __init__ (method)
  __init_subclass__ (method)
  __le__ (method)
  __lt__ (method)
  __ne__ (method)
  __new__ (method)
  __reduce__ (method)
  __reduce_ex__ (method)
  __repr__ (method)
  __setattr__ (method)
  __sizeof__ (method)
  __str__ (method)
  __subclasshook__ (method)
  append_setup (method)
  append_to_batch (method)
  append_to_setup (method)
  clear (method)
  clear_all_contexts (method)
  clear_context (method)
  clear_setup (method)
  close (method)
  connect_nodes (method)
  create_batch_group (method)
  create_node (method)
  create_reel (method)
  create_shelf_reel (method)
  disconnect_node (method)
  encompass_nodes (method)
  frame_all (method)
  frame_selected (method)
  get_node (method)
  go_to (method)
  import_clip (method)
  import_clips (method)
  iterate (method)
  load_setup (method)
  mimic_link (method)
  open (method)
  open_as_batch_group (method)
  organize (method)
  render (method)
  replace_setup (method)
  save (method)
  save_current_iteration (method)
  save_setup (method)
  select_nodes (method)
  set_viewport_layout (method)
  __class__ (method)
  __class_getitem__ (method)
  __contains__ (method)
  __delattr__ (method)
  __delitem__ (method)
  __dir__ (method)
  __eq__ (method)
  __format__ (method)
  __ge__ (method)
  __getattribute__ (method)
  __getitem__ (method)
  __getstate__ (method)
  __gt__ (method)
  __init__ (method)
  __init_subclass__ (method)
  __ior__ (method)
  __iter__ (method)
  __le__ (method)
  __len__ (method)
  __lt__ (method)
  __ne__ (method)
  __new__ (method)
  __or__ (method)
  __reduce__ (method)
  __reduce_ex__ (method)
  __repr__ (method)
  __reversed__ (method)
  __ror__ (method)
  __setattr__ (method)
  __setitem__ (method)
  __sizeof__ (method)
  __str__ (method)
  __subclasshook__ (method)
  clear (method)
  copy (method)
  fromkeys (method)
  get (method)
  items (method)
  keys (method)
  pop (method)
  popitem (method)
  setdefault (method)
  update (method)
  values (method)
# -------------------------------------------------------------------------- #
# version:               0.4.5
# modified:              2024-06-04 - 17:38:53
# comments:              Added 'Smart Replace' option for render and write nodes
