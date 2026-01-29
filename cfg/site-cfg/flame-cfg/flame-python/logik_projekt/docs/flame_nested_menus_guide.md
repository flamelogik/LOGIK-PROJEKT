# Autodesk Flame Custom UI Actions: Creating Nested Contextual Menus

## Overview

Creating deeply nested contextual menus in Autodesk Flame requires understanding how the `hierarchy` parameter works. This guide demonstrates the correct approach using real-world examples.

## Key Principles

1. **Each menu level is a separate dictionary entry** in the returned list
2. **The `hierarchy` parameter specifies the full path** to where the menu item should appear in the tree
3. **Intermediate levels need `'actions': []`** (empty actions list)
4. **Only the deepest level contains the actual action** with `execute`, `isVisible`, etc.

## The Hierarchy Parameter

The `hierarchy` parameter is a **list of parent menu names** that defines the complete path from the root to the current menu item's placement:

- `'hierarchy': []` = Root level (no parents)
- `'hierarchy': ['parent']` = Under one parent
- `'hierarchy': ['parent', 'child']` = Under parent > child
- `'hierarchy': ['parent', 'child', 'grandchild']` = Under parent > child > grandchild

## 4-Layer Deep Example

This example creates: **Tools → Import → Media → Load Files**

```python
def get_media_panel_custom_ui_actions():
    return [
        # Layer 1: Root menu
        {
            'name': 'Tools',
            'hierarchy': [],
            'actions': []
        },
        # Layer 2: First submenu
        {
            'name': 'Import',
            'hierarchy': ['Tools'],
            'order': 0,
            'actions': []
        },
        # Layer 3: Second submenu
        {
            'name': 'Media',
            'hierarchy': ['Tools', 'Import'],
            'order': 0,
            'actions': []
        },
        # Layer 4: Third submenu with the executable action
        {
            'name': 'Load Files',
            'hierarchy': ['Tools', 'Import', 'Media'],
            'order': 0,
            'separator': 'below',
            'isVisible': lambda sel: True,
            'execute': load_files_action,
            'minimumVersion': '2025'
        }
    ]
```

### How It Works

1. **'Tools'** has no hierarchy (`[]`), so it appears at the root level
2. **'Import'** has `hierarchy: ['Tools']`, so it appears as a submenu under Tools
3. **'Media'** has `hierarchy: ['Tools', 'Import']`, so it appears under Tools → Import
4. **'Load Files'** has `hierarchy: ['Tools', 'Import', 'Media']` and contains the `execute` function

The hierarchy path for each level **includes all ancestors up to and including the immediate parent**.

## 6-Layer Deep Example

This example creates: **Project → Settings → Advanced → Performance → Cache → Memory**

```python
def get_batch_custom_ui_actions():
    return [
        # Layer 1: Root
        {
            'name': 'Project',
            'hierarchy': [],
            'actions': []
        },
        # Layer 2
        {
            'name': 'Settings',
            'hierarchy': ['Project'],
            'order': 0,
            'actions': []
        },
        # Layer 3
        {
            'name': 'Advanced',
            'hierarchy': ['Project', 'Settings'],
            'order': 0,
            'actions': []
        },
        # Layer 4
        {
            'name': 'Performance',
            'hierarchy': ['Project', 'Settings', 'Advanced'],
            'order': 0,
            'actions': []
        },
        # Layer 5
        {
            'name': 'Cache',
            'hierarchy': ['Project', 'Settings', 'Advanced', 'Performance'],
            'order': 0,
            'actions': []
        },
        # Layer 6: Final level with executable action
        {
            'name': 'Memory',
            'hierarchy': ['Project', 'Settings', 'Advanced', 'Performance', 'Cache'],
            'order': 0,
            'separator': 'below',
            'isVisible': can_adjust_memory,
            'execute': configure_memory_action,
            'minimumVersion': '2025'
        }
    ]
```

### Structure Breakdown

Each layer adds one more element to the hierarchy list:

| Layer | Name | Hierarchy | Purpose |
|-------|------|-----------|---------|
| 1 | Project | `[]` | Root menu |
| 2 | Settings | `['Project']` | Under Project |
| 3 | Advanced | `['Project', 'Settings']` | Under Project > Settings |
| 4 | Performance | `['Project', 'Settings', 'Advanced']` | Under Project > Settings > Advanced |
| 5 | Cache | `['Project', 'Settings', 'Advanced', 'Performance']` | Under Project > Settings > Advanced > Performance |
| 6 | Memory | `['Project', 'Settings', 'Advanced', 'Performance', 'Cache']` | Under Project > Settings > Advanced > Performance > Cache |

## Important Notes

### What NOT to Do

❌ **Don't use nested `actions` arrays** - This won't work for deep nesting in Flame 2027

```python
# This will NOT work beyond 2 levels
{
    'name': 'Parent',
    'actions': [
        {
            'name': 'Child',
            'actions': [
                {
                    'name': 'Grandchild',  # This won't appear!
                    'execute': my_function
                }
            ]
        }
    ]
}
```

### What TO Do

✅ **Use separate dictionary entries with `hierarchy` paths**

```python
# This WILL work for any depth
[
    {'name': 'Parent', 'hierarchy': [], 'actions': []},
    {'name': 'Child', 'hierarchy': ['Parent'], 'actions': []},
    {'name': 'Grandchild', 'hierarchy': ['Parent', 'Child'], 'actions': [
        {'name': 'Action', 'execute': my_function}
    ]},
]
```

## Common Gotchas

### 1. Forgetting Empty Actions Lists

Every menu item except the final leaf needs `'actions': []`:

```python
# ✅ Correct
{
    'name': 'Submenu',
    'hierarchy': ['Root'],
    'actions': []  # Required!
}

# ❌ Wrong
{
    'name': 'Submenu',
    'hierarchy': ['Root']
    # Missing 'actions': []
}
```

### 2. Incomplete Hierarchy Paths

Always include the **complete path** from root to parent:

```python
# ✅ Correct - full path
{
    'name': 'Item',
    'hierarchy': ['Root', 'Parent', 'Grandparent']
}

# ❌ Wrong - only immediate parent
{
    'name': 'Item',
    'hierarchy': ['Grandparent']  # Flame won't find it!
}
```

### 3. Order of Dictionary Entries

Entries should be defined in **hierarchical order** (parent before child), though the exact order is less critical than correct hierarchy definitions.

```python
# Best practice: define from root downward
[
    {'name': 'Root', 'hierarchy': []},
    {'name': 'Child1', 'hierarchy': ['Root']},
    {'name': 'Child2', 'hierarchy': ['Root']},
    {'name': 'Grandchild', 'hierarchy': ['Root', 'Child1']},
]
```

## Reference: Available Hooks

These custom UI action hooks support nested menus in Flame 2027+:

- `get_main_menu_custom_ui_actions()` - Main menu
- `get_media_panel_custom_ui_actions()` - Media Panel context menu
- `get_batch_custom_ui_actions()` - Batch context menu
- `get_timeline_custom_ui_actions()` - Timeline context menu
- `get_action_custom_ui_actions()` - Action context menu
- `get_mediahub_files_custom_ui_actions()` - MediaHub Files menu
- `get_mediahub_archives_custom_ui_actions()` - MediaHub Archives menu

All follow the same hierarchical structure principles.

## Debugging

Add print statements to verify your menu structure:

```python
def get_batch_custom_ui_actions():
    menu_structure = [
        # ... your menu definitions ...
    ]
    
    print("\n" + "="*80)
    print("DEBUG: Menu structure")
    for i, item in enumerate(menu_structure):
        print(f"  [{i}] name='{item.get('name')}', hierarchy={item.get('hierarchy')}")
    print("="*80 + "\n")
    
    return menu_structure
```

Check the Flame console output to verify the structure is being created correctly.