# Insight: `cache_integer_widget.py`

## 1. Widget Type

`CacheIntegerWidget` is a composite `QWidget` that combines a `QLabel` with a `QComboBox`. It is structurally identical to the `CacheFloatWidget` but serves a different, specific purpose.

## 2. Purpose

This widget allows the user to select the compression format for the *integer-based* media cache within Autodesk Flame. This setting is distinct from the float cache and affects performance and disk space for non-floating-point media.

## 3. Behavior and Functionality

The widget's functionality mirrors the `CacheFloatWidget` precisely, demonstrating a reusable component pattern:

- **Data-Driven Population:** It is populated by the `set_values(values)` method, which takes a list of dictionaries. Each dictionary contains a user-friendly `"format"` string and an internal `"code"`.
- **Separation of Display and Data:** It uses `addItem(text, data)` to associate the visible format name with its internal code.
- **Value Retrieval:** The `get()` method returns the `code` (data) of the selected item, not the visible text.
- **Value Setting:** The `set(value)` method finds and selects the item corresponding to the provided `code`.

## 4. Key Attributes and Properties

- `self.layout`: A `QHBoxLayout` for horizontal arrangement.
- `self.label`: A `QLabel` with the static text "Cache Integer:".
- `self.combobox`: The `QComboBox` instance for the selection.

## 5. Signals and Slots

- **Signals:** The underlying `QComboBox` emits standard `currentIndexChanged(int)` and `currentTextChanged(const QString &)` signals.
- **Slots (Public Methods):**
  - `set_values(self, values)`: Populates the dropdown.
  - `get(self)`: Returns the internal `code` of the selection.
  - `set(self, value)`: Sets the selection based on its `code`.

## 6. Dependencies and Relationships

- **`src.ui.ui_config`**: Imports `ui_config` to use the `COMBOBOX_HEIGHT` constant.
- **External Controller/Data Source**: It depends on a controller to supply the list of valid integer cache formats (as a list of dictionaries). This data is managed externally.
- **Relationship to Project Configuration**: The `code` selected here is a critical piece of technical data used by the project creation logic to correctly configure the Flame project's caching settings.

## 7. UI/UX Notes

This widget effectively reuses the same robust design pattern as the float cache widget. It provides a user-friendly selection menu while ensuring the application works with clean, unambiguous internal codes. This consistency in design simplifies both the user experience and the developer's task of managing the UI state.