# Dictionary containing information about each room
rooms = {
    'room_left_bottom': """
       ROOM
    |--   --|
    |
    |-------|
""",
    'room_middle_bottom': """
       ROOM
    |--   --|

    |-------|
""",
    'room_right_bottom': """
       ROOM
    |--   --|
            |
    |-------|
""",
    'room_left_middle': """
       ROOM
    |--   --|
    |
    |--   --|
""",
    'room_middle_middle': """
       ROOM
    |--   --|

    |--   --|
""",
    'room_right_middle': """
       ROOM
    |--   --|
            |
    |--   --|
""",
    'room_left_top': """
       ROOM
    |-------|
    |   ☺
    |--   --|
""",
    'room_middle_top': """
       ROOM
    |--   --|
        ↑
    |--   --|
""",
    'room_right_top': """
       SHOP
    |-------|
       $$$  |
    |--   --|
""",
    'room_boss': """
       BOSS
    |-------|
    |(ง •̀_•́)ง|
    |-------|
    """,
    'cool_room': """
                SECRET
    |------------------------------|
    |                              |  
    | ✌ You are doing great boss ✌   /
    |                              /
    |------------------------------|
    """
}

# Dictionary containing paths between rooms
rooms_paths = {
    'room_left_bottom': {'up': 'room_left_middle', 'right': 'room_middle_bottom'},
    'room_middle_bottom': {'up': 'room_middle_middle', 'left': 'room_left_bottom', 'right': 'room_right_bottom'},
    'room_right_bottom': {'up': 'room_right_middle', 'left': 'room_middle_bottom'},
    'room_left_middle': {'up': 'room_left_top', 'down': 'room_left_bottom', 'right': 'room_middle_middle'},
    'room_middle_middle': {'up': 'room_middle_top', 'down': 'room_middle_bottom', 'left': 'room_left_middle', 'right': 'room_right_middle'},
    'room_right_middle': {'up': 'room_right_top', 'down': 'room_right_bottom', 'left': 'room_middle_middle'},
    'room_left_top': {'down': 'room_left_middle', 'left': 'cool_room', 'right': 'room_middle_top'},
    'room_middle_top': {'up': 'room_boss', 'down': 'room_middle_middle', 'left': 'room_left_top', 'right': 'room_right_top'},
    'room_right_top': {'down': 'room_right_middle', 'left': 'room_middle_top'},
    'room_boss': {},
    'cool_room': {'right': 'room_left_top'}
}

# List of rooms that have been entered by the player
rooms_entered = ['room_middle_bottom', 'room_boss', 'room_right_top', 'room_left_top', 'cool_room']

# Variable to store the current room the player is in
current_room = 'room_middle_bottom'
