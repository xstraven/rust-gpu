#!/bin/bash

echo "Building WASM package..."

cd ..

wasm-pack build --target web --out-dir website/static/pkg

if [ $? -eq 0 ]; then
    echo "WASM build successful!"
    echo "Generated files in website/static/pkg/"
else
    echo "WASM build failed!"
    exit 1
fi