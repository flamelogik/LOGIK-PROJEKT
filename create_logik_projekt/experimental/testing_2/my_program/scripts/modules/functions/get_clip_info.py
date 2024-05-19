# Function:     get_clip_info

def get_clip_info(self, clip):
    import flame

    # Get clip values

    self.clip_name = str(clip.name)[1:-1]
    #print('clip_name: ', self.clip_name)

    self.clip_duration = clip.duration
    #print('clip_duration:', self.clip_duration)

    self.clip_frame_rate = clip.clip.frame_rate
    #print('clip_frame_rate:', self.clip_frame_rate)

    self.clip_timecode = clip.clip.start_time
    #print('clip_timecode:', self.clip_timecode)

    self.clip_shot_name = pyside6_qt_get_shot_name(clip)
