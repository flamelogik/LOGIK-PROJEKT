
# Create Project Layout by creating or validate folders, reels, & reel groups
def create_layout(*args):

    # If Flame passes any arguments, you can handle them here
    if args:
        print("Received arguments from Flame:", args)

    # ---------------------------------------------------------------------- #

    the_current_projekt = flame.projects.current_project
    the_current_workspace = the_current_projekt.current_workspace
    the_current_desktop = the_current_workspace.desktop

    # ---------------------------------------------------------------------- #

    # Validate or create 'Default Library' library
    default_library = \
        create_or_validate_library(
            the_current_workspace,
            'Default Library'
            )

    # Change the color of 'Default Library' to Dark Red
    change_default_library_color(the_current_workspace)

    # Change the name of 'Default Library' to 'desktops'
    change_default_library_name(the_current_workspace, 'desktops')

    # ---------------------------------------------------------------------- #

    # Validate or create 'desktops' library

    # ---------------------------------------------------------------------- #

    # Validate or create 'reference' library

    # ---------------------------------------------------------------------- #

    # Validate or create 'editorial' library
    editorial_library = \
        create_or_validate_library(
            the_current_workspace,
            'editorial',
            object_colors.get("Dark Gold")
            )

    # Validate or create folder 'conforms' in 'editorial'
    conforms_folder = \
        create_or_validate_object(
            editorial_library,
            'conforms',
            'folder'
            )

    # Validate or create dated conforms template reel group in 'conforms'
    dated_conforms_template_reel_group = \
        create_or_validate_object(
            conforms_folder,
            'YYYY-MM-DD-conform',
            'reel group'
            )

    # Rename reels in 'dated conforms template reel group'
    for reel in dated_conforms_template_reel_group.reels:
        if reel.name == 'Reel 1':
            reel.name = 'ref'
            reel.colour = object_colors.get("Dark Blue")
        if reel.name == 'Reel 2':
            reel.name = 'Sources'
            reel.colour = object_colors.get("Dark Green")
        if reel.name == 'Sequences':
            reel.colour = object_colors.get("Dark Red")

    # # Validate or create dated conforms reel group in 'conforms'
    # dated_conforms_reel_group = \
    #     create_or_validate_object(
    #         conforms_folder,
    #         today_date + '-conform',
    #         'reel group'
    #         )

    # # Rename reels in 'dated conforms reel group'
    # for reel in dated_conforms_reel_group.reels:
    #     if reel.name == 'Reel 1':
    #         reel.name = 'ref'
    #         reel.colour = object_colors.get("Dark Blue")
    #     if reel.name == 'Reel 2':
    #         reel.name = 'Sources'
    #         reel.colour = object_colors.get("Dark Green")
    #     if reel.name == 'Sequences':
    #         reel.colour = object_colors.get("Dark Red")

    # Validate or create folder 'work_in_progress' in 'editorial'
    work_in_progress_folder = \
        create_or_validate_object(
            editorial_library,
            'work_in_progress',
            'folder'
            )

    # Validate or create folder 'postings' in 'work_in_progress'
    postings_folder = \
        create_or_validate_object(
            work_in_progress_folder,
            'postings',
            'folder',
            object_colors.get("Blue")
            )

    # Validate or create dated postings reel in 'postings'
    todays_postings_reel = \
        create_or_validate_object(
            postings_folder,
            today_date + '-postings',
            'reel'
            )

    # ---------------------------------------------------------------------- #

    # Validate or create 'assets' library

    # ---------------------------------------------------------------------- #

    # Validate or create 'masters' library

    # # Validate or create 'master_edits' reel group in 'final_masters'
    # master_edits_reel_group = \
    #     create_or_validate_object(
    #         final_masters_folder,
    #         'master_edits',
    #         'reel group'
    #         )

    # # Rename reels in 'master edits reel group'
    # for reel in master_edits_reel_group.reels:
    #     if reel.name == 'Reel 1':
    #         reel.name = 'final_masters'
    #     elif reel.name == 'Reel 2':
    #         reel.name = 'versions'
    #     elif reel.name == 'Sequences':
    #         reel.name = 'slated_masters'

    # ---------------------------------------------------------------------- #

    # Validate or create 'shots' library

    # ---------------------------------------------------------------------- #

    # Change the current desktop name
    new_desktop_name = today_date + '-work'
    the_current_desktop.name = new_desktop_name

    # Print the name of the current desktop
    print(f"Current desktop: {the_current_desktop.name}")

    # Change the name and color of the reel group in the current desktop
    for desktop_reel_group in the_current_desktop.reel_groups:
        if desktop_reel_group.name == 'Reels':
            desktop_reel_group.name = today_date + '-conform'
            desktop_reel_group.colour = object_colors.get("Dark Purple")
            for reel in desktop_reel_group.reels:
                    if reel.name == 'Reel 1':
                        reel.name = 'ref'
                        reel.colour = object_colors.get("Dark Blue")
                    if reel.name == 'Reel 2':
                        reel.name = 'Sources'
                        reel.colour = object_colors.get("Dark Green")
                    if reel.name == 'Sequences':
                        reel.colour = object_colors.get("Dark Red")

    # Validate or create dated postings reel in 'pattern_browsed_clips'
    published_sequences_reel = \
        create_or_validate_object(
            desktop_reel_group,
            'Published-Sequences',
            'reel',
            # object_reel_type='Sequences',
            object_colors.get("Red")
            )

    # Validate or create dated postings reel in 'pattern_browsed_clips'
    published_versions_reel = \
        create_or_validate_object(
            desktop_reel_group,
            'Published-Versions',
            'reel',
            object_colors.get("Green")
            )

    # Validate or create dated postings reel in 'pattern_browsed_clips'
    todays_postings_reel = \
        create_or_validate_object(
            desktop_reel_group,
            today_date + '-postings',
            'reel',
            object_colors.get("Blue")
            )

    # # Validate or create batch group in 'default_Desktop'
    # default_Desktop_batch_group = \
    #     create_or_validate_object(
    #         the_current_desktop,
    #         'My New Batch',
    #         'batch group',
    #         object_colors.get("Red"),
    #         batch_group=True
    #         )

    # ---------------------------------------------------------------------- #

    print("Project layout setup completed.")
# -------------------------------------------------------------------------- #
# version:               0.0.5
# modified:              2024-05-12 - 15:37:50
# comments:              Added function to read directories from JSON files.
# -------------------------------------------------------------------------- #
# version:               0.0.6
# modified:              2024-05-12 - 18:16:05
# comments:              Added a 'separators' function and tested in flame 2025.
