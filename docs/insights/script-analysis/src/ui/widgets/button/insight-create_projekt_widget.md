# Insight: `create_projekt_widget.py`

## 1. Widget Type

`CreateProjektWidget` is a composite `QWidget` that primarily contains a `QPushButton`. It serves as the main action trigger for creating a new project.

## 2. Purpose

This widget provides the user with a clear and prominent button to initiate the project creation process within the LOGIK-PROJEKT application. It is the final step in the project setup UI.

## 3. Behavior and Functionality

- **Action Trigger:** When clicked, the button emits a `clicked` signal, which is connected to a command (a Python callable) provided during its initialization.
- **Visual Feedback:** The button has a fixed height for consistent UI and a descriptive text "Create LOGIK-PROJEKT". It also has an object name `"createProjektButton"` which can be used for styling or testing.
- **Optional Label:** While a `QLabel` is part of the layout, it is currently empty and fixed-width, suggesting it might be a placeholder or intended for future use (e.g., displaying status messages).

## 4. Key Attributes and Properties

- `self.layout`: A `QHBoxLayout` that arranges the (empty) label and the button horizontally.
- `self.label`: An empty `QLabel` with a fixed width.
- `self.button`: The `QPushButton` instance with the text "Create LOGIK-PROJEKT".

## 5. Signals and Slots

- **Signals:** The `self.button` (a `QPushButton`) emits the standard `clicked()` signal when pressed.
- **Slots (Public Methods):**
  - The `__init__` method takes an optional `command` argument. If provided, this `command` (which should be a callable, typically a method from a controller class) is connected to the button's `clicked` signal. This is the primary mechanism for triggering the project creation logic.

## 6. Dependencies and Relationships

- **`src.ui.ui_config`**: Imports `ui_config` to set the `BUTTON_HEIGHT`, ensuring visual consistency across the application's buttons.
- **`AppLogic` (or a dedicated controller)**: This widget is a crucial part of the application's workflow. The `command` passed to its constructor will almost certainly be a method from the main application logic (`AppLogic`) or a dedicated project creation controller. This method will be responsible for:
  - Gathering all the data from other widgets (client name, campaign name, resolution, frame rate, etc.).
  - Validating the collected data.
  - Initiating the backend processes to create the project (e.g., calling `projekt_creator.py`).

## 7. UI/UX Notes

This button serves as the explicit trigger for a significant action. Its clear labeling and prominent placement guide the user to the final step of the project setup. The direct connection to a `command` in the constructor is a clean way to separate the UI element from the business logic it triggers.