#!/bin/bash
# Post-generation script to fix Python SDK after openapi-generator runs
# This restores custom imports and fixes FeelValue references

set -e

SDK_DIR="/mnt/fast/projects/personal/dmn/dmn-python-sdk"

echo "Fixing Python SDK post-generation..."

# Fix FeelValue imports in all generated model files
echo "Fixing FeelValue imports in models..."
find "$SDK_DIR/quantumdmn/models" -name '*.py' -type f -exec sed -i \
    's/from quantumdmn\.models\.feel_value import FeelValue/from quantumdmn.model.feel_value import FeelValue/g' {} \;

# Fix FeelValue import in main __init__.py
echo "Fixing FeelValue import in __init__.py..."
sed -i 's/from quantumdmn\.models\.feel_value import FeelValue/from quantumdmn.model.feel_value import FeelValue/g' \
    "$SDK_DIR/quantumdmn/__init__.py"

# Add custom class imports to __init__.py if missing
echo "Ensuring custom class imports in __init__.py..."
if ! grep -q "from quantumdmn.engine import DmnEngine" "$SDK_DIR/quantumdmn/__init__.py"; then
    # Add imports after the last 'from quantumdmn.models' line
    sed -i '/from quantumdmn\.models\./a\
\
# custom classes\
from quantumdmn.engine import DmnEngine\
from quantumdmn.auth import ZitadelTokenProvider\
from quantumdmn.model.feel_value import FeelValue' "$SDK_DIR/quantumdmn/__init__.py"
fi

# Add custom classes to __all__ if missing
if ! grep -q "DmnEngine" "$SDK_DIR/quantumdmn/__init__.py"; then
    echo "Adding custom classes to __all__..."
    sed -i '/__all__ = \[/a\
    "DmnEngine",\
    "ZitadelTokenProvider",\
    "FeelValue",' "$SDK_DIR/quantumdmn/__init__.py"
fi

# Remove generated FeelValue stub if it exists
if [ -f "$SDK_DIR/quantumdmn/models/feel_value.py" ]; then
    echo "Removing generated FeelValue stub..."
    rm -f "$SDK_DIR/quantumdmn/models/feel_value.py"
fi

if [ -f "$SDK_DIR/test/test_feel_value.py" ]; then
    echo "Removing generated FeelValue test..."
    rm -f "$SDK_DIR/test/test_feel_value.py"
fi

echo "Python SDK post-generation fixes complete!"
